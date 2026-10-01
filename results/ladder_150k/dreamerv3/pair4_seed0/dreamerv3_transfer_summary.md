# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.395 |                66.080 |              11.517 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.321 |                92.480 |              10.605 |         25 |              0.040 |              0.045 |          0.074 |          0.188 |
| B_L2 (+ object appearance)  |          0.760 | 0.379 |                96.080 |               9.298 |         25 |              0.120 |              0.136 |          0.016 |          0.040 |
| B_L3 (+ distractors)        |          0.760 | 0.294 |               102.360 |               9.533 |         25 |              0.120 |              0.136 |          0.101 |          0.256 |

- **L1: success drop 0.040 absolute, 4.5% relative · SPL drop 0.074 absolute**
- **L2: success drop 0.120 absolute, 13.6% relative · SPL drop 0.016 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.101 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
