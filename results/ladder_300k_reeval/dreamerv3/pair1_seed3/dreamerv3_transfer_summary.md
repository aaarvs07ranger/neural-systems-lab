# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.516 |                51.000 |               8.943 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.400 | 0.343 |               138.960 |               2.317 |         25 |              0.440 |              0.524 |          0.173 |          0.335 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.320 |               148.080 |               1.369 |         25 |              0.520 |              0.619 |          0.196 |          0.380 |
| B_L2 (+ object appearance)                      |          0.280 | 0.280 |               147.120 |               0.914 |         25 |              0.560 |              0.667 |          0.236 |          0.458 |
| B_L3 (+ distractors)                            |          0.280 | 0.243 |               153.080 |               1.390 |         25 |              0.560 |              0.667 |          0.273 |          0.529 |

- **L1: success drop 0.440 absolute, 52.4% relative · SPL drop 0.173 absolute**
- **L2noT: success drop 0.520 absolute, 61.9% relative · SPL drop 0.196 absolute**
- **L2: success drop 0.560 absolute, 66.7% relative · SPL drop 0.236 absolute**
- **L3: success drop 0.560 absolute, 66.7% relative · SPL drop 0.273 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
