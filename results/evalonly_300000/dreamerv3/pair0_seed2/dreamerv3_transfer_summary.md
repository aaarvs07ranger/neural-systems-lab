# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.772 |                14.640 |              11.566 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.743 |                17.680 |              11.526 |         25 |              0.000 |              0.000 |          0.029 |          0.038 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.736 |                19.720 |              11.482 |         25 |              0.000 |              0.000 |          0.036 |          0.046 |
| B_L2 (+ object appearance)                      |          1.000 | 0.626 |                35.600 |              11.321 |         25 |              0.000 |              0.000 |          0.145 |          0.188 |
| B_L3 (+ distractors)                            |          1.000 | 0.651 |                38.160 |              11.287 |         25 |              0.000 |              0.000 |          0.121 |          0.157 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.029 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.036 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.145 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.121 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
