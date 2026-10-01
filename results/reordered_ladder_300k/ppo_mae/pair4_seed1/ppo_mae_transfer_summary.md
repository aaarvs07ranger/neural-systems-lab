# PPO_MAE zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.703 |                33.640 |              12.005 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.701 |                33.760 |              12.009 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          0.240 | 0.174 |               154.720 |               2.415 |         25 |              0.680 |              0.739 |          0.528 |          0.752 |
| F_objall             |          0.920 | 0.684 |                34.080 |              11.999 |         25 |              0.000 |              0.000 |          0.019 |          0.027 |
| F_mat                |          0.440 | 0.320 |               119.040 |               5.114 |         25 |              0.480 |              0.522 |          0.382 |          0.544 |
| R2                   |          0.200 | 0.138 |               162.240 |               1.911 |         25 |              0.720 |              0.783 |          0.565 |          0.803 |
| R3                   |          0.000 | 0.000 |               200.000 |              -0.716 |         25 |              0.920 |              1.000 |          0.703 |          1.000 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.915 |         25 |              0.920 |              1.000 |          0.703 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.680 absolute, 73.9% relative · SPL drop 0.528 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.019 absolute**
- **F_mat: success drop 0.480 absolute, 52.2% relative · SPL drop 0.382 absolute**
- **R2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.565 absolute**
- **R3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.703 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.703 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
