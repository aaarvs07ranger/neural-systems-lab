"""How expensive is a frozen pretrained encoder, per environment step?

Decides whether a JEPA/MAE agent fits before the paper deadline. It trains
nothing: it loads each frozen encoder and times ONE 128x128 observation through
it, the way the agent would on every single environment step.

Two encoders, matched on purpose:
  I-JEPA ViT-H/14  learns by predicting REPRESENTATIONS of masked regions
  MAE    ViT-H/14  learns by predicting PIXELS of masked patches
Same architecture, same size, both pretrained on ImageNet-1K. The only
difference is the prediction target -- the paper's axis, with the pretraining
data held constant.

Design the timing assumes (and the reason it is one forward pass per step): the
encoder sits in the ENVIRONMENT as an observation wrapper, so each frame is
encoded exactly once and PPO's epochs train a small head on cached features. If
the encoder sat inside the policy, PPO's 4 epochs x 32 minibatches would re-encode
every frame and the cost below would multiply.

    python scripts/jepa_cost_check.py            # both encoders, fp32 and fp16
    python scripts/jepa_cost_check.py --iters 50
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

MODELS = {
    "ijepa": ("facebook/ijepa_vith14_1k", "predicts representations"),
    "mae": ("facebook/vit-mae-huge", "predicts pixels"),
}
OBS = 128          # our observation is 128x128x3 uint8
RESIZE = 224       # what these encoders expect
# Measured on this benchmark: the simulator alone runs ~25-100 env steps/s, so a
# per-step encoder cost well under ~10 ms is free and ~40 ms roughly halves throughput.
SIM_MS_PER_STEP = (10.0, 40.0)


def load(name: str, device: torch.device, half: bool):
    from transformers import AutoModel
    model = AutoModel.from_pretrained(name, torch_dtype=torch.float16 if half else torch.float32)
    if hasattr(model, "vit"):          # ViTMAEModel wraps the encoder
        pass
    model.eval().to(device)
    for p in model.parameters():
        p.requires_grad_(False)
    return model


@torch.no_grad()
def time_encoder(model, device: torch.device, half: bool, iters: int) -> dict:
    frame = torch.from_numpy(
        (np.random.rand(1, 3, OBS, OBS) * 255).astype(np.float32)).to(device)
    dtype = torch.float16 if half else torch.float32
    feat_dim = None
    for _ in range(10):                                   # warm-up
        x = torch.nn.functional.interpolate(frame, size=RESIZE, mode="bilinear",
                                            align_corners=False).to(dtype)
        out = model(pixel_values=x).last_hidden_state
        feat_dim = out.shape[-1]
    if device.type == "cuda":
        torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(iters):
        x = torch.nn.functional.interpolate(frame, size=RESIZE, mode="bilinear",
                                            align_corners=False).to(dtype)
        out = model(pixel_values=x).last_hidden_state
        _ = out.mean(dim=1)                                # the agent's feature vector
    if device.type == "cuda":
        torch.cuda.synchronize()
    ms = 1000 * (time.perf_counter() - t0) / iters
    mem = torch.cuda.max_memory_allocated() / 2**30 if device.type == "cuda" else 0.0
    return dict(ms_per_step=round(ms, 2), feature_dim=int(feat_dim),
                gpu_gb=round(mem, 2),
                params_m=round(sum(p.numel() for p in model.parameters()) / 1e6, 1))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--iters", type=int, default=100)
    ap.add_argument("--steps", type=int, default=300_000, help="training budget per run")
    ap.add_argument("--runs", type=int, default=50, help="2 agents x 5 houses x 5 seeds")
    ap.add_argument("--out", default="results/tables/jepa_cost_check.json")
    a = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device} ({torch.cuda.get_device_name(0) if device.type == 'cuda' else 'CPU'})")
    print(f"torch {torch.__version__}")
    results = {}
    for key, (name, what) in MODELS.items():
        for half in (False, True):
            tag = f"{key}_{'fp16' if half else 'fp32'}"
            try:
                model = load(name, device, half)
                r = time_encoder(model, device, half, a.iters)
                del model
                if device.type == "cuda":
                    torch.cuda.empty_cache()
                    torch.cuda.reset_peak_memory_stats()
            except Exception as exc:                        # noqa: BLE001 - report, don't crash
                r = dict(error=f"{type(exc).__name__}: {exc}")
            r.update(model_id=name, learns_by=what)
            results[tag] = r
            print(f"  {tag:12s} {r}")

    print("\nwhat this costs per run and for the whole sweep:")
    summary = {}
    for tag, r in results.items():
        if "error" in r:
            continue
        enc_h = r["ms_per_step"] * a.steps / 1000 / 3600
        summary[tag] = dict(
            encoder_hours_per_run=round(enc_h, 2),
            encoder_gpu_hours_total=round(enc_h * a.runs, 1),
            slowdown_vs_sim=[round(r["ms_per_step"] / s + 1, 2) for s in SIM_MS_PER_STEP],
        )
        print(f"  {tag:12s} {r['ms_per_step']:6.1f} ms/step -> {enc_h:5.2f} h/run, "
              f"{enc_h * a.runs:6.1f} GPU-h for {a.runs} runs, "
              f"x{summary[tag]['slowdown_vs_sim'][0]}-{summary[tag]['slowdown_vs_sim'][1]} wall clock")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(encoders=results, budget=summary,
                                   steps=a.steps, runs=a.runs), indent=1))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
