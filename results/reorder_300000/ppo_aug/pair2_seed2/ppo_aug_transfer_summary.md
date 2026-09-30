# PPO_AUG zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.779 |                 9.680 |              10.674 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 9.680 |              10.674 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.620 |                40.240 |               8.708 |         25 |              0.160 |              0.160 |          0.158 |          0.203 |
| F_objall             |          1.000 | 0.779 |                 9.680 |              10.670 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                |          0.800 | 0.579 |                47.920 |               8.262 |         25 |              0.200 |              0.200 |          0.200 |          0.257 |
| R2                   |          0.840 | 0.620 |                40.240 |               8.708 |         25 |              0.160 |              0.160 |          0.158 |          0.203 |
| R3                   |          0.840 | 0.654 |                39.800 |               8.667 |         25 |              0.160 |              0.160 |          0.125 |          0.161 |
| B_L3 (+ distractors) |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.158 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.200 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.158 absolute**
- **R3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.125 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
