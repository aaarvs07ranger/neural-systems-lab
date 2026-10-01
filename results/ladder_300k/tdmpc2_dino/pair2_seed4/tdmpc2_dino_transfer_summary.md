# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.780 |                11.560 |              10.672 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.779 |                17.800 |              10.604 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.700 |                23.360 |               9.730 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| B_L2 (+ object appearance)                      |          1.000 | 0.779 |                12.160 |              10.667 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L3 (+ distractors)                            |          1.000 | 0.779 |                 8.040 |              10.693 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
