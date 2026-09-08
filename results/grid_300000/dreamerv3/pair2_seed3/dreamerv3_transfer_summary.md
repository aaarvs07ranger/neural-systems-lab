# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.680 |                39.000 |               9.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.080 |               188.600 |              -0.021 |         25 |              0.800 |              0.909 |          0.600 |          0.882 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.040 |              -0.475 |         25 |              0.840 |              0.955 |          0.640 |          0.941 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.040 |              -0.417 |         25 |              0.840 |              0.955 |          0.640 |          0.941 |

- **L1: success drop 0.800 absolute, 90.9% relative · SPL drop 0.600 absolute**
- **L2: success drop 0.840 absolute, 95.5% relative · SPL drop 0.640 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.640 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
