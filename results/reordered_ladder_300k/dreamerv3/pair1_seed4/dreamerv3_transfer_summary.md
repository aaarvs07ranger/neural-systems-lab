# DREAMERV3 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.673 |                15.200 |              10.936 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.672 |                15.680 |              10.945 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_lightsky           |          1.000 | 0.681 |                13.520 |              10.939 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| F_objall             |          1.000 | 0.699 |                11.040 |              10.861 |         25 |              0.000 |              0.000 |         -0.026 |         -0.038 |
| F_mat                |          0.280 | 0.280 |               146.400 |               0.894 |         25 |              0.720 |              0.720 |          0.393 |          0.584 |
| R2                   |          1.000 | 0.679 |                18.720 |              10.944 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| R3                   |          1.000 | 0.682 |                11.400 |              10.805 |         25 |              0.000 |              0.000 |         -0.009 |         -0.013 |
| B_L3 (+ distractors) |          0.280 | 0.280 |               147.280 |               1.159 |         25 |              0.720 |              0.720 |          0.393 |          0.584 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.026 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.393 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.393 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
