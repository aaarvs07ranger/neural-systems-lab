# PPO_AUG zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.631 |                57.920 |               9.829 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.630 |                57.960 |               9.832 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          0.720 | 0.543 |                71.160 |               8.501 |         25 |              0.080 |              0.100 |          0.088 |          0.139 |
| F_objall             |          0.160 | 0.115 |               169.800 |               1.462 |         25 |              0.640 |              0.800 |          0.516 |          0.818 |
| F_mat                |          0.360 | 0.258 |               132.320 |               2.984 |         25 |              0.440 |              0.550 |          0.373 |          0.591 |
| R2                   |          0.720 | 0.543 |                71.120 |               8.500 |         25 |              0.080 |              0.100 |          0.088 |          0.139 |
| R3                   |          0.480 | 0.325 |               114.280 |               5.028 |         25 |              0.320 |              0.400 |          0.307 |          0.486 |
| B_L3 (+ distractors) |          0.320 | 0.218 |               140.000 |               2.187 |         25 |              0.480 |              0.600 |          0.413 |          0.655 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.080 absolute, 10.0% relative · SPL drop 0.088 absolute**
- **F_objall: success drop 0.640 absolute, 80.0% relative · SPL drop 0.516 absolute**
- **F_mat: success drop 0.440 absolute, 55.0% relative · SPL drop 0.373 absolute**
- **R2: success drop 0.080 absolute, 10.0% relative · SPL drop 0.088 absolute**
- **R3: success drop 0.320 absolute, 40.0% relative · SPL drop 0.307 absolute**
- **L3: success drop 0.480 absolute, 60.0% relative · SPL drop 0.413 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
