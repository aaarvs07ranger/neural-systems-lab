# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.800 | 0.631 |                57.920 |               9.829 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.258 |               132.520 |               2.759 |         25 |              0.440 |              0.550 |          0.373 |          0.591 |
| B_L2 (+ object appearance)  |          0.320 | 0.218 |               140.000 |               2.187 |         25 |              0.480 |              0.600 |          0.413 |          0.655 |
| B_L3 (+ distractors)        |          0.320 | 0.218 |               140.000 |               2.187 |         25 |              0.480 |              0.600 |          0.413 |          0.655 |

- **L1: success drop 0.440 absolute, 55.0% relative · SPL drop 0.373 absolute**
- **L2: success drop 0.480 absolute, 60.0% relative · SPL drop 0.413 absolute**
- **L3: success drop 0.480 absolute, 60.0% relative · SPL drop 0.413 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
