# TDMPC2 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.780 |                16.960 |              10.625 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.778 |                13.040 |              10.654 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| F_lightsky           |          0.800 | 0.574 |                63.760 |               8.080 |         25 |              0.200 |              0.200 |          0.206 |          0.264 |
| F_objall             |          1.000 | 0.778 |                22.960 |              10.551 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_mat                |          0.960 | 0.737 |                42.360 |               9.975 |         25 |              0.040 |              0.040 |          0.043 |          0.055 |
| R2                   |          0.800 | 0.572 |                63.960 |               8.118 |         25 |              0.200 |              0.200 |          0.208 |          0.267 |
| R3                   |          0.840 | 0.612 |                49.920 |               8.634 |         25 |              0.160 |              0.160 |          0.168 |          0.215 |
| B_L3 (+ distractors) |          0.840 | 0.603 |                81.040 |               8.279 |         25 |              0.160 |              0.160 |          0.177 |          0.227 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_lightsky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.206 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **R2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.208 absolute**
- **R3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.168 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.177 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
