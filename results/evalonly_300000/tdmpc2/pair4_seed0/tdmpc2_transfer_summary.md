# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.773 |                22.320 |              13.266 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.376 |               114.880 |               8.817 |         25 |              0.280 |              0.280 |          0.397 |          0.514 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.560 | 0.246 |               137.640 |               5.747 |         25 |              0.440 |              0.440 |          0.526 |          0.681 |
| B_L2 (+ object appearance)                      |          0.440 | 0.171 |               146.800 |               4.176 |         25 |              0.560 |              0.560 |          0.602 |          0.779 |
| B_L3 (+ distractors)                            |          0.520 | 0.216 |               133.560 |               5.167 |         25 |              0.480 |              0.480 |          0.556 |          0.720 |

- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.397 absolute**
- **L2noT: success drop 0.440 absolute, 44.0% relative · SPL drop 0.526 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.602 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.556 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
