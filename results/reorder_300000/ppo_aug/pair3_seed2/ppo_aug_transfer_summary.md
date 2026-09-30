# PPO_AUG zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.730 |                26.800 |              11.973 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.730 |                26.800 |              11.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.642 |                48.200 |              10.257 |         25 |              0.120 |              0.125 |          0.088 |          0.121 |
| F_objall             |          0.720 | 0.538 |                75.320 |               8.708 |         25 |              0.240 |              0.250 |          0.193 |          0.264 |
| F_mat                |          0.520 | 0.407 |               101.680 |               5.107 |         25 |              0.440 |              0.458 |          0.323 |          0.442 |
| R2                   |          0.840 | 0.642 |                48.200 |              10.257 |         25 |              0.120 |              0.125 |          0.088 |          0.121 |
| R3                   |          0.760 | 0.588 |                61.360 |               8.936 |         25 |              0.200 |              0.208 |          0.143 |          0.195 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.230 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.5% relative · SPL drop 0.088 absolute**
- **F_objall: success drop 0.240 absolute, 25.0% relative · SPL drop 0.193 absolute**
- **F_mat: success drop 0.440 absolute, 45.8% relative · SPL drop 0.323 absolute**
- **R2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.088 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.143 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
