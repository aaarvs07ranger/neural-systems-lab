# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.726 |                38.560 |              11.977 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.157 |               175.320 |               0.980 |         25 |              0.720 |              0.750 |          0.568 |          0.783 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.071 |               187.080 |              -0.871 |         25 |              0.840 |              0.875 |          0.655 |          0.903 |
| B_L2 (+ object appearance)                      |          0.240 | 0.164 |               169.800 |               0.621 |         25 |              0.720 |              0.750 |          0.562 |          0.774 |
| B_L3 (+ distractors)                            |          0.200 | 0.156 |               177.240 |               0.230 |         25 |              0.760 |              0.792 |          0.569 |          0.784 |

- **L1: success drop 0.720 absolute, 75.0% relative · SPL drop 0.568 absolute**
- **L2noT: success drop 0.840 absolute, 87.5% relative · SPL drop 0.655 absolute**
- **L2: success drop 0.720 absolute, 75.0% relative · SPL drop 0.562 absolute**
- **L3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.569 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
