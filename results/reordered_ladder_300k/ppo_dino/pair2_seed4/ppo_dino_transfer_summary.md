# PPO_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.738 |                14.320 |              10.230 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.738 |                14.320 |              10.230 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.691 |                29.960 |               9.282 |         25 |              0.080 |              0.083 |          0.047 |          0.063 |
| F_objall             |          0.840 | 0.652 |                37.360 |               8.786 |         25 |              0.120 |              0.125 |          0.086 |          0.116 |
| F_mat                |          0.880 | 0.692 |                30.280 |               9.250 |         25 |              0.080 |              0.083 |          0.046 |          0.062 |
| R2                   |          0.880 | 0.691 |                29.960 |               9.282 |         25 |              0.080 |              0.083 |          0.047 |          0.063 |
| R3                   |          0.960 | 0.738 |                15.080 |              10.232 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L3 (+ distractors) |          0.880 | 0.691 |                31.000 |               9.164 |         25 |              0.080 |              0.083 |          0.047 |          0.063 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.047 absolute**
- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.086 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.046 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.047 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
