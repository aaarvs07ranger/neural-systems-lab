# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.320 | 0.244 |               140.280 |               2.414 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.528 |                80.320 |               8.158 |         25 |             -0.480 |             -1.500 |         -0.284 |         -1.165 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.484 |                88.680 |               7.649 |         25 |             -0.440 |             -1.375 |         -0.240 |         -0.985 |
| B_L2 (+ object appearance)                      |          0.600 | 0.401 |               105.200 |               5.886 |         25 |             -0.280 |             -0.875 |         -0.157 |         -0.643 |
| B_L3 (+ distractors)                            |          0.640 | 0.464 |                92.560 |               6.192 |         25 |             -0.320 |             -1.000 |         -0.220 |         -0.901 |

- **L1: success drop -0.480 absolute, -150.0% relative · SPL drop -0.284 absolute**
- **L2noT: success drop -0.440 absolute, -137.5% relative · SPL drop -0.240 absolute**
- **L2: success drop -0.280 absolute, -87.5% relative · SPL drop -0.157 absolute**
- **L3: success drop -0.320 absolute, -100.0% relative · SPL drop -0.220 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
