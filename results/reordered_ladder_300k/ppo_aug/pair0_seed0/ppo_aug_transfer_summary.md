# PPO_AUG zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.785 |                20.920 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.785 |                20.920 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.785 |                21.120 |              10.944 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_objall             |          0.160 | 0.149 |               169.040 |               0.792 |         25 |              0.800 |              0.833 |          0.636 |          0.810 |
| F_mat                |          0.840 | 0.702 |                44.240 |               9.309 |         25 |              0.120 |              0.125 |          0.084 |          0.107 |
| R2                   |          0.960 | 0.783 |                21.160 |              10.946 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| R3                   |          0.120 | 0.120 |               176.360 |              -0.304 |         25 |              0.840 |              0.875 |          0.665 |          0.847 |
| B_L3 (+ distractors) |          0.160 | 0.140 |               169.600 |               0.290 |         25 |              0.800 |              0.833 |          0.646 |          0.822 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_objall: success drop 0.800 absolute, 83.3% relative · SPL drop 0.636 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.084 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **R3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.665 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.646 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
