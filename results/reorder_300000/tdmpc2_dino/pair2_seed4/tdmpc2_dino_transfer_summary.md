# TDMPC2_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.780 |                11.560 |              10.672 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 9.680 |              10.711 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_lightsky           |          1.000 | 0.779 |                 9.840 |              10.712 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_objall             |          1.000 | 0.780 |                 8.160 |              10.706 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          1.000 | 0.779 |                10.320 |              10.676 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R2                   |          1.000 | 0.779 |                12.720 |              10.679 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R3                   |          1.000 | 0.779 |                11.320 |              10.677 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L3 (+ distractors) |          1.000 | 0.779 |                10.960 |              10.673 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
