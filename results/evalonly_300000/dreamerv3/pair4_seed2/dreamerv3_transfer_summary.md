# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.594 |                24.920 |              13.905 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.412 |                49.840 |              11.989 |         25 |              0.120 |              0.120 |          0.182 |          0.307 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.409 |                57.800 |              11.366 |         25 |              0.160 |              0.160 |          0.185 |          0.312 |
| B_L2 (+ object appearance)                      |          0.960 | 0.578 |                38.880 |              12.845 |         25 |              0.040 |              0.040 |          0.016 |          0.026 |
| B_L3 (+ distractors)                            |          0.880 | 0.493 |                49.080 |              11.749 |         25 |              0.120 |              0.120 |          0.101 |          0.170 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.182 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.185 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.016 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.101 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
