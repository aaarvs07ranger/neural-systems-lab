# Experiment tracker

One canonical record per training run, with full provenance — requested by
Vishwas (2026-08-12 meeting) so results never live only in scattered artifacts.

| file | role |
|---|---|
| `results/tracker/runs.csv` | **canonical store** — one row per training run; append/update via `scripts/tracker.py`, never by hand-typing metrics |
| `results/tracker/summary.md` | **generated view** — aggregate mean±std tables + full run table; rebuilt by `render`, never edited by hand |
| `scripts/tracker.py` | the only writer of both files |

## What counts as a run

**One row = one training run**: one `baseline` trained with one **training
seed** on one `house_pair` at one `shift_level`, then evaluated with the
frozen-policy paired A/B protocol. The A/B metric columns come from that
run's `*_transfer_summary.csv` — ingestion reads the artifact, so numbers
are never manually transcribed.

### Training seed vs evaluation seeds (do not confuse)

* **Training seed** (`seed` column): seeds init + action sampling + env
  start-pose order for the whole training run. Different training seeds =
  independently raised agents; reported as mean ± std across seeds.
* **Evaluation seeds** (`eval_seed_base`, 10000+): per-episode start-pose
  seeds during eval, re-seeded explicitly each episode and **identical on
  variants A and B** (paired starts). These are part of the protocol, not a
  source of run-to-run variation, and are the same for every run.

## Cohorts

* `sweep` — seed-sweep runs; the **only cohort used for aggregates/claims**.
* `main` — early single-seed runs (kept for history; superseded by sweeps).
* `archive` — invalid/undertrained runs kept as negative results
  (e.g. the DreamerV3 ratio-32 actor collapse). Never cite as data points.

## Column glossary

| column | meaning |
|---|---|
| `experiment_id` | `{baseline}[-recipetag]_{pair}_{level}_s{seed}[_{suffix}]` — unique, stable key |
| `date` | run completion date (UTC-agnostic, from job logs) |
| `baseline` | `ppo` / `ppo_aug` / `dreamerv3` / `tdmpc2` |
| `architecture_class` | the architecture-class axis of the benchmark |
| `cohort` | `sweep` / `main` / `archive` (see above) |
| `seed` | **training** seed |
| `house_pair` | paired-house id (`pair0` = procthor10k-train house 0) |
| `shift_level` | severity rung: `L1` textures+lighting; `L2` +object appearance; `L3` +distractors; `L4` +layout (planned) |
| `environment_parameters` | compact description of the env/shift (house size, shift recipe, variant seed) |
| `object_parameters` | task-object settings (e.g. `target=Fridge`) |
| `task` | task type (`objectnav`; multi-step interactive task planned) |
| `training_recipe` | published-recipe identifier incl. the compute knob (fairness rule: cross-baseline claims only at published recipes) |
| `train_steps` | env-step budget (the cross-baseline fairness currency) |
| `eval_episodes` / `eval_seed_base` | paired-eval protocol parameters |
| `git_commit` | repo state the run executed at (see caveat below) |
| `slurm_job` | klone job id(s), `+`-joined across preemption resumes |
| `A_*` / `B_*` | metric on train visuals / zero-shot visuals |
| `relative_success_drop` | `(A−B)/A` success, per run |
| `relative_SPL_drop` | `(A−B)/A` SPL, per run |
| `episode_length_ratio` | `B/A` mean episode length |
| `status` | `complete` / `superseded` / `invalid` |
| `results_path` | where the raw tables live in the repo |
| `notes` | anything a future reader must know |

## Adding runs

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
* Known protocol limitations (tracked, not hidden): eval start poses are not
  held out from training (the A→B contrast is unaffected — poses are paired
  and identical on both sides); n=1 house pair at L1 so far; dense-shaped
  reward + auto-termination (easier than strict Habitat ObjectNav);
  TD-MPC2 eval actions mildly stochastic (upstream ShiftAug active at eval).
