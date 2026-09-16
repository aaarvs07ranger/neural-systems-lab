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


def load(name: str, device: torch.device, half: bool, attn: str = ""):
    """`attn` forces an attention implementation ("sdpa" / "eager").

    Left to itself, transformers picks per model class, and the two encoders can
    end up on different kernels -- which would make a timing comparison between
    them measure the library, not the model. Both are timed under the same
    setting.
    """
    from transformers import AutoModel
    kw = {"attn_implementation": attn} if attn else {}
    model = AutoModel.from_pretrained(
        name, torch_dtype=torch.float16 if half else torch.float32, **kw)
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


@torch.no_grad()
def fidelity(name: str, device: torch.device, iters: int = 8) -> dict:
    """Does half precision give the same features as full precision?

    Half precision is ~4x faster on I-JEPA, but the agent's whole observation is
    this feature vector -- if fp16 distorted it, every JEPA/MAE number would be
    measured on a different representation than the one the encoder published.
    Compares both on identical inputs: cosine similarity and worst relative error.
    """
    from transformers import AutoModel

    lo = AutoModel.from_pretrained(name, torch_dtype=torch.float16).eval().to(device)
    hi = AutoModel.from_pretrained(name, torch_dtype=torch.float32).eval().to(device)
    cos, rel = [], []
    rng = np.random.default_rng(0)
    for i in range(iters):
        # A spread of inputs: flat, gradient, sinusoidal texture, noise.
        g = np.linspace(0, 1, RESIZE, dtype=np.float32)
        kind = i % 4
        if kind == 0:
            img = np.full((RESIZE, RESIZE), 0.5, np.float32)
        elif kind == 1:
            img = np.tile(g, (RESIZE, 1))
        elif kind == 2:
            img = 0.5 + 0.5 * np.sin(12 * np.pi * np.add.outer(g, g))
        else:
            img = rng.random((RESIZE, RESIZE), dtype=np.float32)
        x = torch.from_numpy(img).to(device)[None, None].expand(1, 3, RESIZE, RESIZE).contiguous()
        a_ = hi(pixel_values=x).last_hidden_state.mean(dim=1).float()
        b_ = lo(pixel_values=x.half()).last_hidden_state.mean(dim=1).float()
        cos.append(float(torch.nn.functional.cosine_similarity(a_, b_).item()))
        rel.append(float(((a_ - b_).abs() / a_.abs().clamp(min=1e-6)).max().item()))
    del lo, hi
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return dict(min_cosine_similarity=round(min(cos), 6),
                worst_relative_error=round(max(rel), 4), inputs=iters)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--iters", type=int, default=100)
    ap.add_argument("--steps", type=int, default=300_000, help="training budget per run")
    ap.add_argument("--runs", type=int, default=50, help="2 agents x 5 houses x 5 seeds")
    ap.add_argument("--attn", default="", choices=("", "sdpa", "eager"),
                    help="force one attention implementation for both encoders")
    ap.add_argument("--out", default="results/tables/jepa_cost_check.json")
    a = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"device: {device} ({torch.cuda.get_device_name(0) if device.type == 'cuda' else 'CPU'})")
    print(f"torch {torch.__version__}")
    print(f"attention implementation: {a.attn or 'library default (per model)'}")
    results = {}
    for key, (name, what) in MODELS.items():
        for half in (False, True):
            tag = f"{key}_{'fp16' if half else 'fp32'}"
            try:
                model = load(name, device, half, a.attn)
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

    print("\nhalf vs full precision on identical inputs (the feature IS the observation):")
    for key, (name, _what) in MODELS.items():
        try:
            f = fidelity(name, device)
        except Exception as exc:                            # noqa: BLE001
            f = dict(error=f"{type(exc).__name__}: {exc}")
        results[f"{key}_fp16_vs_fp32"] = f
        print(f"  {key:6s} {f}")

    print("\nwhat this costs per run and for the whole sweep:")
    summary = {}
    for tag, r in results.items():
        if "error" in r or "ms_per_step" not in r:   # skip the precision-comparison rows
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
