# Experiment tracker

One canonical record per training run, with full provenance — requested by
Vishwas (2026-08-12 meeting) so results never live only in scattered artifacts.

| file | role |
|---|---|
| `results/tracker/runs.csv` | **canonical store** — one row per training run; append/update via `scripts/tracker.py`, never by hand-typing metrics |
| `results/tracker/summary.md` | **generated view** — aggregate tables + full run table; rebuilt by `render`, never edited by hand |
| `results/tracker/houses.csv` | **per-house facts**, one row per house pair × rung: target, whether it could be swapped, floor cells, clutter kept, C1–C3 gate, and how much the image changed. Per house, not per run — every agent in a house sees the same images |
| `scripts/tracker.py` | the only writer of both files |

## What counts as a run

**One row = one trained agent measured at one rung.** A legacy sweep run
evaluated one shifted house, so it is one row. A grid agent was evaluated on
every rung of its house pair, so it has one row per rung; the `A_*` columns
repeat across its rows by construction (every rung is scored against that
agent's own house A). The metric columns are read from the run's
`*_transfer_summary.csv` — numbers are never manually transcribed.

### Training seed vs evaluation seeds (do not confuse)

* **Training seed** (`seed` column): seeds init + action sampling + env
  start-pose order for the whole training run. Different training seeds =
  independently raised agents; reported as mean ± std across seeds.
* **Evaluation seeds** (`eval_seed_base`, 10000+): per-episode start-pose
  seeds during eval, re-seeded explicitly each episode and **identical on
  variants A and B** (paired starts). These are part of the protocol, not a
  source of run-to-run variation, and are the same for every run.

## Cohorts

* `grid_300k` — **the headline.** 4 agent types × 5 house pairs × 5 seeds at 300k
  env steps, protocol v2. Rungs L1, L2, L3 for every agent, plus L2noT for the 93
  agents whose saved model still existed (from the eval-only sweep, or from the
  run's own evaluation where it already included L2noT).
* `grid_150k` — the same grid at 150k env steps (appendix; the two-budget
  comparison). Rungs L1, L2, L3. Ids have no budget tag (`ppo-v2_pair0_L1_s0`), as
  when first ingested; 300k ids carry `-v2-300k`.
* `rerun_300k` — 7 agents retrained because their saved model had been deleted.
  Same seed, **different agent**. Never the headline; used for those cells' L2noT
  comparison and as rerun-variance evidence. Ids end in `_rerun`.
* `sweep` — protocol-v1 single-house seed sweeps (pair0, L1 only). Superseded by
  the grids; kept for history.
* `main` — early single-seed runs (history).
* `archive` — invalid/undertrained runs kept as negative results
  (e.g. the DreamerV3 ratio-32 actor collapse). Never cite as data points.

**House-A competency:** any row whose house-A success is below 0.5 says so in
`notes`. Such runs stay in the tracker and in every success-rate table; they are
left out only of relative-drop comparisons, where a near-zero denominator makes
the ratio meaningless (rule fixed 2026-09-05).

## Column glossary

| column | meaning |
|---|---|
| `experiment_id` | `{baseline}[-recipetag]_{pair}_{level}_s{seed}[_{suffix}]` — unique, stable key |
| `date` | legacy cohorts: run completion date from job logs. Grid and rerun cohorts: the date the result table first entered the repo — an upper bound on completion, and checkable with `git log` |
| `baseline` | `ppo` / `ppo_aug` / `dreamerv3` / `tdmpc2` |
| `architecture_class` | the architecture-class axis of the benchmark |
| `cohort` | `grid_300k` / `grid_150k` / `rerun_300k` / `sweep` / `main` / `archive` (see above) |
| `seed` | **training** seed |
| `house_pair` | paired-house id (`pair0`–`pair4`; ProcTHOR index in `environment_parameters` and `houses.csv`) |
| `shift_level` | rung: `L1` walls/floor/lighting; `L2noT` L1 + every object's appearance except the target; `L2` L1 + every object's appearance incl. the target; `L3` L2 + distractors. (Paper names: L1, L2, L3, L4 respectively for L1, L2noT, L2, L3.) |
| `environment_parameters` | compact description of the env/shift (house size, shift recipe, variant seed) |
| `object_parameters` | task-object settings (e.g. `target=Fridge`) |
| `task` | task type (`objectnav`; multi-step interactive task planned) |
| `training_recipe` | published-recipe identifier incl. the compute knob (fairness rule: cross-baseline claims only at published recipes) |
| `train_steps` | env-step budget (the cross-baseline fairness currency) |
| `eval_episodes` / `eval_seed_base` | paired-eval protocol parameters |
| `git_commit` | repo state when the job was submitted: the last commit before the submission time (see caveats) |
| `slurm_job` | klone job id; `array_task` when known per cell; `+`-joined when a cell may have come from either of two submissions |
| `A_*` / `B_*` | metric in house A / in this row's rung. For L2noT rows from the eval-only sweep, `A_*` come from that same re-evaluation |
| `relative_success_drop` | `(A−B)/A` success, per run |
| `relative_SPL_drop` | `(A−B)/A` SPL, per run |
| `episode_length_ratio` | `B/A` mean episode length |
| `status` | `complete` / `superseded` / `invalid` |
| `results_path` | where the raw tables live in the repo |
| `notes` | anything a future reader must know |

## Rebuilding

```bash
python scripts/tracker.py rebuild   # runs.csv + houses.csv from every committed result
python scripts/tracker.py render    # summary.md
```

`rebuild` starts from an empty table and re-ingests everything, so it is the
safe way to pick up new results. It needs results to be **committed** (the grid
`date` column comes from git).

## Adding runs (legacy commands)

After rsyncing a sweep back into `results/sweeps/<name>/seed<N>/`:

```bash
python scripts/tracker.py ingest-sweep results/sweeps/ppo_aug \
    --prefix ppo_aug --baseline ppo_aug --date 2026-08-24 \
    --git-commit <sha> --slurm-job <jobid> \
    --recipe "SB3 PPO defaults + photometric jitter, 150k env steps"
python scripts/tracker.py render
```

Single runs: `python scripts/tracker.py add --summary <summary.csv> ...`
(see `--help`). Re-ingestion is idempotent (upsert by `experiment_id`).
`python scripts/tracker.py backfill` rebuilds every historical row from the
committed artifacts.

## How aggregates are computed

Grid cohorts: success rates are means over every agent; shares of house-A
success lost are means over agents with house-A success ≥ 0.5. L2noT is not
pooled in `summary.md` (7 of its measurements are on retrained agents); its
analysis compares each agent with itself in `results/tables/target_effect_tests.md`.

Legacy sweep cohort:

Grouped by `(baseline, training_recipe, house_pair, shift_level)` over the
`sweep` cohort. **Relative drops are computed per seed and then averaged**
(mean ± std of per-seed drops, ddof=1) — matching the committed
`results/sweeps/*/aggregate.md` convention. This differs from the drop of
the means when B-variance is high (PPO), so don't mix the two.

## Provenance caveats

* `git_commit` for the historical cluster runs is the documented repo state
  at launch (session log). Intervening commits in each range added results
  or lockfiles only — the training/eval pipeline is code-identical across
  each range.
* The two `archive` DreamerV3 runs predate the first git commit; their code
  state was later committed at `9fe95b6`.
* Grid `git_commit` values were recovered on 2026-09-15 by matching each job's
  submission time (session transcript) to `git log`. Between the 300k launch
  (`ad21a37`) and the last resubmission (`3e4cede`) only sbatch scripts and the
  L2noT evaluation rung changed; training code is identical. Before that
  rebuild, every 150k grid row wrongly carried `bf3d777` (a later commit) and
  pair0's house description regardless of pair; both are fixed.
* DreamerV3 300k cells other than the 6 listed individually came from either the
  first submission (`39720497`) or the resubmission (`39945496`); which one is not
  recoverable without the cluster logs, so both ids are recorded.
* The C1–C3 gate for L2noT passed 20/20 (job log, 2026-09-13) but the per-rung
  record was not written into the committed `verification.json`; `houses.csv`
  says "not recorded" rather than guessing.
* Protocol limitations, legacy cohorts (v1): eval start poses not held out from
  training; one house pair at L1. Fixed in protocol v2 (the grids).
* All cohorts: dense-shaped reward + auto-termination (easier than strict
  Habitat ObjectNav); TD-MPC2 and DreamerV3 evaluation is stochastic, so single
  cells vary between re-evaluations (pooled means move ≤ 0.023).
