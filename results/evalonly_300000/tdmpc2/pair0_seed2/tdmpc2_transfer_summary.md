# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.816 |                11.280 |              11.605 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.590 |                52.520 |              11.181 |         25 |              0.000 |              0.000 |          0.226 |          0.277 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.708 |                34.800 |              10.861 |         25 |              0.040 |              0.040 |          0.108 |          0.133 |
| B_L2 (+ object appearance)                      |          0.880 | 0.540 |                89.720 |               9.238 |         25 |              0.120 |              0.120 |          0.276 |          0.338 |
| B_L3 (+ distractors)                            |          1.000 | 0.659 |                53.200 |              11.154 |         25 |              0.000 |              0.000 |          0.157 |          0.193 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.226 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.108 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.276 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.157 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
