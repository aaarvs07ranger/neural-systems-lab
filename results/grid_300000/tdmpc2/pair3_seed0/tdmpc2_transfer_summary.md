# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.717 |                31.280 |              12.050 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.120 | 0.078 |               185.480 |              -0.751 |         25 |              0.840 |              0.875 |          0.639 |          0.891 |
| B_L2 (+ object appearance)  |          0.120 | 0.072 |               184.000 |              -0.941 |         25 |              0.840 |              0.875 |          0.645 |          0.899 |
| B_L3 (+ distractors)        |          0.160 | 0.115 |               179.960 |              -0.456 |         25 |              0.800 |              0.833 |          0.602 |          0.840 |

- **L1: success drop 0.840 absolute, 87.5% relative · SPL drop 0.639 absolute**
- **L2: success drop 0.840 absolute, 87.5% relative · SPL drop 0.645 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.602 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
