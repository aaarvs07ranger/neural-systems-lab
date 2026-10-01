# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.629 |                35.760 |              12.010 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.387 |                87.040 |               7.683 |         25 |              0.280 |              0.304 |          0.242 |          0.385 |
| B_L2 (+ object appearance)  |          0.480 | 0.296 |               113.200 |               5.075 |         25 |              0.440 |              0.478 |          0.333 |          0.530 |
| B_L3 (+ distractors)        |          0.440 | 0.261 |               120.200 |               4.542 |         25 |              0.480 |              0.522 |          0.368 |          0.585 |

- **L1: success drop 0.280 absolute, 30.4% relative · SPL drop 0.242 absolute**
- **L2: success drop 0.440 absolute, 47.8% relative · SPL drop 0.333 absolute**
- **L3: success drop 0.480 absolute, 52.2% relative · SPL drop 0.368 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
