# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.600 | 0.426 |                92.200 |               6.044 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.440 | 0.255 |               139.480 |               4.040 |         25 |              0.160 |              0.267 |          0.171 |          0.402 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.400 | 0.213 |               149.360 |               3.402 |         25 |              0.200 |              0.333 |          0.212 |          0.499 |
| B_L2 (+ object appearance)                      |          0.520 | 0.296 |               134.480 |               4.897 |         25 |              0.080 |              0.133 |          0.130 |          0.304 |
| B_L3 (+ distractors)                            |          0.440 | 0.233 |               133.560 |               3.973 |         25 |              0.160 |              0.267 |          0.192 |          0.452 |

- **L1: success drop 0.160 absolute, 26.7% relative · SPL drop 0.171 absolute**
- **L2noT: success drop 0.200 absolute, 33.3% relative · SPL drop 0.212 absolute**
- **L2: success drop 0.080 absolute, 13.3% relative · SPL drop 0.130 absolute**
- **L3: success drop 0.160 absolute, 26.7% relative · SPL drop 0.192 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
