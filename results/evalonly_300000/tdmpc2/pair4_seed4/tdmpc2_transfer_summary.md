# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.808 |                20.600 |              13.214 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.200 | 0.093 |               179.960 |               0.740 |         25 |              0.800 |              0.800 |          0.715 |          0.885 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.006 |               193.480 |              -1.524 |         25 |              0.960 |              0.960 |          0.802 |          0.993 |
| B_L2 (+ object appearance)                      |          0.080 | 0.033 |               189.960 |              -1.034 |         25 |              0.920 |              0.920 |          0.775 |          0.959 |
| B_L3 (+ distractors)                            |          0.120 | 0.031 |               184.240 |              -0.782 |         25 |              0.880 |              0.880 |          0.777 |          0.961 |

- **L1: success drop 0.800 absolute, 80.0% relative · SPL drop 0.715 absolute**
- **L2noT: success drop 0.960 absolute, 96.0% relative · SPL drop 0.802 absolute**
- **L2: success drop 0.920 absolute, 92.0% relative · SPL drop 0.775 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.777 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
