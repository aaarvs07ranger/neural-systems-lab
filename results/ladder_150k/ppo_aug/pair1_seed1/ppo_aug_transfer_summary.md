# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.715 |                10.120 |              10.816 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.440 | 0.354 |               114.240 |               3.434 |         25 |              0.560 |              0.560 |          0.361 |          0.505 |
| B_L2 (+ object appearance)  |          0.480 | 0.426 |               107.200 |               3.947 |         25 |              0.520 |              0.520 |          0.290 |          0.405 |
| B_L3 (+ distractors)        |          0.320 | 0.320 |               137.840 |               1.838 |         25 |              0.680 |              0.680 |          0.395 |          0.553 |

- **L1: success drop 0.560 absolute, 56.0% relative · SPL drop 0.361 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.290 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.395 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
