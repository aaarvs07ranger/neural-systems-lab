# PPO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.639 |                47.760 |              10.218 |         25 |              0.160 |              0.160 |          0.121 |          0.159 |
| F_objall             |          0.480 | 0.399 |               115.680 |               6.068 |         25 |              0.520 |              0.520 |          0.361 |          0.475 |
| F_mat                |          0.040 | 0.040 |               192.160 |              -1.540 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| R2                   |          0.840 | 0.639 |                47.760 |              10.218 |         25 |              0.160 |              0.160 |          0.121 |          0.159 |
| R3                   |          0.720 | 0.567 |                67.760 |               8.152 |         25 |              0.280 |              0.280 |          0.194 |          0.255 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.200 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.121 absolute**
- **F_objall: success drop 0.520 absolute, 52.0% relative · SPL drop 0.361 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.121 absolute**
- **R3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.194 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
