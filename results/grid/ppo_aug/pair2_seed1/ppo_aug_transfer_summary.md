# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.780 |                10.360 |              10.705 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.780 |                10.920 |              10.700 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L2 (+ object appearance)  |          0.960 | 0.740 |                18.400 |              10.211 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| B_L3 (+ distractors)        |          0.960 | 0.740 |                18.400 |              10.211 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
