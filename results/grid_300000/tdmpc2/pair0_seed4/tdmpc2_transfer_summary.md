# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.789 |                18.880 |              10.954 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.619 |                55.200 |               9.652 |         25 |              0.080 |              0.083 |          0.170 |          0.215 |
| B_L2 (+ object appearance)  |          0.520 | 0.373 |               116.640 |               4.878 |         25 |              0.440 |              0.458 |          0.416 |          0.528 |
| B_L3 (+ distractors)        |          0.600 | 0.389 |               124.600 |               5.832 |         25 |              0.360 |              0.375 |          0.399 |          0.506 |

- **L1: success drop 0.080 absolute, 8.3% relative · SPL drop 0.170 absolute**
- **L2: success drop 0.440 absolute, 45.8% relative · SPL drop 0.416 absolute**
- **L3: success drop 0.360 absolute, 37.5% relative · SPL drop 0.399 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
