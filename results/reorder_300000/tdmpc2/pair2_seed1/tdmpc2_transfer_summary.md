# TDMPC2 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.739 |                16.560 |              10.212 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                16.320 |              10.633 |         25 |             -0.040 |             -0.042 |         -0.039 |         -0.052 |
| F_lightsky           |          0.840 | 0.619 |                46.520 |               8.665 |         25 |              0.120 |              0.125 |          0.120 |          0.162 |
| F_objall             |          1.000 | 0.775 |                14.760 |              10.641 |         25 |             -0.040 |             -0.042 |         -0.036 |         -0.049 |
| F_mat                |          0.960 | 0.729 |                31.080 |              10.044 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| R2                   |          0.880 | 0.653 |                39.680 |               9.154 |         25 |              0.080 |              0.083 |          0.085 |          0.115 |
| R3                   |          0.880 | 0.659 |                44.040 |               9.119 |         25 |              0.080 |              0.083 |          0.079 |          0.107 |
| B_L3 (+ distractors) |          0.880 | 0.685 |                47.520 |               9.004 |         25 |              0.080 |              0.083 |          0.054 |          0.073 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.039 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.5% relative · SPL drop 0.120 absolute**
- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.036 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.085 absolute**
- **R3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.079 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.054 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
