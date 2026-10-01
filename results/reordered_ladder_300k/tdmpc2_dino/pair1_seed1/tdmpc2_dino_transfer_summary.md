# TDMPC2_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.718 |                 7.840 |              10.857 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.715 |                 8.680 |              10.872 |         25 |              0.000 |              0.000 |          0.003 |          0.005 |
| F_lightsky           |          1.000 | 0.718 |                 9.720 |              10.830 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          1.000 | 0.718 |                 9.800 |              10.877 |         25 |              0.000 |              0.000 |          0.000 |          0.001 |
| F_mat                |          0.960 | 0.682 |                20.120 |              10.279 |         25 |              0.040 |              0.040 |          0.036 |          0.050 |
| R2                   |          1.000 | 0.720 |                 8.360 |              10.846 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| R3                   |          1.000 | 0.718 |                 7.960 |              10.873 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L3 (+ distractors) |          0.960 | 0.686 |                24.600 |              10.290 |         25 |              0.040 |              0.040 |          0.033 |          0.045 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
