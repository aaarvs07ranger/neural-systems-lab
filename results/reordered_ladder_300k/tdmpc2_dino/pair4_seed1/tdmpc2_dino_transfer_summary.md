# TDMPC2_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.774 |                19.800 |              13.229 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.774 |                18.760 |              13.242 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          1.000 | 0.792 |                20.120 |              13.225 |         25 |              0.000 |              0.000 |         -0.017 |         -0.022 |
| F_objall             |          0.960 | 0.753 |                25.640 |              12.603 |         25 |              0.040 |              0.040 |          0.021 |          0.027 |
| F_mat                |          0.760 | 0.557 |                72.040 |               9.719 |         25 |              0.240 |              0.240 |          0.218 |          0.281 |
| R2                   |          0.920 | 0.722 |                32.800 |              12.033 |         25 |              0.080 |              0.080 |          0.053 |          0.068 |
| R3                   |          0.920 | 0.738 |                33.600 |              12.009 |         25 |              0.080 |              0.080 |          0.036 |          0.046 |
| B_L3 (+ distractors) |          0.880 | 0.601 |                56.560 |              11.270 |         25 |              0.120 |              0.120 |          0.174 |          0.224 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.017 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.021 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.218 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.053 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.036 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.174 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
