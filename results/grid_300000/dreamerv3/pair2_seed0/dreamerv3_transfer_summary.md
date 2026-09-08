# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.636 |                45.920 |               8.807 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.772 |                24.120 |              10.513 |         25 |             -0.160 |             -0.190 |         -0.136 |         -0.214 |
| B_L2 (+ object appearance)  |          1.000 | 0.763 |                32.720 |              10.473 |         25 |             -0.160 |             -0.190 |         -0.127 |         -0.200 |
| B_L3 (+ distractors)        |          1.000 | 0.772 |                22.000 |              10.556 |         25 |             -0.160 |             -0.190 |         -0.137 |         -0.215 |

- **L1: success drop -0.160 absolute, -19.0% relative · SPL drop -0.136 absolute**
- **L2: success drop -0.160 absolute, -19.0% relative · SPL drop -0.127 absolute**
- **L3: success drop -0.160 absolute, -19.0% relative · SPL drop -0.137 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
