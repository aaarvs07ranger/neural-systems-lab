# DREAMERV3 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.752 |                12.720 |              10.915 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.752 |                13.120 |              10.919 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.768 |                12.800 |              10.927 |         25 |              0.000 |              0.000 |         -0.016 |         -0.022 |
| F_objall             |          1.000 | 0.770 |                13.360 |              10.879 |         25 |              0.000 |              0.000 |         -0.018 |         -0.024 |
| F_mat                |          1.000 | 0.770 |                17.200 |              10.828 |         25 |              0.000 |              0.000 |         -0.019 |         -0.025 |
| R2                   |          1.000 | 0.768 |                12.360 |              10.923 |         25 |              0.000 |              0.000 |         -0.016 |         -0.021 |
| R3                   |          1.000 | 0.769 |                17.640 |              10.847 |         25 |              0.000 |              0.000 |         -0.018 |         -0.023 |
| B_L3 (+ distractors) |          0.960 | 0.748 |                58.040 |               9.892 |         25 |              0.040 |              0.040 |          0.004 |          0.005 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.018 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.019 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.018 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.004 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
