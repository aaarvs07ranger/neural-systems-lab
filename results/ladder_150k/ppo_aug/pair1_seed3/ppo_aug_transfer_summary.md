# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.717 |                 9.200 |              10.836 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.690 |                24.360 |               9.878 |         25 |              0.080 |              0.080 |          0.027 |          0.037 |
| B_L2 (+ object appearance)  |          0.960 | 0.702 |                22.360 |              10.325 |         25 |              0.040 |              0.040 |          0.015 |          0.021 |
| B_L3 (+ distractors)        |          0.640 | 0.480 |                79.640 |               6.196 |         25 |              0.360 |              0.360 |          0.238 |          0.331 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.027 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.015 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.238 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
