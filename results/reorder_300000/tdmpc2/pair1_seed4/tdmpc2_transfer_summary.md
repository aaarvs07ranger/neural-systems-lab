# TDMPC2 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.718 |                 9.320 |              10.845 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.686 |                24.800 |              10.643 |         25 |              0.000 |              0.000 |          0.032 |          0.044 |
| F_lightsky           |          1.000 | 0.721 |                10.760 |              10.827 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_objall             |          1.000 | 0.713 |                12.200 |              10.836 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_mat                |          0.640 | 0.487 |               102.840 |               5.774 |         25 |              0.360 |              0.360 |          0.231 |          0.322 |
| R2                   |          1.000 | 0.709 |                11.640 |              10.817 |         25 |              0.000 |              0.000 |          0.009 |          0.013 |
| R3                   |          1.000 | 0.701 |                23.160 |              10.728 |         25 |              0.000 |              0.000 |          0.017 |          0.024 |
| B_L3 (+ distractors) |          0.240 | 0.210 |               157.800 |               0.422 |         25 |              0.760 |              0.760 |          0.508 |          0.707 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.032 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_mat: success drop 0.360 absolute, 36.0% relative · SPL drop 0.231 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.017 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.508 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
