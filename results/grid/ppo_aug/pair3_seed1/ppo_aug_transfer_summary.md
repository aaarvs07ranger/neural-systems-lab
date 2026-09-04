# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.680 | 0.484 |                83.200 |               7.932 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.240 | 0.166 |               154.680 |               1.364 |         25 |              0.440 |              0.647 |          0.317 |          0.656 |
| B_L2 (+ object appearance)  |          0.240 | 0.164 |               154.560 |               1.212 |         25 |              0.440 |              0.647 |          0.320 |          0.661 |
| B_L3 (+ distractors)        |          0.240 | 0.164 |               154.560 |               1.148 |         25 |              0.440 |              0.647 |          0.320 |          0.661 |

- **L1: success drop 0.440 absolute, 64.7% relative · SPL drop 0.317 absolute**
- **L2: success drop 0.440 absolute, 64.7% relative · SPL drop 0.320 absolute**
- **L3: success drop 0.440 absolute, 64.7% relative · SPL drop 0.320 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
