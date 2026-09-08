# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.640 | 0.401 |                91.760 |               6.451 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.440 | 0.356 |               127.000 |               3.521 |         25 |              0.200 |              0.312 |          0.046 |          0.114 |
| B_L2 (+ object appearance)  |          0.400 | 0.300 |               143.680 |               3.001 |         25 |              0.240 |              0.375 |          0.101 |          0.252 |
| B_L3 (+ distractors)        |          0.600 | 0.407 |               108.080 |               5.593 |         25 |              0.040 |              0.063 |         -0.006 |         -0.014 |

- **L1: success drop 0.200 absolute, 31.2% relative · SPL drop 0.046 absolute**
- **L2: success drop 0.240 absolute, 37.5% relative · SPL drop 0.101 absolute**
- **L3: success drop 0.040 absolute, 6.3% relative · SPL drop -0.006 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
