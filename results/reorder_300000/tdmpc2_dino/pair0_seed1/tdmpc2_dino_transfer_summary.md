# TDMPC2_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.789 |                18.800 |              10.962 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.782 |                18.120 |              10.960 |         25 |              0.000 |              0.000 |          0.007 |          0.008 |
| F_lightsky           |          0.880 | 0.722 |                34.120 |               9.875 |         25 |              0.080 |              0.083 |          0.066 |          0.084 |
| F_objall             |          0.880 | 0.697 |                34.960 |               9.960 |         25 |              0.080 |              0.083 |          0.092 |          0.116 |
| F_mat                |          0.920 | 0.759 |                29.080 |              10.432 |         25 |              0.040 |              0.042 |          0.029 |          0.037 |
| R2                   |          0.920 | 0.758 |                25.960 |              10.469 |         25 |              0.040 |              0.042 |          0.031 |          0.039 |
| R3                   |          0.880 | 0.690 |                36.800 |               9.964 |         25 |              0.080 |              0.083 |          0.098 |          0.125 |
| B_L3 (+ distractors) |          0.920 | 0.736 |                29.880 |              10.407 |         25 |              0.040 |              0.042 |          0.053 |          0.067 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.066 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.092 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.029 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **R3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.098 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.053 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
