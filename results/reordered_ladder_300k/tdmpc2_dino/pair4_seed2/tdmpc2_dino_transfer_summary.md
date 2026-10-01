# TDMPC2_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.792 |                18.480 |              13.250 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.789 |                18.880 |              13.255 |         25 |              0.000 |              0.000 |          0.004 |          0.004 |
| F_lightsky           |          0.920 | 0.736 |                32.520 |              12.057 |         25 |              0.080 |              0.080 |          0.056 |          0.071 |
| F_objall             |          0.960 | 0.741 |                28.880 |              12.617 |         25 |              0.040 |              0.040 |          0.051 |          0.064 |
| F_mat                |          0.920 | 0.661 |                41.280 |              12.015 |         25 |              0.080 |              0.080 |          0.131 |          0.166 |
| R2                   |          0.840 | 0.644 |                46.040 |              10.984 |         25 |              0.160 |              0.160 |          0.149 |          0.187 |
| R3                   |          0.920 | 0.697 |                32.800 |              12.089 |         25 |              0.080 |              0.080 |          0.095 |          0.120 |
| B_L3 (+ distractors) |          0.680 | 0.466 |                82.640 |               8.640 |         25 |              0.320 |              0.320 |          0.327 |          0.412 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.056 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.051 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.131 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.149 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.095 absolute**
- **L3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.327 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
