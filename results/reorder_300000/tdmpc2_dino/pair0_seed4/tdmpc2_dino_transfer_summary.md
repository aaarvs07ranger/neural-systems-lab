# TDMPC2_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                19.720 |              10.927 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.761 |                25.920 |              10.460 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| F_lightsky           |          1.000 | 0.813 |                17.520 |              11.525 |         25 |             -0.040 |             -0.042 |         -0.030 |         -0.039 |
| F_objall             |          0.960 | 0.771 |                20.000 |              10.931 |         25 |              0.000 |              0.000 |          0.012 |          0.015 |
| F_mat                |          0.960 | 0.778 |                23.920 |              11.030 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| R2                   |          0.960 | 0.792 |                18.880 |              11.077 |         25 |              0.000 |              0.000 |         -0.010 |         -0.012 |
| R3                   |          0.960 | 0.792 |                21.760 |              11.005 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| B_L3 (+ distractors) |          0.880 | 0.686 |                40.800 |               9.849 |         25 |              0.080 |              0.083 |          0.097 |          0.124 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.2% relative · SPL drop -0.030 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.010 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.097 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
