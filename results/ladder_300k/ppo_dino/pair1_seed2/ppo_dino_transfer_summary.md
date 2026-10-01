# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                21.640 |               9.913 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.604 |                37.520 |               8.879 |         25 |              0.080 |              0.087 |          0.094 |          0.135 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.444 |                68.240 |               6.843 |         25 |              0.240 |              0.261 |          0.254 |          0.364 |
| B_L2 (+ object appearance)                      |          0.720 | 0.454 |                60.720 |               7.342 |         25 |              0.200 |              0.217 |          0.244 |          0.349 |
| B_L3 (+ distractors)                            |          0.800 | 0.536 |                45.360 |               8.372 |         25 |              0.120 |              0.130 |          0.163 |          0.233 |

- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.094 absolute**
- **L2noT: success drop 0.240 absolute, 26.1% relative · SPL drop 0.254 absolute**
- **L2: success drop 0.200 absolute, 21.7% relative · SPL drop 0.244 absolute**
- **L3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.163 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
