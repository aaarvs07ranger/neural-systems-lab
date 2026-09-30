# TDMPC2 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.738 |                17.800 |              10.202 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 9.320 |              10.684 |         25 |             -0.040 |             -0.042 |         -0.042 |         -0.056 |
| F_lightsky           |          0.880 | 0.658 |                36.080 |               9.212 |         25 |              0.080 |              0.083 |          0.080 |          0.108 |
| F_objall             |          1.000 | 0.778 |                 8.080 |              10.704 |         25 |             -0.040 |             -0.042 |         -0.040 |         -0.054 |
| F_mat                |          0.960 | 0.736 |                25.920 |              10.127 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| R2                   |          0.960 | 0.738 |                23.160 |              10.163 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| R3                   |          0.880 | 0.655 |                40.160 |               9.155 |         25 |              0.080 |              0.083 |          0.083 |          0.113 |
| B_L3 (+ distractors) |          0.920 | 0.698 |                41.600 |               9.460 |         25 |              0.040 |              0.042 |          0.039 |          0.053 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.042 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.080 absolute**
- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.040 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **R3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.083 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.039 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
