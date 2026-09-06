# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.527 |                83.200 |              10.304 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.172 |               168.560 |               1.101 |         25 |              0.560 |              0.667 |          0.355 |          0.674 |
| B_L2 (+ object appearance)  |          0.080 | 0.047 |               191.560 |              -1.460 |         25 |              0.760 |              0.905 |          0.480 |          0.910 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               186.040 |              -0.894 |         25 |              0.720 |              0.857 |          0.407 |          0.772 |

- **L1: success drop 0.560 absolute, 66.7% relative · SPL drop 0.355 absolute**
- **L2: success drop 0.760 absolute, 90.5% relative · SPL drop 0.480 absolute**
- **L3: success drop 0.720 absolute, 85.7% relative · SPL drop 0.407 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
