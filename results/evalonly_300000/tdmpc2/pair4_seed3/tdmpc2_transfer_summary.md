# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.786 |                19.680 |              13.240 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.492 |                95.120 |              10.572 |         25 |              0.200 |              0.200 |          0.294 |          0.374 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.285 |               140.760 |               5.503 |         25 |              0.520 |              0.520 |          0.501 |          0.637 |
| B_L2 (+ object appearance)                      |          0.520 | 0.307 |               128.080 |               5.791 |         25 |              0.480 |              0.480 |          0.479 |          0.610 |
| B_L3 (+ distractors)                            |          0.600 | 0.302 |               123.400 |               7.034 |         25 |              0.400 |              0.400 |          0.484 |          0.616 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.294 absolute**
- **L2noT: success drop 0.520 absolute, 52.0% relative · SPL drop 0.501 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.479 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.484 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
