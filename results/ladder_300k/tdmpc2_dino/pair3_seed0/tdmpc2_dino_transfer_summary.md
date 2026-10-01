# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.761 |                20.720 |              12.578 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.480 | 0.317 |               125.960 |               4.765 |         25 |              0.520 |              0.520 |          0.445 |          0.584 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.302 |               125.760 |               3.981 |         25 |              0.560 |              0.560 |          0.459 |          0.603 |
| B_L2 (+ object appearance)                      |          0.560 | 0.395 |               120.360 |               5.829 |         25 |              0.440 |              0.440 |          0.366 |          0.481 |
| B_L3 (+ distractors)                            |          0.320 | 0.213 |               147.600 |               2.404 |         25 |              0.680 |              0.680 |          0.548 |          0.720 |

- **L1: success drop 0.520 absolute, 52.0% relative · SPL drop 0.445 absolute**
- **L2noT: success drop 0.560 absolute, 56.0% relative · SPL drop 0.459 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.366 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.548 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
