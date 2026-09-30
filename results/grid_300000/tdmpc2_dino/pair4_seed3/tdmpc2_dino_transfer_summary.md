# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.778 |                26.960 |              12.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.644 |                48.080 |              10.745 |         25 |              0.120 |              0.125 |          0.134 |          0.172 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.577 |                57.840 |              10.209 |         25 |              0.160 |              0.167 |          0.202 |          0.259 |
| B_L2 (+ object appearance)                      |          0.880 | 0.679 |                49.280 |              11.224 |         25 |              0.080 |              0.083 |          0.099 |          0.127 |
| B_L3 (+ distractors)                            |          0.920 | 0.708 |                38.200 |              11.922 |         25 |              0.040 |              0.042 |          0.070 |          0.090 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.134 absolute**
- **L2noT: success drop 0.160 absolute, 16.7% relative · SPL drop 0.202 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.099 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.070 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
