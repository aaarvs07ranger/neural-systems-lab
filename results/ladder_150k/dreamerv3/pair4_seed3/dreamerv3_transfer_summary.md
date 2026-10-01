# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.000 | 0.000 |               200.000 |               2.007 |         25 |              0.000 |                nan |          0.000 |            nan |
| B_L1 (materials + lighting) |          0.200 | 0.096 |               185.280 |               4.285 |         25 |             -0.200 |                nan |         -0.096 |            nan |
| B_L2 (+ object appearance)  |          0.480 | 0.329 |               136.120 |               7.237 |         25 |             -0.480 |                nan |         -0.329 |            nan |
| B_L3 (+ distractors)        |          0.280 | 0.177 |               158.000 |               5.000 |         25 |             -0.280 |                nan |         -0.177 |            nan |

- **L1: success drop -0.200 absolute · SPL drop -0.096 absolute**
- **L2: success drop -0.480 absolute · SPL drop -0.329 absolute**
- **L3: success drop -0.280 absolute · SPL drop -0.177 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
