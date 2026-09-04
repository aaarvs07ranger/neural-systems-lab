# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.760 | 0.496 |                66.840 |               9.958 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.400 | 0.218 |               128.480 |               4.300 |         25 |              0.360 |              0.474 |          0.279 |          0.562 |
| B_L2 (+ object appearance)  |          0.080 | 0.059 |               185.440 |              -0.943 |         25 |              0.680 |              0.895 |          0.437 |          0.881 |
| B_L3 (+ distractors)        |          0.080 | 0.059 |               185.440 |              -0.949 |         25 |              0.680 |              0.895 |          0.437 |          0.881 |

- **L1: success drop 0.360 absolute, 47.4% relative · SPL drop 0.279 absolute**
- **L2: success drop 0.680 absolute, 89.5% relative · SPL drop 0.437 absolute**
- **L3: success drop 0.680 absolute, 89.5% relative · SPL drop 0.437 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
