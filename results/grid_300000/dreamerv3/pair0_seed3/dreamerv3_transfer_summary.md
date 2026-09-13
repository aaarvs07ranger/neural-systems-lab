# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.787 |                16.200 |              11.554 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.720 |                23.640 |              11.469 |         25 |              0.000 |              0.000 |          0.067 |          0.085 |
| B_L2 (+ object appearance)  |          0.920 | 0.546 |                75.960 |              10.041 |         25 |              0.080 |              0.080 |          0.241 |          0.306 |
| B_L3 (+ distractors)        |          0.840 | 0.502 |                77.040 |               9.184 |         25 |              0.160 |              0.160 |          0.285 |          0.362 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.067 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.241 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.285 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
