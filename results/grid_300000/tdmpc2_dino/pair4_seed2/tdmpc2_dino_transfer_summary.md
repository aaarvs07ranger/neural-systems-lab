# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.758 |                18.720 |              13.268 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.627 |                45.880 |              11.373 |         25 |              0.120 |              0.120 |          0.131 |          0.173 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.605 |                66.560 |              10.754 |         25 |              0.160 |              0.160 |          0.153 |          0.202 |
| B_L2 (+ object appearance)                      |          0.840 | 0.549 |                66.800 |              10.785 |         25 |              0.160 |              0.160 |          0.209 |          0.275 |
| B_L3 (+ distractors)                            |          0.800 | 0.580 |                58.720 |              10.447 |         25 |              0.200 |              0.200 |          0.178 |          0.235 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.131 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.153 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.209 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.178 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
