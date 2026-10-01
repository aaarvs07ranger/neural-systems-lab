# TDMPC2 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.716 |                31.200 |              12.056 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.715 |                29.320 |              12.094 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.657 |                48.680 |              10.755 |         25 |              0.080 |              0.083 |          0.058 |          0.082 |
| F_objall             |          0.880 | 0.660 |                53.640 |              10.617 |         25 |              0.080 |              0.083 |          0.056 |          0.078 |
| F_mat                |          0.000 | 0.000 |               200.000 |              -1.988 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |
| R2                   |          0.880 | 0.646 |                62.280 |              10.705 |         25 |              0.080 |              0.083 |          0.070 |          0.098 |
| R3                   |          0.840 | 0.608 |                64.800 |              10.053 |         25 |              0.120 |              0.125 |          0.108 |          0.150 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.555 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.058 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.056 absolute**
- **F_mat: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.070 absolute**
- **R3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.108 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
