# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                24.880 |               9.862 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.242 |               130.840 |               2.352 |         25 |              0.560 |              0.609 |          0.452 |          0.651 |
| B_L2 (+ object appearance)  |          0.480 | 0.393 |               109.000 |               4.031 |         25 |              0.440 |              0.478 |          0.302 |          0.434 |
| B_L3 (+ distractors)        |          0.400 | 0.371 |               124.000 |               2.916 |         25 |              0.520 |              0.565 |          0.323 |          0.465 |

- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.452 absolute**
- **L2: success drop 0.440 absolute, 47.8% relative · SPL drop 0.302 absolute**
- **L3: success drop 0.520 absolute, 56.5% relative · SPL drop 0.323 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
