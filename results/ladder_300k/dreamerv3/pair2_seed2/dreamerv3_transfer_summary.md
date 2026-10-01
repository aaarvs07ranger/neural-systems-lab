# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.080 | 0.080 |               184.640 |              -0.455 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.703 |                59.840 |               8.510 |         25 |             -0.760 |             -9.500 |         -0.623 |         -7.786 |
| B_L2 (+ object appearance)  |          0.640 | 0.540 |               116.240 |               5.892 |         25 |             -0.560 |             -7.000 |         -0.460 |         -5.752 |
| B_L3 (+ distractors)        |          0.800 | 0.596 |                88.760 |               7.803 |         25 |             -0.720 |             -9.000 |         -0.516 |         -6.452 |

- **L1: success drop -0.760 absolute, -950.0% relative · SPL drop -0.623 absolute**
- **L2: success drop -0.560 absolute, -700.0% relative · SPL drop -0.460 absolute**
- **L3: success drop -0.720 absolute, -900.0% relative · SPL drop -0.516 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
