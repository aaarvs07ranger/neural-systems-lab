# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.816 |                12.800 |              11.586 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.660 |                51.240 |              10.691 |         25 |              0.040 |              0.040 |          0.156 |          0.191 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.618 |                66.520 |               9.711 |         25 |              0.120 |              0.120 |          0.198 |          0.243 |
| B_L2 (+ object appearance)                      |          0.640 | 0.464 |               107.080 |               6.316 |         25 |              0.360 |              0.360 |          0.352 |          0.431 |
| B_L3 (+ distractors)                            |          0.680 | 0.468 |                99.200 |               6.724 |         25 |              0.320 |              0.320 |          0.348 |          0.426 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.156 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.198 absolute**
- **L2: success drop 0.360 absolute, 36.0% relative · SPL drop 0.352 absolute**
- **L3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.348 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
