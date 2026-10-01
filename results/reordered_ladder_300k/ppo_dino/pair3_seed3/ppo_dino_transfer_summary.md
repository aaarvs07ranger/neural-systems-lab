# PPO_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.690 |                33.760 |              11.455 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.660 |                40.360 |              10.839 |         25 |              0.040 |              0.043 |          0.030 |          0.043 |
| F_lightsky           |          0.880 | 0.660 |                40.240 |              10.841 |         25 |              0.040 |              0.043 |          0.030 |          0.043 |
| F_objall             |          0.800 | 0.565 |                57.360 |               9.970 |         25 |              0.120 |              0.130 |          0.125 |          0.181 |
| F_mat                |          0.320 | 0.200 |               141.480 |               3.188 |         25 |              0.600 |              0.652 |          0.490 |          0.710 |
| R2                   |          0.840 | 0.631 |                46.680 |              10.280 |         25 |              0.080 |              0.087 |          0.059 |          0.086 |
| R3                   |          0.640 | 0.457 |                84.200 |               7.815 |         25 |              0.280 |              0.304 |          0.233 |          0.338 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.160 |              -0.613 |         25 |              0.880 |              0.957 |          0.650 |          0.942 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.030 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.030 absolute**
- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.125 absolute**
- **F_mat: success drop 0.600 absolute, 65.2% relative · SPL drop 0.490 absolute**
- **R2: success drop 0.080 absolute, 8.7% relative · SPL drop 0.059 absolute**
- **R3: success drop 0.280 absolute, 30.4% relative · SPL drop 0.233 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.650 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
