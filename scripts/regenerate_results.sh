#!/usr/bin/env bash
# Regenerate every results table and figure from the committed per-run CSVs.
#
# Order matters only where one output feeds another: analyze_rgb_shift.py writes
# the JSON plot_rgb_shift.py reads. Everything else reads results/<set>/ directly.
# Deterministic: every random draw is seeded, so a second run reproduces every
# file byte for byte (the PNG timestamps aside).
#
#   bash scripts/regenerate_results.sh          # results/tables + results/plots + tracker
#   bash scripts/regenerate_results.sh --paper  # also paper/generated + paper/figures
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== tables"
python scripts/robust_stats.py                       # 95% CIs: ladder, reordered ladder, single changes
python scripts/robust_stats.py --set ladder_150k
python scripts/make_tables.py                        # main + per-house tables
python scripts/make_tables.py --grid ladder_150k
python scripts/analyze_grid.py > /dev/null           # declared significance tests (appendix)
python scripts/analyze_grid.py --grid ladder_150k > /dev/null
python scripts/test_target_effect.py > /dev/null     # goal-object control
python scripts/test_single_change.py > /dev/null     # single-change tests
python scripts/summarize_single_change.py            # parts vs whole, per house
python scripts/analyze_visual_shift.py > /dev/null   # first image-change analysis (5 houses)
python scripts/analyze_rgb_shift.py                  # colour shift vs drop (69 houses)

echo "== figures"
python scripts/plot_ladder.py
python scripts/plot_ladder.py --all-agents --mode light
python scripts/plot_ladder.py --grid ladder_150k
python scripts/plot_reordered.py
python scripts/plot_target_effect.py
python scripts/plot_single_change.py
python scripts/plot_visual_shift.py
python scripts/plot_rgb_shift.py

echo "== tracker"
python scripts/tracker.py rebuild
python scripts/tracker.py render

if [[ "${1:-}" == "--paper" ]]; then
    echo "== paper"
    python scripts/make_paper_tables.py
    python scripts/plot_paper_figures.py
fi
echo "done"
