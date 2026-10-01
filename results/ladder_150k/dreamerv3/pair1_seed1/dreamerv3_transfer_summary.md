# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.360 | 0.239 |               140.080 |               3.034 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.320 | 0.250 |               147.800 |               1.473 |         25 |              0.040 |              0.111 |         -0.011 |         -0.047 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               161.000 |              -0.100 |         25 |              0.160 |              0.444 |          0.039 |          0.164 |
| B_L3 (+ distractors)        |          0.440 | 0.318 |               124.720 |               3.452 |         25 |             -0.080 |             -0.222 |         -0.078 |         -0.328 |

- **L1: success drop 0.040 absolute, 11.1% relative · SPL drop -0.011 absolute**
- **L2: success drop 0.160 absolute, 44.4% relative · SPL drop 0.039 absolute**
- **L3: success drop -0.080 absolute, -22.2% relative · SPL drop -0.078 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
