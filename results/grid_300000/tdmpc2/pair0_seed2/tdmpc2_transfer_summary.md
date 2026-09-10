# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.817 |                11.240 |              11.610 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.667 |                57.000 |              10.620 |         25 |              0.040 |              0.040 |          0.150 |          0.184 |
| B_L2 (+ object appearance)  |          0.800 | 0.554 |                73.440 |               8.403 |         25 |              0.200 |              0.200 |          0.262 |          0.321 |
| B_L3 (+ distractors)        |          0.840 | 0.569 |                77.280 |               8.974 |         25 |              0.160 |              0.160 |          0.248 |          0.303 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.150 absolute**
- **L2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.262 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.248 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
