# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.678 |                29.200 |               9.339 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.240 |               0.567 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.200 | 0.200 |               160.240 |               0.398 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |

- **L1: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L2noT: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
