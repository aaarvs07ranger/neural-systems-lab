# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.699 |                21.480 |               9.771 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.680 | 0.494 |                67.560 |               6.646 |         25 |              0.240 |              0.261 |          0.206 |          0.294 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.472 |                82.800 |               5.617 |         25 |              0.320 |              0.348 |          0.227 |          0.325 |
| B_L2 (+ object appearance)                      |          0.600 | 0.472 |                82.800 |               5.617 |         25 |              0.320 |              0.348 |          0.227 |          0.325 |
| B_L3 (+ distractors)                            |          0.640 | 0.487 |                75.240 |               6.179 |         25 |              0.280 |              0.304 |          0.212 |          0.304 |

- **L1: success drop 0.240 absolute, 26.1% relative · SPL drop 0.206 absolute**
- **L2noT: success drop 0.320 absolute, 34.8% relative · SPL drop 0.227 absolute**
- **L2: success drop 0.320 absolute, 34.8% relative · SPL drop 0.227 absolute**
- **L3: success drop 0.280 absolute, 30.4% relative · SPL drop 0.212 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
