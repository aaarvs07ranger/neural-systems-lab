# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.774 |                12.280 |              10.654 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.565 |                64.360 |               8.089 |         25 |              0.200 |              0.200 |          0.209 |          0.270 |
| B_L2 (+ object appearance)  |          0.840 | 0.646 |                70.800 |               8.445 |         25 |              0.160 |              0.160 |          0.128 |          0.166 |
| B_L3 (+ distractors)        |          0.880 | 0.648 |                60.880 |               8.918 |         25 |              0.120 |              0.120 |          0.127 |          0.163 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.209 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.128 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.127 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
