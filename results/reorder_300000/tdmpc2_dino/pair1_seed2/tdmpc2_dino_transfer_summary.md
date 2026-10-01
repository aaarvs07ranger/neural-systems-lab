# TDMPC2_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.701 |                15.400 |              10.307 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.714 |                 8.720 |              10.861 |         25 |             -0.040 |             -0.042 |         -0.012 |         -0.018 |
| F_lightsky           |          0.960 | 0.701 |                15.040 |              10.295 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_objall             |          0.960 | 0.700 |                17.160 |              10.312 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_mat                |          0.920 | 0.642 |                29.320 |               9.808 |         25 |              0.040 |              0.042 |          0.059 |          0.085 |
| R2                   |          1.000 | 0.716 |                 8.920 |              10.862 |         25 |             -0.040 |             -0.042 |         -0.014 |         -0.020 |
| R3                   |          1.000 | 0.718 |                10.480 |              10.851 |         25 |             -0.040 |             -0.042 |         -0.016 |         -0.024 |
| B_L3 (+ distractors) |          0.680 | 0.492 |                77.640 |               6.653 |         25 |              0.280 |              0.292 |          0.210 |          0.299 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.012 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.059 absolute**
- **R2: success drop -0.040 absolute, -4.2% relative · SPL drop -0.014 absolute**
- **R3: success drop -0.040 absolute, -4.2% relative · SPL drop -0.016 absolute**
- **L3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.210 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
