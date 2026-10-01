# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.320 | 0.244 |               141.800 |               2.486 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.522 |                86.920 |               7.998 |         25 |             -0.480 |             -1.500 |         -0.278 |         -1.141 |
| B_L2 (+ object appearance)  |          0.640 | 0.376 |                98.920 |               6.166 |         25 |             -0.320 |             -1.000 |         -0.132 |         -0.540 |
| B_L3 (+ distractors)        |          0.440 | 0.312 |               122.520 |               3.817 |         25 |             -0.120 |             -0.375 |         -0.068 |         -0.279 |

- **L1: success drop -0.480 absolute, -150.0% relative · SPL drop -0.278 absolute**
- **L2: success drop -0.320 absolute, -100.0% relative · SPL drop -0.132 absolute**
- **L3: success drop -0.120 absolute, -37.5% relative · SPL drop -0.068 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
