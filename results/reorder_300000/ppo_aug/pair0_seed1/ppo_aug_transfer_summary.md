# PPO_AUG zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.771 |                19.920 |              11.092 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.771 |                19.920 |              11.092 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.760 | 0.608 |                57.960 |               8.530 |         25 |              0.200 |              0.208 |          0.164 |          0.213 |
| F_objall             |          0.680 | 0.541 |                72.760 |               7.680 |         25 |              0.280 |              0.292 |          0.230 |          0.299 |
| F_mat                |          0.800 | 0.631 |                51.000 |               8.711 |         25 |              0.160 |              0.167 |          0.140 |          0.182 |
| R2                   |          0.720 | 0.571 |                65.200 |               7.929 |         25 |              0.240 |              0.250 |          0.201 |          0.260 |
| R3                   |          0.200 | 0.163 |               162.600 |               0.836 |         25 |              0.760 |              0.792 |          0.608 |          0.789 |
| B_L3 (+ distractors) |          0.280 | 0.191 |               149.360 |               1.869 |         25 |              0.680 |              0.708 |          0.581 |          0.752 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.200 absolute, 20.8% relative · SPL drop 0.164 absolute**
- **F_objall: success drop 0.280 absolute, 29.2% relative · SPL drop 0.230 absolute**
- **F_mat: success drop 0.160 absolute, 16.7% relative · SPL drop 0.140 absolute**
- **R2: success drop 0.240 absolute, 25.0% relative · SPL drop 0.201 absolute**
- **R3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.608 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.581 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
