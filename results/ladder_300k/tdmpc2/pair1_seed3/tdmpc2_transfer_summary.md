# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.716 |                 8.160 |              10.858 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.328 |               148.680 |               1.991 |         25 |              0.640 |              0.640 |          0.388 |          0.542 |
| B_L2 (+ object appearance)  |          0.320 | 0.320 |               142.800 |               1.384 |         25 |              0.680 |              0.680 |          0.396 |          0.553 |
| B_L3 (+ distractors)        |          0.480 | 0.414 |               122.040 |               3.745 |         25 |              0.520 |              0.520 |          0.302 |          0.422 |

- **L1: success drop 0.640 absolute, 64.0% relative · SPL drop 0.388 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.396 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.302 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
