# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.714 |                11.080 |              10.813 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.320 | 0.320 |               145.720 |               1.765 |         25 |              0.680 |              0.680 |          0.394 |          0.552 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.383 |               133.480 |               3.687 |         25 |              0.520 |              0.520 |          0.332 |          0.464 |
| B_L2 (+ object appearance)                      |          0.360 | 0.324 |               143.560 |               2.328 |         25 |              0.640 |              0.640 |          0.390 |          0.546 |
| B_L3 (+ distractors)                            |          0.240 | 0.240 |               154.840 |               0.620 |         25 |              0.760 |              0.760 |          0.474 |          0.664 |

- **L1: success drop 0.680 absolute, 68.0% relative · SPL drop 0.394 absolute**
- **L2noT: success drop 0.520 absolute, 52.0% relative · SPL drop 0.332 absolute**
- **L2: success drop 0.640 absolute, 64.0% relative · SPL drop 0.390 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.474 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
