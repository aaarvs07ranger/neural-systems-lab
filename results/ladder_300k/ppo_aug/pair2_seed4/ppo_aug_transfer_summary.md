# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.700 |                24.600 |               9.743 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.620 |                39.880 |               8.788 |         25 |              0.080 |              0.087 |          0.080 |          0.114 |
| B_L2 (+ object appearance)  |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |
| B_L3 (+ distractors)        |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |

- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
