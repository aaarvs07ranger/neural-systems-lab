# DREAMERV3 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.280 | 0.145 |               160.560 |               5.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.480 | 0.247 |               133.760 |               7.472 |         25 |             -0.200 |             -0.714 |         -0.102 |         -0.703 |
| F_lightsky           |          0.960 | 0.566 |                57.760 |              13.008 |         25 |             -0.680 |             -2.429 |         -0.420 |         -2.896 |
| F_objall             |          0.760 | 0.454 |                78.080 |              10.581 |         25 |             -0.480 |             -1.714 |         -0.309 |         -2.126 |
| F_mat                |          0.400 | 0.167 |               146.920 |               6.358 |         25 |             -0.120 |             -0.429 |         -0.022 |         -0.153 |
| R2                   |          0.800 | 0.428 |                80.000 |              11.081 |         25 |             -0.520 |             -1.857 |         -0.282 |         -1.945 |
| R3                   |          0.880 | 0.513 |                69.920 |              11.880 |         25 |             -0.600 |             -2.143 |         -0.368 |         -2.536 |
| B_L3 (+ distractors) |          0.760 | 0.396 |                91.920 |               9.432 |         25 |             -0.480 |             -1.714 |         -0.251 |         -1.731 |

- **F_clut: success drop -0.200 absolute, -71.4% relative · SPL drop -0.102 absolute**
- **F_lightsky: success drop -0.680 absolute, -242.9% relative · SPL drop -0.420 absolute**
- **F_objall: success drop -0.480 absolute, -171.4% relative · SPL drop -0.309 absolute**
- **F_mat: success drop -0.120 absolute, -42.9% relative · SPL drop -0.022 absolute**
- **R2: success drop -0.520 absolute, -185.7% relative · SPL drop -0.282 absolute**
- **R3: success drop -0.600 absolute, -214.3% relative · SPL drop -0.368 absolute**
- **L3: success drop -0.480 absolute, -171.4% relative · SPL drop -0.251 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
