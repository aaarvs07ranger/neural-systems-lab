# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.753 |                33.080 |              12.467 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.160 | 0.111 |               178.680 |              -0.280 |         25 |              0.840 |              0.840 |          0.642 |          0.852 |
| B_L2 (+ object appearance)  |          0.160 | 0.127 |               178.440 |               0.186 |         25 |              0.840 |              0.840 |          0.626 |          0.831 |
| B_L3 (+ distractors)        |          0.160 | 0.111 |               182.440 |               0.071 |         25 |              0.840 |              0.840 |          0.642 |          0.852 |

- **L1: success drop 0.840 absolute, 84.0% relative · SPL drop 0.642 absolute**
- **L2: success drop 0.840 absolute, 84.0% relative · SPL drop 0.626 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.642 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
