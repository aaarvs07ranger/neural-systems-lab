# TDMPC2_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.806 |                21.200 |              13.216 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.805 |                19.800 |              13.229 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          0.960 | 0.778 |                26.640 |              12.590 |         25 |              0.040 |              0.040 |          0.028 |          0.034 |
| F_objall             |          0.920 | 0.717 |                32.600 |              11.999 |         25 |              0.080 |              0.080 |          0.089 |          0.111 |
| F_mat                |          0.880 | 0.649 |                42.240 |              11.357 |         25 |              0.120 |              0.120 |          0.157 |          0.195 |
| R2                   |          1.000 | 0.810 |                20.920 |              13.216 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| R3                   |          0.960 | 0.769 |                26.920 |              12.487 |         25 |              0.040 |              0.040 |          0.037 |          0.046 |
| B_L3 (+ distractors) |          0.840 | 0.667 |                52.480 |              10.635 |         25 |              0.160 |              0.160 |          0.139 |          0.172 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.028 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.089 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.157 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.037 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.139 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
