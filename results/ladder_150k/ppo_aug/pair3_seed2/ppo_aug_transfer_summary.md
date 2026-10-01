# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.320 | 0.200 |               140.680 |               2.597 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.120 | 0.064 |               177.200 |              -0.600 |         25 |              0.200 |              0.625 |          0.136 |          0.679 |
| B_L2 (+ object appearance)  |          0.120 | 0.060 |               177.440 |              -0.635 |         25 |              0.200 |              0.625 |          0.140 |          0.702 |
| B_L3 (+ distractors)        |          0.120 | 0.060 |               177.440 |              -0.635 |         25 |              0.200 |              0.625 |          0.140 |          0.702 |

- **L1: success drop 0.200 absolute, 62.5% relative · SPL drop 0.136 absolute**
- **L2: success drop 0.200 absolute, 62.5% relative · SPL drop 0.140 absolute**
- **L3: success drop 0.200 absolute, 62.5% relative · SPL drop 0.140 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
