# TDMPC2_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.780 |                15.640 |              10.637 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.739 |                16.400 |              10.215 |         25 |              0.040 |              0.040 |          0.042 |          0.053 |
| F_lightsky           |          1.000 | 0.780 |                10.320 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          1.000 | 0.780 |                 9.120 |              10.680 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          1.000 | 0.779 |                10.680 |              10.665 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R2                   |          1.000 | 0.779 |                12.520 |              10.662 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R3                   |          1.000 | 0.779 |                11.800 |              10.664 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L3 (+ distractors) |          1.000 | 0.778 |                12.840 |              10.662 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
