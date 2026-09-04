# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.760 | 0.485 |                64.320 |               9.282 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.480 | 0.278 |               116.040 |               4.535 |         25 |              0.280 |              0.368 |          0.207 |          0.427 |
| B_L2 (+ object appearance)  |          0.520 | 0.290 |               108.520 |               5.266 |         25 |              0.240 |              0.316 |          0.196 |          0.404 |
| B_L3 (+ distractors)        |          0.480 | 0.282 |               115.080 |               4.700 |         25 |              0.280 |              0.368 |          0.204 |          0.420 |

- **L1: success drop 0.280 absolute, 36.8% relative · SPL drop 0.207 absolute**
- **L2: success drop 0.240 absolute, 31.6% relative · SPL drop 0.196 absolute**
- **L3: success drop 0.280 absolute, 36.8% relative · SPL drop 0.204 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
