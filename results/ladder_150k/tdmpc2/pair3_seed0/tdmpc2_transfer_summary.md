# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.684 |                40.400 |              11.436 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.200 | 0.144 |               171.200 |               0.371 |         25 |              0.720 |              0.783 |          0.540 |          0.789 |
| B_L2 (+ object appearance)  |          0.200 | 0.141 |               177.040 |               0.715 |         25 |              0.720 |              0.783 |          0.543 |          0.794 |
| B_L3 (+ distractors)        |          0.160 | 0.146 |               178.400 |               0.259 |         25 |              0.760 |              0.826 |          0.539 |          0.787 |

- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.540 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **L3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.539 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
