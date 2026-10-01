# PPO_JEPA zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.700 |                21.600 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.700 |                21.560 |               9.891 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.880 | 0.660 |                29.600 |               9.409 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_objall             |          0.720 | 0.565 |                60.680 |               7.219 |         25 |              0.200 |              0.217 |          0.135 |          0.193 |
| F_mat                |          0.400 | 0.323 |               121.640 |               3.034 |         25 |              0.520 |              0.565 |          0.377 |          0.539 |
| R2                   |          0.880 | 0.660 |                29.600 |               9.406 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| R3                   |          0.160 | 0.160 |               168.200 |               0.048 |         25 |              0.760 |              0.826 |          0.540 |          0.772 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_objall: success drop 0.200 absolute, 21.7% relative · SPL drop 0.135 absolute**
- **F_mat: success drop 0.520 absolute, 56.5% relative · SPL drop 0.377 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **R3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.540 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
