# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                 8.280 |              10.685 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.400 | 0.365 |               122.840 |               3.064 |         25 |              0.600 |              0.600 |          0.414 |          0.532 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.445 |               108.360 |               4.168 |         25 |              0.520 |              0.520 |          0.334 |          0.429 |
| B_L2 (+ object appearance)                      |          0.480 | 0.445 |               108.360 |               4.168 |         25 |              0.520 |              0.520 |          0.334 |          0.429 |
| B_L3 (+ distractors)                            |          0.480 | 0.445 |               107.960 |               4.165 |         25 |              0.520 |              0.520 |          0.334 |          0.429 |

- **L1: success drop 0.600 absolute, 60.0% relative · SPL drop 0.414 absolute**
- **L2noT: success drop 0.520 absolute, 52.0% relative · SPL drop 0.334 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.334 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.334 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
