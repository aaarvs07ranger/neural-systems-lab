# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.764 |                21.280 |              12.573 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.120 | 0.064 |               187.800 |              -0.760 |         25 |              0.880 |              0.880 |          0.700 |          0.916 |
| B_L2 (+ object appearance)  |          0.280 | 0.200 |               172.960 |               0.958 |         25 |              0.720 |              0.720 |          0.564 |          0.738 |
| B_L3 (+ distractors)        |          0.160 | 0.103 |               185.880 |              -0.265 |         25 |              0.840 |              0.840 |          0.661 |          0.865 |

- **L1: success drop 0.880 absolute, 88.0% relative · SPL drop 0.700 absolute**
- **L2: success drop 0.720 absolute, 72.0% relative · SPL drop 0.564 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.661 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
