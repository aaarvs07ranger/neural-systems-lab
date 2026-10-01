# PPO_MAE zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.695 |                21.760 |               9.908 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.699 |                21.720 |               9.897 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_lightsky           |          0.880 | 0.657 |                29.560 |               9.413 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_objall             |          0.880 | 0.647 |                30.080 |               9.416 |         25 |              0.040 |              0.043 |          0.048 |          0.069 |
| F_mat                |          0.240 | 0.240 |               152.440 |               0.964 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| R2                   |          0.880 | 0.658 |                29.560 |               9.404 |         25 |              0.040 |              0.043 |          0.036 |          0.052 |
| R3                   |          0.840 | 0.608 |                38.240 |               8.864 |         25 |              0.080 |              0.087 |          0.087 |          0.125 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.495 |          0.712 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.048 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.036 absolute**
- **R3: success drop 0.080 absolute, 8.7% relative · SPL drop 0.087 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
