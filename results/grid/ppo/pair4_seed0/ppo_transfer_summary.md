# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.709 |                35.440 |              12.236 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.289 |               131.560 |               2.970 |         25 |              0.560 |              0.609 |          0.420 |          0.592 |
| B_L2 (+ object appearance)  |          0.160 | 0.111 |               169.600 |              -0.180 |         25 |              0.760 |              0.826 |          0.598 |          0.843 |
| B_L3 (+ distractors)        |          0.160 | 0.111 |               169.600 |              -0.220 |         25 |              0.760 |              0.826 |          0.598 |          0.843 |

- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.420 absolute**
- **L2: success drop 0.760 absolute, 82.6% relative · SPL drop 0.598 absolute**
- **L3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.598 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
