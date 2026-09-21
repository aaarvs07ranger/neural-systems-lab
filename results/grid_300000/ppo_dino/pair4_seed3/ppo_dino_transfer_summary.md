# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.769 |                25.680 |              12.609 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.715 |                33.400 |              12.063 |         25 |              0.040 |              0.042 |          0.054 |          0.070 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.666 |                47.160 |              10.737 |         25 |              0.120 |              0.125 |          0.103 |          0.134 |
| B_L2 (+ object appearance)                      |          0.840 | 0.666 |                47.080 |              10.734 |         25 |              0.120 |              0.125 |          0.103 |          0.134 |
| B_L3 (+ distractors)                            |          0.760 | 0.603 |                60.920 |               9.703 |         25 |              0.200 |              0.208 |          0.166 |          0.216 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.054 absolute**
- **L2noT: success drop 0.120 absolute, 12.5% relative · SPL drop 0.103 absolute**
- **L2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.103 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.166 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
