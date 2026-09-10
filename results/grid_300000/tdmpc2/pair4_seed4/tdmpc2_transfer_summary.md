# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.805 |                20.320 |              13.237 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.240 | 0.134 |               164.080 |               1.035 |         25 |              0.760 |              0.760 |          0.671 |          0.834 |
| B_L2 (+ object appearance)  |          0.080 | 0.018 |               186.040 |              -1.369 |         25 |              0.920 |              0.920 |          0.787 |          0.978 |
| B_L3 (+ distractors)        |          0.040 | 0.020 |               192.640 |              -1.982 |         25 |              0.960 |              0.960 |          0.785 |          0.975 |

- **L1: success drop 0.760 absolute, 76.0% relative · SPL drop 0.671 absolute**
- **L2: success drop 0.920 absolute, 92.0% relative · SPL drop 0.787 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.785 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
