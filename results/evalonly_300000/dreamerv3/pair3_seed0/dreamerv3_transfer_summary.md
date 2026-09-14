# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.691 |                28.440 |              12.780 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.616 |         25 |              1.000 |              1.000 |          0.691 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.910 |         25 |              1.000 |              1.000 |          0.691 |          1.000 |
| B_L2 (+ object appearance)                      |          0.120 | 0.120 |               184.240 |              -1.090 |         25 |              0.880 |              0.880 |          0.571 |          0.826 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               180.560 |              -0.715 |         25 |              0.840 |              0.840 |          0.531 |          0.769 |

- **L1: success drop 1.000 absolute, 100.0% relative · SPL drop 0.691 absolute**
- **L2noT: success drop 1.000 absolute, 100.0% relative · SPL drop 0.691 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.571 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.531 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
