# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.800 | 0.571 |                48.160 |               8.257 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.574 |                48.440 |               8.265 |         25 |              0.000 |              0.000 |         -0.003 |         -0.006 |
| B_L2 (+ object appearance)  |          0.800 | 0.574 |                48.240 |               8.260 |         25 |              0.000 |              0.000 |         -0.003 |         -0.006 |
| B_L3 (+ distractors)        |          0.800 | 0.574 |                48.240 |               8.260 |         25 |              0.000 |              0.000 |         -0.003 |         -0.006 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
