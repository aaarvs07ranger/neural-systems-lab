# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.360 | 0.246 |               157.160 |               2.913 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.461 |               110.240 |               4.923 |         25 |             -0.240 |             -0.667 |         -0.214 |         -0.870 |
| B_L2 (+ object appearance)  |          0.560 | 0.433 |               108.080 |               4.661 |         25 |             -0.200 |             -0.556 |         -0.187 |         -0.759 |
| B_L3 (+ distractors)        |          0.920 | 0.594 |                58.840 |               9.543 |         25 |             -0.560 |             -1.556 |         -0.347 |         -1.409 |

- **L1: success drop -0.240 absolute, -66.7% relative · SPL drop -0.214 absolute**
- **L2: success drop -0.200 absolute, -55.6% relative · SPL drop -0.187 absolute**
- **L3: success drop -0.560 absolute, -155.6% relative · SPL drop -0.347 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
