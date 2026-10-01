# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.665 |                36.520 |              10.507 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.561 |                74.080 |               9.704 |         25 |              0.040 |              0.043 |          0.105 |          0.157 |
| B_L2 (+ object appearance)  |          0.440 | 0.297 |               126.720 |               4.451 |         25 |              0.480 |              0.522 |          0.369 |          0.554 |
| B_L3 (+ distractors)        |          0.440 | 0.327 |               129.160 |               4.470 |         25 |              0.480 |              0.522 |          0.339 |          0.509 |

- **L1: success drop 0.040 absolute, 4.3% relative · SPL drop 0.105 absolute**
- **L2: success drop 0.480 absolute, 52.2% relative · SPL drop 0.369 absolute**
- **L3: success drop 0.480 absolute, 52.2% relative · SPL drop 0.339 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
