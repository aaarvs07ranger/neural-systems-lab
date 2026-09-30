# PPO_JEPA zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.700 |                21.680 |               9.891 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.660 |                29.520 |               9.418 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_lightsky           |          0.840 | 0.638 |                37.320 |               8.924 |         25 |              0.080 |              0.087 |          0.062 |          0.088 |
| F_objall             |          0.240 | 0.211 |               152.880 |               1.376 |         25 |              0.680 |              0.739 |          0.489 |          0.698 |
| F_mat                |          0.240 | 0.240 |               152.280 |               0.937 |         25 |              0.680 |              0.739 |          0.460 |          0.657 |
| R2                   |          0.840 | 0.638 |                37.280 |               8.916 |         25 |              0.080 |              0.087 |          0.062 |          0.088 |
| R3                   |          0.160 | 0.160 |               168.200 |               0.095 |         25 |              0.760 |              0.826 |          0.540 |          0.772 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.7% relative · SPL drop 0.062 absolute**
- **F_objall: success drop 0.680 absolute, 73.9% relative · SPL drop 0.489 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.460 absolute**
- **R2: success drop 0.080 absolute, 8.7% relative · SPL drop 0.062 absolute**
- **R3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.540 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
