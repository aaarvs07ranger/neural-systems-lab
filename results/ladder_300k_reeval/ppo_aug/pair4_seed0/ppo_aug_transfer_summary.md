# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.740 |                25.360 |              12.578 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.680 | 0.474 |                75.800 |               8.339 |         25 |              0.280 |              0.292 |          0.266 |          0.359 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.344 |               114.240 |               5.539 |         25 |              0.480 |              0.500 |          0.396 |          0.535 |
| B_L2 (+ object appearance)                      |          0.400 | 0.319 |               125.240 |               4.218 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |
| B_L3 (+ distractors)                            |          0.400 | 0.319 |               125.240 |               4.191 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |

- **L1: success drop 0.280 absolute, 29.2% relative · SPL drop 0.266 absolute**
- **L2noT: success drop 0.480 absolute, 50.0% relative · SPL drop 0.396 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
