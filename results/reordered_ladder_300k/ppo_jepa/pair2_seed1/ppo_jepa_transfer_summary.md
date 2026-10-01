# PPO_JEPA zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.651 |                37.280 |               8.796 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.651 |                37.280 |               8.796 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.618 |                37.320 |               8.783 |         25 |              0.000 |              0.000 |          0.033 |          0.051 |
| F_objall             |          0.920 | 0.698 |                21.840 |               9.744 |         25 |             -0.080 |             -0.095 |         -0.047 |         -0.073 |
| F_mat                |          0.840 | 0.620 |                37.560 |               8.784 |         25 |              0.000 |              0.000 |          0.031 |          0.047 |
| R2                   |          0.840 | 0.618 |                37.320 |               8.783 |         25 |              0.000 |              0.000 |          0.033 |          0.051 |
| R3                   |          0.880 | 0.659 |                29.520 |               9.258 |         25 |             -0.040 |             -0.048 |         -0.008 |         -0.013 |
| B_L3 (+ distractors) |          0.600 | 0.444 |                83.680 |               5.764 |         25 |              0.240 |              0.286 |          0.207 |          0.318 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.033 absolute**
- **F_objall: success drop -0.080 absolute, -9.5% relative · SPL drop -0.047 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.031 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.033 absolute**
- **R3: success drop -0.040 absolute, -4.8% relative · SPL drop -0.008 absolute**
- **L3: success drop 0.240 absolute, 28.6% relative · SPL drop 0.207 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
