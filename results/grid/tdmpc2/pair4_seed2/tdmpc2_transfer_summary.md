# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.781 |                22.560 |              13.210 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.573 |                88.440 |              10.750 |         25 |              0.160 |              0.160 |          0.208 |          0.266 |
| B_L2 (+ object appearance)  |          0.160 | 0.073 |               176.720 |               1.460 |         25 |              0.840 |              0.840 |          0.707 |          0.906 |
| B_L3 (+ distractors)        |          0.240 | 0.131 |               171.280 |               2.500 |         25 |              0.760 |              0.760 |          0.650 |          0.832 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.208 absolute**
- **L2: success drop 0.840 absolute, 84.0% relative · SPL drop 0.707 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.650 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
