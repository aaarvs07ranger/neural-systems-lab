# PPO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.698 |                21.800 |               9.920 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.698 |                21.800 |               9.923 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.920 | 0.670 |                22.040 |               9.887 |         25 |              0.000 |              0.000 |          0.029 |          0.041 |
| F_objall             |          0.320 | 0.276 |               137.480 |               2.088 |         25 |              0.600 |              0.652 |          0.422 |          0.604 |
| F_mat                |          0.640 | 0.570 |                76.920 |               6.001 |         25 |              0.280 |              0.304 |          0.128 |          0.184 |
| R2                   |          0.920 | 0.670 |                22.040 |               9.883 |         25 |              0.000 |              0.000 |          0.029 |          0.041 |
| R3                   |          0.200 | 0.200 |               160.280 |               0.498 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.520 |               0.395 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.029 absolute**
- **F_objall: success drop 0.600 absolute, 65.2% relative · SPL drop 0.422 absolute**
- **F_mat: success drop 0.280 absolute, 30.4% relative · SPL drop 0.128 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.029 absolute**
- **R3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
