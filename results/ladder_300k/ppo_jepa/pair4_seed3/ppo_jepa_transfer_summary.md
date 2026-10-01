# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.727 |                27.800 |              12.569 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.560 | 0.357 |                98.440 |               6.136 |         25 |              0.400 |              0.417 |          0.370 |          0.508 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.209 |               140.400 |               3.562 |         25 |              0.640 |              0.667 |          0.518 |          0.713 |
| B_L2 (+ object appearance)                      |          0.400 | 0.288 |               126.880 |               4.397 |         25 |              0.560 |              0.583 |          0.439 |          0.604 |
| B_L3 (+ distractors)                            |          0.320 | 0.241 |               140.880 |               3.276 |         25 |              0.640 |              0.667 |          0.486 |          0.669 |

- **L1: success drop 0.400 absolute, 41.7% relative · SPL drop 0.370 absolute**
- **L2noT: success drop 0.640 absolute, 66.7% relative · SPL drop 0.518 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.439 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.486 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
