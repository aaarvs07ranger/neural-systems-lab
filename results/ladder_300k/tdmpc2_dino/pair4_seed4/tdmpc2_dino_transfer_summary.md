# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.735 |                33.480 |              11.982 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.674 |                42.920 |              11.594 |         25 |              0.040 |              0.043 |          0.061 |          0.084 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.656 |                37.240 |              12.098 |         25 |              0.000 |              0.000 |          0.079 |          0.108 |
| B_L2 (+ object appearance)                      |          0.880 | 0.617 |                48.680 |              11.472 |         25 |              0.040 |              0.043 |          0.118 |          0.160 |
| B_L3 (+ distractors)                            |          0.880 | 0.628 |                45.760 |              11.615 |         25 |              0.040 |              0.043 |          0.107 |          0.146 |

- **L1: success drop 0.040 absolute, 4.3% relative · SPL drop 0.061 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.079 absolute**
- **L2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.118 absolute**
- **L3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.107 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
