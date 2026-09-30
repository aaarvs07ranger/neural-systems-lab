# PPO_JEPA zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.727 |                27.800 |              12.569 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.727 |                27.840 |              12.571 |         25 |              0.000 |              0.000 |         -0.000 |         -0.001 |
| F_lightsky           |          0.960 | 0.735 |                27.600 |              12.576 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| F_objall             |          0.920 | 0.670 |                34.720 |              12.093 |         25 |              0.040 |              0.042 |          0.057 |          0.078 |
| F_mat                |          0.520 | 0.358 |               105.760 |               5.761 |         25 |              0.440 |              0.458 |          0.369 |          0.508 |
| R2                   |          0.960 | 0.731 |                27.720 |              12.569 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| R3                   |          0.920 | 0.692 |                34.280 |              11.792 |         25 |              0.040 |              0.042 |          0.035 |          0.048 |
| B_L3 (+ distractors) |          0.320 | 0.241 |               140.880 |               3.276 |         25 |              0.640 |              0.667 |          0.486 |          0.669 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.057 absolute**
- **F_mat: success drop 0.440 absolute, 45.8% relative · SPL drop 0.369 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.035 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.486 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
