# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.763 |                19.040 |              13.274 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.651 |                55.320 |              11.331 |         25 |              0.120 |              0.120 |          0.113 |          0.148 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.626 |                52.320 |              11.340 |         25 |              0.120 |              0.120 |          0.138 |          0.180 |
| B_L2 (+ object appearance)                      |          0.920 | 0.627 |                56.680 |              11.847 |         25 |              0.080 |              0.080 |          0.136 |          0.179 |
| B_L3 (+ distractors)                            |          0.800 | 0.562 |                62.400 |              10.298 |         25 |              0.200 |              0.200 |          0.201 |          0.263 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.113 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.138 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.136 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.201 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
