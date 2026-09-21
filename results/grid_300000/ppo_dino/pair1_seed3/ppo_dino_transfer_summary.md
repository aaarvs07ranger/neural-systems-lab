# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.694 |                21.720 |               9.923 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.570 |                38.080 |               8.900 |         25 |              0.080 |              0.087 |          0.125 |          0.179 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.568 |                38.160 |               8.893 |         25 |              0.080 |              0.087 |          0.126 |          0.182 |
| B_L2 (+ object appearance)                      |          0.800 | 0.525 |                46.000 |               8.420 |         25 |              0.120 |              0.130 |          0.169 |          0.243 |
| B_L3 (+ distractors)                            |          0.800 | 0.526 |                45.960 |               8.426 |         25 |              0.120 |              0.130 |          0.168 |          0.242 |

- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.125 absolute**
- **L2noT: success drop 0.080 absolute, 8.7% relative · SPL drop 0.126 absolute**
- **L2: success drop 0.120 absolute, 13.0% relative · SPL drop 0.169 absolute**
- **L3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.168 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
