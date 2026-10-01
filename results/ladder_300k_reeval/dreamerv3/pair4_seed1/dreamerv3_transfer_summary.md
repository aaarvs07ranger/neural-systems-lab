# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.597 |                24.320 |              13.926 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.556 |                29.120 |              13.863 |         25 |              0.000 |              0.000 |          0.041 |          0.069 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.474 |                49.960 |              12.023 |         25 |              0.120 |              0.120 |          0.123 |          0.206 |
| B_L2 (+ object appearance)                      |          0.960 | 0.591 |                34.760 |              12.965 |         25 |              0.040 |              0.040 |          0.006 |          0.010 |
| B_L3 (+ distractors)                            |          0.960 | 0.614 |                36.240 |              13.103 |         25 |              0.040 |              0.040 |         -0.016 |         -0.027 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.041 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.123 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.006 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.016 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
