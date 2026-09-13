# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.623 |                62.280 |              10.500 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.040 |               192.120 |              -2.041 |         25 |              0.800 |              0.952 |          0.583 |          0.936 |
| B_L2 (+ object appearance)  |          0.040 | 0.010 |               194.200 |              -1.955 |         25 |              0.800 |              0.952 |          0.613 |          0.984 |
| B_L3 (+ distractors)        |          0.120 | 0.089 |               180.080 |              -0.902 |         25 |              0.720 |              0.857 |          0.535 |          0.857 |

- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.583 absolute**
- **L2: success drop 0.800 absolute, 95.2% relative · SPL drop 0.613 absolute**
- **L3: success drop 0.720 absolute, 85.7% relative · SPL drop 0.535 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
