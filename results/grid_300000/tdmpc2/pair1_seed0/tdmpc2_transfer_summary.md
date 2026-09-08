# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.714 |                 8.200 |              10.848 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.578 |                72.880 |               8.842 |         25 |              0.120 |              0.120 |          0.136 |          0.190 |
| B_L2 (+ object appearance)  |          0.720 | 0.508 |               104.880 |               6.810 |         25 |              0.280 |              0.280 |          0.206 |          0.288 |
| B_L3 (+ distractors)        |          0.760 | 0.498 |                93.320 |               7.338 |         25 |              0.240 |              0.240 |          0.217 |          0.303 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.136 absolute**
- **L2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.206 absolute**
- **L3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.217 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
