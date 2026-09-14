# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.573 |                53.480 |              11.806 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.120 | 0.065 |               184.760 |              -0.569 |         25 |              0.840 |              0.875 |          0.509 |          0.887 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.200 | 0.122 |               171.000 |               0.472 |         25 |              0.760 |              0.792 |          0.451 |          0.787 |
| B_L2 (+ object appearance)                      |          0.280 | 0.172 |               156.040 |               1.865 |         25 |              0.680 |              0.708 |          0.402 |          0.701 |
| B_L3 (+ distractors)                            |          0.400 | 0.285 |               149.400 |               3.223 |         25 |              0.560 |              0.583 |          0.288 |          0.503 |

- **L1: success drop 0.840 absolute, 87.5% relative · SPL drop 0.509 absolute**
- **L2noT: success drop 0.760 absolute, 79.2% relative · SPL drop 0.451 absolute**
- **L2: success drop 0.680 absolute, 70.8% relative · SPL drop 0.402 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.288 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
