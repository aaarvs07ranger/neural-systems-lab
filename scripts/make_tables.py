"""Paper tables from the grid, generated -- never transcribed.

Every number in the paper comes from here, so a table can be regenerated from
the committed CSVs and can never drift from them. Two outputs:

  results/tables/grid_main.md       the main-body table: baseline x rung,
                                    pooled over houses, both metrics
  results/tables/grid_by_pair.md    the appendix table: every cell, with the
                                    per-house detail the main body cannot hold

Pooling is reported WITH the spread across houses, never instead of it. PPO's
L1 drop ranges 8% to 92% across the five houses, so a pooled mean alone would
describe no house in the study.

    python scripts/make_tables.py
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from config import GenerationConfig, TABLES_DIR, pair_dir

RUNGS = ["L1", "L2", "L3"]
ORDER = ["ppo", "ppo_aug", "dreamerv3", "tdmpc2"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO + aug", "dreamerv3": "DreamerV3",
        "tdmpc2": "TD-MPC2"}
CLASS = {"ppo": "model-free", "ppo_aug": "model-free + DR",
         "dreamerv3": "reconstruction WM", "tdmpc2": "decoder-free WM"}


def load() -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob("results/grid/*/*/*_transfer_summary.csv")):
        p = Path(f)
        baseline = p.parents[1].name
        pair, seed = p.parent.name.split("_seed")
        df = pd.read_csv(f).set_index("level")
        A, AS = df.loc["A", "success_rate"], df.loc["A", "spl"]
        for rung in RUNGS:
            if rung not in df.index:
                continue
            rows.append(dict(
                baseline=baseline, pair=pair, seed=int(seed), rung=rung,
                A_success=A, A_spl=AS,
                success=df.loc[rung, "success_rate"], spl=df.loc[rung, "spl"],
                drop=(A - df.loc[rung, "success_rate"]) / A if A else float("nan"),
                spl_drop=(AS - df.loc[rung, "spl"]) / AS if AS else float("nan"),
            ))
    return pd.DataFrame(rows)


def pair_meta() -> dict:
    out = {}
    for i in range(GenerationConfig().n_pairs):
        pid = f"pair{i}"
        try:
            v = json.loads((pair_dir(pid) / "verification.json").read_text())
            s = json.loads((pair_dir(pid) / "safe_assets.json").read_text())
            t = json.loads((pair_dir(pid) / "task_config.json").read_text())
            l3 = json.loads((pair_dir(pid) / "l3_prune.json").read_text())
            out[pid] = dict(cells=v["reference"]["n_reachable"],
                            target=t["target_object_type"],
                            swappable=bool(s.get("target_swappable")),
                            clutter=l3.get("n_kept"))
        except FileNotFoundError:
            pass
    return out


def main_table(d: pd.DataFrame, meta: dict) -> str:
    lines = ["# Grid — main table", "",
             "Relative drop vs each agent's own house A, pooled over "
             f"{d.pair.nunique()} house pairs x {d.seed.nunique()} seeds. "
             "`range` is across HOUSES (the mean of each house's 5 seeds), "
             "because the between-house spread is a result in its own right and "
             "a pooled mean alone would describe no house in the study.", "",
             "| baseline | class | rung | success drop | range over houses | SPL drop | range over houses | n |",
             "|---|---|---|---|---|---|---|---|"]
    for b in [x for x in ORDER if x in set(d.baseline)]:
        for rung in RUNGS:
            s = d[(d.baseline == b) & (d.rung == rung)]
            if s.empty:
                continue
            per_house = s.groupby("pair")["drop"].mean()
            per_house_spl = s.groupby("pair")["spl_drop"].mean()
            lines.append(
                f"| {NICE[b]} | {CLASS[b]} | {rung} | "
                f"{s['drop'].mean():.1%} | {per_house.min():.0%}–{per_house.max():.0%} | "
                f"{s['spl_drop'].mean():.1%} | {per_house_spl.min():.0%}–{per_house_spl.max():.0%} | "
                f"{len(s)} |")
    return "\n".join(lines) + "\n"


def by_pair_table(d: pd.DataFrame, meta: dict) -> str:
    lines = ["# Grid — per-house breakdown (appendix)", "",
             "Mean ± s.d. over 5 training seeds. `target swapped` records whether "
             "this pair's target object had a footprint-safe alternative asset: "
             "where it did not, L2 changes the appearance of everything EXCEPT "
             "the target, which is the study's natural control.", ""]
    pairs = sorted(d.pair.unique(), key=lambda p: meta.get(p, {}).get("cells", 0))
    for pid in pairs:
        m = meta.get(pid, {})
        lines += [f"## {pid} — {m.get('target','?')}, {m.get('cells','?')} reachable cells, "
                  f"{m.get('clutter','?')} distractors, "
                  f"target swapped at L2: **{'yes' if m.get('swappable') else 'NO'}**", "",
                  "| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for b in [x for x in ORDER if x in set(d.baseline)]:
            s = d[(d.baseline == b) & (d.pair == pid)]
            if s.empty:
                continue
            cells = [f"{s['A_success'].mean():.2f}"]
            for rung in RUNGS:
                r = s[s.rung == rung]["success"]
                cells.append(f"{r.mean():.2f} ± {r.std():.2f}" if len(r) else "—")
            cells.append(f"{s['A_spl'].mean():.2f}")
            for rung in RUNGS:
                r = s[s.rung == rung]["spl"]
                cells.append(f"{r.mean():.2f} ± {r.std():.2f}" if len(r) else "—")
            lines.append("| " + NICE[b] + " | " + " | ".join(cells) + " |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    d = load()
    if d.empty:
        raise SystemExit("no grid results under results/grid/")
    meta = pair_meta()
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    for name, text in (("grid_main.md", main_table(d, meta)),
                       ("grid_by_pair.md", by_pair_table(d, meta))):
        (TABLES_DIR / name).write_text(text)
        print(f"  wrote {TABLES_DIR / name}")
    done = d.groupby("baseline").pair.count() // len(RUNGS)
    print(f"  cells included: {dict(done)}")


if __name__ == "__main__":
    main()
