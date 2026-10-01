# TDMPC2_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.779 |                 9.080 |              10.697 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.739 |                19.840 |              10.192 |         25 |              0.040 |              0.040 |          0.039 |          0.050 |
| F_lightsky           |          0.960 | 0.740 |                18.400 |              10.227 |         25 |              0.040 |              0.040 |          0.038 |          0.049 |
| F_objall             |          0.960 | 0.740 |                18.480 |              10.188 |         25 |              0.040 |              0.040 |          0.038 |          0.049 |
| F_mat                |          0.960 | 0.740 |                17.160 |              10.204 |         25 |              0.040 |              0.040 |          0.038 |          0.049 |
| R2                   |          1.000 | 0.779 |                14.440 |              10.616 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| R3                   |          1.000 | 0.780 |                17.680 |              10.619 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| B_L3 (+ distractors) |          1.000 | 0.780 |                13.240 |              10.644 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
