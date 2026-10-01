# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.754 |                28.640 |              12.512 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.080 | 0.080 |               192.560 |              -1.171 |         25 |              0.920 |              0.920 |          0.674 |          0.894 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.120 |               188.080 |              -0.937 |         25 |              0.880 |              0.880 |          0.634 |          0.841 |
| B_L2 (+ object appearance)                      |          0.240 | 0.154 |               184.240 |               0.873 |         25 |              0.760 |              0.760 |          0.600 |          0.795 |
| B_L3 (+ distractors)                            |          0.120 | 0.091 |               187.560 |              -0.706 |         25 |              0.880 |              0.880 |          0.663 |          0.879 |

- **L1: success drop 0.920 absolute, 92.0% relative · SPL drop 0.674 absolute**
- **L2noT: success drop 0.880 absolute, 88.0% relative · SPL drop 0.634 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.600 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.663 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
