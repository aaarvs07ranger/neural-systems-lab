# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.801 |                21.720 |              13.222 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.469 |                93.680 |              10.955 |         25 |              0.160 |              0.160 |          0.332 |          0.414 |
| B_L2 (+ object appearance)  |          0.560 | 0.330 |               130.160 |               6.489 |         25 |              0.440 |              0.440 |          0.472 |          0.589 |
| B_L3 (+ distractors)        |          0.760 | 0.423 |               103.960 |               9.338 |         25 |              0.240 |              0.240 |          0.378 |          0.472 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.332 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.472 absolute**
- **L3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.378 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
