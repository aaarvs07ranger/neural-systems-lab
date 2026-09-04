# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.797 |                12.640 |              11.573 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.520 | 0.423 |               103.360 |               5.107 |         25 |              0.480 |              0.480 |          0.374 |          0.470 |
| B_L2 (+ object appearance)  |          0.400 | 0.281 |               130.200 |               3.440 |         25 |              0.600 |              0.600 |          0.516 |          0.648 |
| B_L3 (+ distractors)        |          0.440 | 0.282 |               126.600 |               3.894 |         25 |              0.560 |              0.560 |          0.515 |          0.646 |

- **L1: success drop 0.480 absolute, 48.0% relative · SPL drop 0.374 absolute**
- **L2: success drop 0.600 absolute, 60.0% relative · SPL drop 0.516 absolute**
- **L3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.515 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
