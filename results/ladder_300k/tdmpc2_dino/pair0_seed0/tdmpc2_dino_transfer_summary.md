# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.789 |                18.320 |              10.958 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.776 |                22.440 |              11.052 |         25 |              0.000 |              0.000 |          0.013 |          0.016 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.727 |                35.600 |               9.868 |         25 |              0.080 |              0.083 |          0.062 |          0.079 |
| B_L2 (+ object appearance)                      |          0.880 | 0.702 |                37.800 |               9.944 |         25 |              0.080 |              0.083 |          0.087 |          0.110 |
| B_L3 (+ distractors)                            |          0.920 | 0.753 |                32.200 |              10.379 |         25 |              0.040 |              0.042 |          0.037 |          0.046 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.062 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.087 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.037 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
