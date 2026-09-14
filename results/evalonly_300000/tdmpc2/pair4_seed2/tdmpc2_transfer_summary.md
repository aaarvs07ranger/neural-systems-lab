# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.773 |                26.840 |              12.603 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.436 |               109.720 |               8.459 |         25 |              0.240 |              0.250 |          0.337 |          0.436 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.103 |               180.760 |               0.308 |         25 |              0.840 |              0.875 |          0.670 |          0.867 |
| B_L2 (+ object appearance)                      |          0.080 | 0.065 |               189.640 |               0.466 |         25 |              0.880 |              0.917 |          0.708 |          0.916 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.360 |              -0.656 |         25 |              0.920 |              0.958 |          0.733 |          0.948 |

- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.337 absolute**
- **L2noT: success drop 0.840 absolute, 87.5% relative · SPL drop 0.670 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.708 absolute**
- **L3: success drop 0.920 absolute, 95.8% relative · SPL drop 0.733 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
