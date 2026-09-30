# DREAMERV3 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.796 |                13.320 |              11.600 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.804 |                11.880 |              11.595 |         25 |              0.000 |              0.000 |         -0.009 |         -0.011 |
| F_lightsky           |          0.960 | 0.662 |                30.680 |              10.894 |         25 |              0.040 |              0.040 |          0.134 |          0.169 |
| F_objall             |          1.000 | 0.818 |                12.200 |              11.571 |         25 |              0.000 |              0.000 |         -0.022 |         -0.027 |
| F_mat                |          1.000 | 0.762 |                23.400 |              11.475 |         25 |              0.000 |              0.000 |          0.034 |          0.042 |
| R2                   |          1.000 | 0.718 |                29.000 |              11.422 |         25 |              0.000 |              0.000 |          0.078 |          0.098 |
| R3                   |          0.880 | 0.575 |                67.800 |               9.582 |         25 |              0.120 |              0.120 |          0.221 |          0.277 |
| B_L3 (+ distractors) |          1.000 | 0.618 |                45.960 |              11.211 |         25 |              0.000 |              0.000 |          0.178 |          0.224 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.134 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.034 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.078 absolute**
- **R3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.221 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.178 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
