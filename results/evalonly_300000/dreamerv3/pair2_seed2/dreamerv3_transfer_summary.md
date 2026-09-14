# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.080 | 0.080 |               184.640 |              -0.442 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.637 |                66.280 |               8.460 |         25 |             -0.760 |             -9.500 |         -0.557 |         -6.958 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.540 |                96.720 |               6.498 |         25 |             -0.600 |             -7.500 |         -0.460 |         -5.748 |
| B_L2 (+ object appearance)                      |          0.720 | 0.578 |                88.760 |               6.972 |         25 |             -0.640 |             -8.000 |         -0.498 |         -6.224 |
| B_L3 (+ distractors)                            |          0.720 | 0.613 |                99.680 |               6.873 |         25 |             -0.640 |             -8.000 |         -0.533 |         -6.669 |

- **L1: success drop -0.760 absolute, -950.0% relative · SPL drop -0.557 absolute**
- **L2noT: success drop -0.600 absolute, -750.0% relative · SPL drop -0.460 absolute**
- **L2: success drop -0.640 absolute, -800.0% relative · SPL drop -0.498 absolute**
- **L3: success drop -0.640 absolute, -800.0% relative · SPL drop -0.533 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
