# DREAMERV3 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.752 |                13.360 |              10.967 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.752 |                14.200 |              10.957 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.728 |                23.600 |              10.416 |         25 |              0.040 |              0.040 |          0.025 |          0.033 |
| F_objall             |          1.000 | 0.769 |                12.960 |              10.912 |         25 |              0.000 |              0.000 |         -0.017 |         -0.022 |
| F_mat                |          0.880 | 0.674 |                63.720 |               9.063 |         25 |              0.120 |              0.120 |          0.079 |          0.104 |
| R2                   |          0.920 | 0.688 |                28.280 |               9.945 |         25 |              0.080 |              0.080 |          0.065 |          0.086 |
| R3                   |          0.960 | 0.729 |                28.600 |              10.331 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| B_L3 (+ distractors) |          0.760 | 0.562 |                72.480 |               7.603 |         25 |              0.240 |              0.240 |          0.191 |          0.253 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.017 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.079 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.065 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **L3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.191 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
