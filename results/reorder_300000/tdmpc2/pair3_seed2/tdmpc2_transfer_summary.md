# TDMPC2 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.715 |                32.520 |              12.063 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.680 |                39.560 |              11.584 |         25 |              0.040 |              0.042 |          0.035 |          0.049 |
| F_lightsky           |          0.960 | 0.704 |                48.400 |              11.745 |         25 |              0.000 |              0.000 |          0.011 |          0.015 |
| F_objall             |          0.880 | 0.672 |                53.640 |              10.636 |         25 |              0.080 |              0.083 |          0.043 |          0.060 |
| F_mat                |          0.160 | 0.128 |               182.640 |               0.024 |         25 |              0.800 |              0.833 |          0.587 |          0.821 |
| R2                   |          0.840 | 0.627 |                61.880 |              10.212 |         25 |              0.120 |              0.125 |          0.089 |          0.124 |
| R3                   |          1.000 | 0.721 |                57.440 |              12.196 |         25 |             -0.040 |             -0.042 |         -0.006 |         -0.008 |
| B_L3 (+ distractors) |          0.200 | 0.148 |               180.320 |               0.147 |         25 |              0.760 |              0.792 |          0.567 |          0.792 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.035 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.043 absolute**
- **F_mat: success drop 0.800 absolute, 83.3% relative · SPL drop 0.587 absolute**
- **R2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.089 absolute**
- **R3: success drop -0.040 absolute, -4.2% relative · SPL drop -0.006 absolute**
- **L3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.567 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
