# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.628 |                46.200 |               9.657 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.658 |                43.120 |              10.510 |         25 |             -0.080 |             -0.087 |         -0.030 |         -0.047 |
| B_L2 (+ object appearance)  |          1.000 | 0.651 |                34.440 |              10.598 |         25 |             -0.080 |             -0.087 |         -0.023 |         -0.036 |
| B_L3 (+ distractors)        |          0.960 | 0.630 |                40.560 |              10.076 |         25 |             -0.040 |             -0.043 |         -0.002 |         -0.003 |

- **L1: success drop -0.080 absolute, -8.7% relative · SPL drop -0.030 absolute**
- **L2: success drop -0.080 absolute, -8.7% relative · SPL drop -0.023 absolute**
- **L3: success drop -0.040 absolute, -4.3% relative · SPL drop -0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
