# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.759 |                21.320 |              11.078 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.738 |                20.920 |              11.490 |         25 |             -0.040 |             -0.042 |          0.021 |          0.027 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.676 |                28.320 |              11.416 |         25 |             -0.040 |             -0.042 |          0.083 |          0.109 |
| B_L2 (+ object appearance)                      |          0.960 | 0.512 |                77.960 |              10.464 |         25 |              0.000 |              0.000 |          0.247 |          0.325 |
| B_L3 (+ distractors)                            |          0.960 | 0.555 |                66.200 |              10.570 |         25 |              0.000 |              0.000 |          0.203 |          0.268 |

- **L1: success drop -0.040 absolute, -4.2% relative · SPL drop 0.021 absolute**
- **L2noT: success drop -0.040 absolute, -4.2% relative · SPL drop 0.083 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.247 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.203 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
