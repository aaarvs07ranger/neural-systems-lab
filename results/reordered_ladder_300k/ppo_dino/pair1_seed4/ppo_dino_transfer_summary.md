# PPO_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.681 |                14.440 |              10.397 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.670 |                22.040 |               9.913 |         25 |              0.040 |              0.042 |          0.011 |          0.017 |
| F_lightsky           |          0.960 | 0.681 |                14.400 |              10.384 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_objall             |          0.920 | 0.641 |                22.360 |               9.922 |         25 |              0.040 |              0.042 |          0.040 |          0.059 |
| F_mat                |          0.760 | 0.506 |                53.320 |               7.841 |         25 |              0.200 |              0.208 |          0.175 |          0.257 |
| R2                   |          0.960 | 0.680 |                14.400 |              10.379 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R3                   |          0.920 | 0.640 |                22.440 |               9.916 |         25 |              0.040 |              0.042 |          0.041 |          0.061 |
| B_L3 (+ distractors) |          0.760 | 0.513 |                53.680 |               7.925 |         25 |              0.200 |              0.208 |          0.169 |          0.247 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.011 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.200 absolute, 20.8% relative · SPL drop 0.175 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.041 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.169 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
