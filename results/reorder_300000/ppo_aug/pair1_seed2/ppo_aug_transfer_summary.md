# PPO_AUG zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.719 |                 9.840 |              10.824 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.711 |                17.240 |              10.321 |         25 |              0.040 |              0.040 |          0.008 |          0.011 |
| F_lightsky           |          0.920 | 0.667 |                24.800 |               9.802 |         25 |              0.080 |              0.080 |          0.052 |          0.072 |
| F_objall             |          0.840 | 0.610 |                41.680 |               8.883 |         25 |              0.160 |              0.160 |          0.110 |          0.152 |
| F_mat                |          0.200 | 0.138 |               160.960 |               0.271 |         25 |              0.800 |              0.800 |          0.581 |          0.808 |
| R2                   |          0.920 | 0.671 |                24.840 |               9.799 |         25 |              0.080 |              0.080 |          0.048 |          0.067 |
| R3                   |          0.920 | 0.666 |                29.960 |               9.789 |         25 |              0.080 |              0.080 |          0.054 |          0.074 |
| B_L3 (+ distractors) |          0.160 | 0.160 |               169.120 |              -0.130 |         25 |              0.840 |              0.840 |          0.559 |          0.778 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.008 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.052 absolute**
- **F_objall: success drop 0.160 absolute, 16.0% relative · SPL drop 0.110 absolute**
- **F_mat: success drop 0.800 absolute, 80.0% relative · SPL drop 0.581 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.048 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.054 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.559 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
