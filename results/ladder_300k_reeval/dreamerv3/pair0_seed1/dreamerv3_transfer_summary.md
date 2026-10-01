# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.806 |                12.560 |              11.594 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.769 |                22.040 |              11.467 |         25 |              0.000 |              0.000 |          0.037 |          0.046 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.699 |                34.160 |              11.365 |         25 |              0.000 |              0.000 |          0.107 |          0.133 |
| B_L2 (+ object appearance)                      |          1.000 | 0.598 |                57.800 |              11.106 |         25 |              0.000 |              0.000 |          0.208 |          0.259 |
| B_L3 (+ distractors)                            |          1.000 | 0.627 |                58.440 |              11.097 |         25 |              0.000 |              0.000 |          0.179 |          0.222 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.037 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.107 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.208 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.179 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
