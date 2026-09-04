# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.654 |                39.800 |               8.766 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.614 |                47.240 |               8.294 |         25 |              0.040 |              0.048 |          0.040 |          0.061 |
| B_L2 (+ object appearance)  |          0.760 | 0.607 |                54.560 |               7.817 |         25 |              0.080 |              0.095 |          0.047 |          0.071 |
| B_L3 (+ distractors)        |          0.760 | 0.607 |                54.560 |               7.817 |         25 |              0.080 |              0.095 |          0.047 |          0.071 |

- **L1: success drop 0.040 absolute, 4.8% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.080 absolute, 9.5% relative · SPL drop 0.047 absolute**
- **L3: success drop 0.080 absolute, 9.5% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
