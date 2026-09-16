# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.656 |                29.560 |               9.423 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.320 |               0.907 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.280 |               0.877 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |

- **L1: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **L2noT: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
