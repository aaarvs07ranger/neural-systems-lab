# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.655 |                31.040 |               9.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.655 |                31.120 |               9.265 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L2 (+ object appearance)  |          0.800 | 0.575 |                46.440 |               8.294 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |
| B_L3 (+ distractors)        |          0.800 | 0.575 |                46.440 |               8.294 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**
- **L3: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
