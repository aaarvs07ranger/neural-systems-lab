# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.700 |                26.320 |              11.047 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.675 |                45.600 |              11.272 |         25 |             -0.040 |             -0.042 |          0.025 |          0.036 |
| B_L2 (+ object appearance)  |          0.880 | 0.593 |                59.840 |               9.751 |         25 |              0.080 |              0.083 |          0.107 |          0.153 |
| B_L3 (+ distractors)        |          0.920 | 0.590 |                56.040 |              10.253 |         25 |              0.040 |              0.042 |          0.109 |          0.156 |

- **L1: success drop -0.040 absolute, -4.2% relative · SPL drop 0.025 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.107 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.109 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
