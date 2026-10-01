# DREAMERV3 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.600 | 0.461 |                89.280 |               5.830 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.680 | 0.470 |                77.240 |               6.761 |         25 |             -0.080 |             -0.133 |         -0.009 |         -0.020 |
| F_lightsky           |          0.880 | 0.668 |                45.360 |               9.123 |         25 |             -0.280 |             -0.467 |         -0.207 |         -0.450 |
| F_objall             |          0.600 | 0.426 |                89.600 |               5.807 |         25 |              0.000 |              0.000 |          0.035 |          0.075 |
| F_mat                |          0.920 | 0.750 |                36.280 |               9.634 |         25 |             -0.320 |             -0.533 |         -0.289 |         -0.628 |
| R2                   |          0.920 | 0.673 |                32.760 |               9.629 |         25 |             -0.320 |             -0.533 |         -0.212 |         -0.460 |
| R3                   |          0.840 | 0.622 |                63.040 |               8.540 |         25 |             -0.240 |             -0.400 |         -0.161 |         -0.350 |
| B_L3 (+ distractors) |          0.960 | 0.729 |                24.720 |              10.108 |         25 |             -0.360 |             -0.600 |         -0.268 |         -0.583 |

- **F_clut: success drop -0.080 absolute, -13.3% relative · SPL drop -0.009 absolute**
- **F_lightsky: success drop -0.280 absolute, -46.7% relative · SPL drop -0.207 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.035 absolute**
- **F_mat: success drop -0.320 absolute, -53.3% relative · SPL drop -0.289 absolute**
- **R2: success drop -0.320 absolute, -53.3% relative · SPL drop -0.212 absolute**
- **R3: success drop -0.240 absolute, -40.0% relative · SPL drop -0.161 absolute**
- **L3: success drop -0.360 absolute, -60.0% relative · SPL drop -0.268 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
