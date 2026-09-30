# TDMPC2 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.766 |                25.640 |              13.171 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.754 |                26.760 |              12.546 |         25 |              0.040 |              0.040 |          0.012 |          0.016 |
| F_lightsky           |          0.880 | 0.669 |                49.400 |              11.300 |         25 |              0.120 |              0.120 |          0.096 |          0.126 |
| F_objall             |          0.920 | 0.659 |                54.520 |              11.599 |         25 |              0.080 |              0.080 |          0.107 |          0.140 |
| F_mat                |          0.800 | 0.523 |                71.880 |              10.090 |         25 |              0.200 |              0.200 |          0.242 |          0.316 |
| R2                   |          0.800 | 0.594 |                63.960 |              10.324 |         25 |              0.200 |              0.200 |          0.172 |          0.225 |
| R3                   |          0.680 | 0.435 |                96.520 |               7.984 |         25 |              0.320 |              0.320 |          0.331 |          0.432 |
| B_L3 (+ distractors) |          0.520 | 0.177 |               144.280 |               5.582 |         25 |              0.480 |              0.480 |          0.589 |          0.769 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.012 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.096 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.107 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.242 absolute**
- **R2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.172 absolute**
- **R3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.331 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.589 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
