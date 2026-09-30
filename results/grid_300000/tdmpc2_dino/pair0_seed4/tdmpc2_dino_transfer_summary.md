# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                18.720 |              10.940 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.749 |                28.840 |              10.543 |         25 |              0.040 |              0.042 |          0.034 |          0.043 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.711 |                42.440 |               9.900 |         25 |              0.080 |              0.083 |          0.071 |          0.091 |
| B_L2 (+ object appearance)                      |          0.880 | 0.699 |                44.720 |               9.821 |         25 |              0.080 |              0.083 |          0.083 |          0.107 |
| B_L3 (+ distractors)                            |          0.840 | 0.674 |                45.600 |               9.306 |         25 |              0.120 |              0.125 |          0.109 |          0.139 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.034 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.071 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.083 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.109 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
