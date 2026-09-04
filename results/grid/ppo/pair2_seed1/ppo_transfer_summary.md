# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.738 |                14.720 |              10.226 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.578 |                45.400 |               8.300 |         25 |              0.160 |              0.167 |          0.160 |          0.217 |
| B_L2 (+ object appearance)  |          0.680 | 0.522 |                68.520 |               6.591 |         25 |              0.280 |              0.292 |          0.216 |          0.293 |
| B_L3 (+ distractors)        |          0.680 | 0.522 |                68.520 |               6.572 |         25 |              0.280 |              0.292 |          0.216 |          0.293 |

- **L1: success drop 0.160 absolute, 16.7% relative · SPL drop 0.160 absolute**
- **L2: success drop 0.280 absolute, 29.2% relative · SPL drop 0.216 absolute**
- **L3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.216 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
