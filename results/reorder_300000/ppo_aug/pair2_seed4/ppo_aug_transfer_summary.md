# PPO_AUG zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.700 |                24.600 |               9.743 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.700 |                24.600 |               9.743 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.660 |                31.200 |               9.258 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_objall             |          0.880 | 0.660 |                31.800 |               9.262 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_mat                |          0.760 | 0.540 |                55.360 |               7.823 |         25 |              0.160 |              0.174 |          0.160 |          0.228 |
| R2                   |          0.880 | 0.660 |                31.200 |               9.258 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| R3                   |          0.880 | 0.660 |                31.800 |               9.262 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| B_L3 (+ distractors) |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **R3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
