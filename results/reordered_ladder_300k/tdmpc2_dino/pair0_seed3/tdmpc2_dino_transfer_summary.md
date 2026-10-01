# TDMPC2_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                18.480 |              10.978 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.786 |                18.800 |              10.958 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_lightsky           |          0.960 | 0.777 |                18.640 |              10.977 |         25 |              0.000 |              0.000 |          0.006 |          0.007 |
| F_objall             |          0.960 | 0.779 |                19.720 |              10.932 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_mat                |          0.960 | 0.767 |                19.400 |              10.954 |         25 |              0.000 |              0.000 |          0.015 |          0.019 |
| R2                   |          0.960 | 0.785 |                18.080 |              10.976 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| R3                   |          0.960 | 0.776 |                24.160 |              10.894 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| B_L3 (+ distractors) |          0.960 | 0.748 |                29.160 |              10.844 |         25 |              0.000 |              0.000 |          0.035 |          0.045 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.035 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
