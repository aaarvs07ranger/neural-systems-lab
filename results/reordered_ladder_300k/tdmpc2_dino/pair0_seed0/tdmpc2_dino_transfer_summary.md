# TDMPC2_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                18.200 |              10.976 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.783 |                18.160 |              10.975 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.960 | 0.789 |                18.280 |              10.963 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_objall             |          0.920 | 0.760 |                29.880 |              10.384 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| F_mat                |          0.920 | 0.750 |                28.000 |              10.432 |         25 |              0.040 |              0.042 |          0.033 |          0.042 |
| R2                   |          0.960 | 0.789 |                18.840 |              10.956 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| R3                   |          0.960 | 0.780 |                29.080 |              10.825 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L3 (+ distractors) |          0.920 | 0.749 |                30.640 |              10.542 |         25 |              0.040 |              0.042 |          0.033 |          0.042 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.033 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.033 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
