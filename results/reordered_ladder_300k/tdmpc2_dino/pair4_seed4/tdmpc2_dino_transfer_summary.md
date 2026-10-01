# TDMPC2_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.775 |                26.000 |              12.592 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.735 |                34.840 |              12.103 |         25 |              0.040 |              0.042 |          0.040 |          0.052 |
| F_lightsky           |          0.960 | 0.750 |                31.960 |              12.607 |         25 |              0.000 |              0.000 |          0.025 |          0.033 |
| F_objall             |          0.960 | 0.774 |                25.800 |              12.559 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_mat                |          0.920 | 0.709 |                37.040 |              11.960 |         25 |              0.040 |              0.042 |          0.066 |          0.086 |
| R2                   |          0.920 | 0.740 |                34.600 |              12.110 |         25 |              0.040 |              0.042 |          0.035 |          0.045 |
| R3                   |          0.960 | 0.747 |                29.800 |              12.535 |         25 |              0.000 |              0.000 |          0.028 |          0.036 |
| B_L3 (+ distractors) |          0.960 | 0.674 |                39.160 |              12.583 |         25 |              0.000 |              0.000 |          0.101 |          0.130 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.025 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.066 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.035 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.028 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.101 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
