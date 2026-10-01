# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.774 |                21.040 |              13.192 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.280 | 0.218 |               148.240 |               3.540 |         25 |              0.720 |              0.720 |          0.555 |          0.718 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.207 |               141.160 |               3.899 |         25 |              0.680 |              0.680 |          0.566 |          0.732 |
| B_L2 (+ object appearance)                      |          0.280 | 0.210 |               149.040 |               3.698 |         25 |              0.720 |              0.720 |          0.564 |          0.729 |
| B_L3 (+ distractors)                            |          0.320 | 0.228 |               141.800 |               4.134 |         25 |              0.680 |              0.680 |          0.546 |          0.705 |

- **L1: success drop 0.720 absolute, 72.0% relative · SPL drop 0.555 absolute**
- **L2noT: success drop 0.680 absolute, 68.0% relative · SPL drop 0.566 absolute**
- **L2: success drop 0.720 absolute, 72.0% relative · SPL drop 0.564 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.546 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
