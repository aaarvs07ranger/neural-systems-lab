# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.719 |                 9.840 |              10.824 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.160 | 0.129 |               168.520 |              -0.200 |         25 |              0.840 |              0.840 |          0.590 |          0.821 |
| B_L2 (+ object appearance)  |          0.160 | 0.160 |               169.120 |              -0.130 |         25 |              0.840 |              0.840 |          0.559 |          0.778 |
| B_L3 (+ distractors)        |          0.160 | 0.160 |               169.120 |              -0.130 |         25 |              0.840 |              0.840 |          0.559 |          0.778 |

- **L1: success drop 0.840 absolute, 84.0% relative · SPL drop 0.590 absolute**
- **L2: success drop 0.840 absolute, 84.0% relative · SPL drop 0.559 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.559 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
