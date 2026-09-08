# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.040 | 0.040 |               192.160 |               2.000 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.152 |               152.360 |               4.142 |         25 |             -0.240 |             -6.000 |         -0.112 |         -2.802 |
| B_L2 (+ object appearance)  |          0.800 | 0.402 |                79.200 |               9.973 |         25 |             -0.760 |            -19.000 |         -0.362 |         -9.052 |
| B_L3 (+ distractors)        |          0.840 | 0.382 |                77.640 |              10.598 |         25 |             -0.800 |            -20.000 |         -0.342 |         -8.551 |

- **L1: success drop -0.240 absolute, -600.0% relative · SPL drop -0.112 absolute**
- **L2: success drop -0.760 absolute, -1900.0% relative · SPL drop -0.362 absolute**
- **L3: success drop -0.800 absolute, -2000.0% relative · SPL drop -0.342 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
