# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.771 |                13.680 |              11.587 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.693 |                23.960 |              11.440 |         25 |              0.000 |              0.000 |          0.078 |          0.101 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.662 |                27.160 |              11.446 |         25 |              0.000 |              0.000 |          0.109 |          0.141 |
| B_L2 (+ object appearance)                      |          1.000 | 0.622 |                36.320 |              11.307 |         25 |              0.000 |              0.000 |          0.149 |          0.193 |
| B_L3 (+ distractors)                            |          0.960 | 0.595 |                46.120 |              10.727 |         25 |              0.040 |              0.040 |          0.176 |          0.228 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.078 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.109 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.149 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.176 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
