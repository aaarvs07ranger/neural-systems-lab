# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.701 |                16.560 |              10.292 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.635 |                27.600 |               9.810 |         25 |              0.040 |              0.042 |          0.066 |          0.095 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.555 |                53.560 |               8.126 |         25 |              0.160 |              0.167 |          0.147 |          0.209 |
| B_L2 (+ object appearance)                      |          0.800 | 0.555 |                54.160 |               8.106 |         25 |              0.160 |              0.167 |          0.146 |          0.209 |
| B_L3 (+ distractors)                            |          0.800 | 0.526 |                53.160 |               8.106 |         25 |              0.160 |              0.167 |          0.175 |          0.249 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.066 absolute**
- **L2noT: success drop 0.160 absolute, 16.7% relative · SPL drop 0.147 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.146 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.175 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
