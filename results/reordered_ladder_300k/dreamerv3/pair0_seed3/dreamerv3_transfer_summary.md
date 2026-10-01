# DREAMERV3 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.750 |                22.040 |              11.088 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.749 |                21.640 |              11.085 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          1.000 | 0.709 |                36.640 |              11.350 |         25 |             -0.040 |             -0.042 |          0.041 |          0.055 |
| F_objall             |          1.000 | 0.799 |                12.600 |              11.559 |         25 |             -0.040 |             -0.042 |         -0.049 |         -0.065 |
| F_mat                |          1.000 | 0.708 |                26.680 |              11.432 |         25 |             -0.040 |             -0.042 |          0.042 |          0.056 |
| R2                   |          0.960 | 0.694 |                30.400 |              10.970 |         25 |              0.000 |              0.000 |          0.056 |          0.074 |
| R3                   |          0.960 | 0.637 |                44.880 |              10.787 |         25 |              0.000 |              0.000 |          0.113 |          0.151 |
| B_L3 (+ distractors) |          0.920 | 0.542 |                63.960 |              10.178 |         25 |              0.040 |              0.042 |          0.208 |          0.277 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.2% relative · SPL drop 0.041 absolute**
- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.049 absolute**
- **F_mat: success drop -0.040 absolute, -4.2% relative · SPL drop 0.042 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.056 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.113 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.208 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
