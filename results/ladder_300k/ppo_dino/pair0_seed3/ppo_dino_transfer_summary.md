# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.777 |                17.520 |              10.990 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.752 |                25.160 |              10.461 |         25 |              0.040 |              0.042 |          0.025 |          0.033 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.746 |                25.200 |              10.492 |         25 |              0.040 |              0.042 |          0.031 |          0.040 |
| B_L2 (+ object appearance)                      |          0.800 | 0.642 |                48.160 |               8.871 |         25 |              0.160 |              0.167 |          0.135 |          0.174 |
| B_L3 (+ distractors)                            |          0.760 | 0.612 |                55.480 |               8.332 |         25 |              0.200 |              0.208 |          0.165 |          0.212 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.025 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.135 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.165 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
