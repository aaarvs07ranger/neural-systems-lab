# TD-MPC2 baseline (next milestone — not yet implemented)

Plan:

1. Vendor the official TD-MPC2 PyTorch implementation (`nicklashansen/tdmpc2`,
   pinned commit) into this folder.
2. TD-MPC2 expects continuous actions by default — use its discrete-action head
   (or a one-hot relaxation wrapper) over our Discrete(5) ObjectNav action space,
   and its pixel encoder for the 128x128x3 uint8 observations.
3. Implement `models.common.BaselineAdapter` so `main.py --baseline tdmpc2`
   reuses the identical A->B transfer-eval and reporting code.
4. Keep the training budget and eval protocol identical to PPO for a fair table.

MPS notes: TD-MPC2 planning (MPPI/CEM) is batch-heavy — benchmark planner batch
sizes on M4; run with `PYTORCH_ENABLE_MPS_FALLBACK=1` (set automatically by main.py).
