# PPO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.674 |                41.920 |               9.612 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.665 |                42.080 |               9.617 |         25 |              0.000 |              0.000 |          0.009 |          0.014 |
| F_lightsky           |          0.720 | 0.588 |                64.080 |               7.861 |         25 |              0.120 |              0.143 |          0.086 |          0.128 |
| F_objall             |          0.160 | 0.150 |               169.120 |               0.687 |         25 |              0.680 |              0.810 |          0.525 |          0.778 |
| F_mat                |          0.480 | 0.423 |               108.440 |               4.393 |         25 |              0.360 |              0.429 |          0.251 |          0.372 |
| R2                   |          0.720 | 0.573 |                64.720 |               7.853 |         25 |              0.120 |              0.143 |          0.101 |          0.150 |
| R3                   |          0.200 | 0.190 |               161.480 |               0.641 |         25 |              0.640 |              0.762 |          0.485 |          0.719 |
| B_L3 (+ distractors) |          0.240 | 0.194 |               154.760 |               1.157 |         25 |              0.600 |              0.714 |          0.481 |          0.713 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_lightsky: success drop 0.120 absolute, 14.3% relative · SPL drop 0.086 absolute**
- **F_objall: success drop 0.680 absolute, 81.0% relative · SPL drop 0.525 absolute**
- **F_mat: success drop 0.360 absolute, 42.9% relative · SPL drop 0.251 absolute**
- **R2: success drop 0.120 absolute, 14.3% relative · SPL drop 0.101 absolute**
- **R3: success drop 0.640 absolute, 76.2% relative · SPL drop 0.485 absolute**
- **L3: success drop 0.600 absolute, 71.4% relative · SPL drop 0.481 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
