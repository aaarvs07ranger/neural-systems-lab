# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.000 | 0.000 |               200.000 |               0.479 |         25 |              0.000 |                nan |          0.000 |            nan |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.284 |         25 |              0.000 |                nan |          0.000 |            nan |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -1.937 |         25 |             -0.040 |                nan |         -0.040 |            nan |
| B_L2 (+ object appearance)                      |          0.080 | 0.080 |               189.200 |              -1.019 |         25 |             -0.080 |                nan |         -0.080 |            nan |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.017 |         25 |              0.000 |                nan |          0.000 |            nan |

- **L1: success drop 0.000 absolute · SPL drop 0.000 absolute**
- **L2noT: success drop -0.040 absolute · SPL drop -0.040 absolute**
- **L2: success drop -0.080 absolute · SPL drop -0.080 absolute**
- **L3: success drop 0.000 absolute · SPL drop 0.000 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
