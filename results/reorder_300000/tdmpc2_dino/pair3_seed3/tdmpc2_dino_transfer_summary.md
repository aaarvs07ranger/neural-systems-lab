# TDMPC2_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.762 |                20.200 |              12.594 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.761 |                20.480 |              12.587 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          0.960 | 0.740 |                29.480 |              11.997 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| F_objall             |          0.880 | 0.668 |                46.320 |              10.866 |         25 |              0.120 |              0.120 |          0.095 |          0.124 |
| F_mat                |          0.880 | 0.592 |                68.280 |              10.722 |         25 |              0.120 |              0.120 |          0.170 |          0.223 |
| R2                   |          1.000 | 0.763 |                20.720 |              12.584 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| R3                   |          0.920 | 0.707 |                38.880 |              11.280 |         25 |              0.080 |              0.080 |          0.055 |          0.072 |
| B_L3 (+ distractors) |          0.720 | 0.521 |                91.680 |               8.588 |         25 |              0.280 |              0.280 |          0.242 |          0.317 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.095 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.170 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.055 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.242 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
