# TDMPC2_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.778 |                11.440 |              10.660 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.780 |                14.320 |              10.630 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_lightsky           |          1.000 | 0.777 |                13.160 |              10.663 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_objall             |          1.000 | 0.778 |                11.360 |              10.669 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                |          1.000 | 0.778 |                10.360 |              10.695 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| R2                   |          0.960 | 0.736 |                22.960 |              10.156 |         25 |              0.040 |              0.040 |          0.042 |          0.054 |
| R3                   |          1.000 | 0.778 |                14.600 |              10.639 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| B_L3 (+ distractors) |          1.000 | 0.778 |                14.440 |              10.638 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
