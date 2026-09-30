# PPO_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                17.160 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.783 |                17.200 |              10.960 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.920 | 0.730 |                25.160 |              10.449 |         25 |              0.040 |              0.042 |          0.053 |          0.068 |
| F_objall             |          0.800 | 0.610 |                48.560 |               8.868 |         25 |              0.160 |              0.167 |          0.173 |          0.221 |
| F_mat                |          0.920 | 0.752 |                24.920 |              10.616 |         25 |              0.040 |              0.042 |          0.031 |          0.040 |
| R2                   |          0.920 | 0.732 |                25.160 |              10.456 |         25 |              0.040 |              0.042 |          0.051 |          0.065 |
| R3                   |          0.680 | 0.536 |                70.960 |               7.170 |         25 |              0.280 |              0.292 |          0.247 |          0.315 |
| B_L3 (+ distractors) |          0.800 | 0.635 |                47.880 |               8.788 |         25 |              0.160 |              0.167 |          0.148 |          0.189 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.053 absolute**
- **F_objall: success drop 0.160 absolute, 16.7% relative · SPL drop 0.173 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.051 absolute**
- **R3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.247 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
