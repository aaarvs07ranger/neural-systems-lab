# PPO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.817 |                14.720 |              11.545 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.817 |                14.720 |              11.545 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.160 | 0.135 |               169.320 |               0.309 |         25 |              0.840 |              0.840 |          0.682 |          0.835 |
| F_objall             |          0.280 | 0.176 |               159.000 |               2.462 |         25 |              0.720 |              0.720 |          0.641 |          0.785 |
| F_mat                |          0.280 | 0.237 |               146.800 |               1.718 |         25 |              0.720 |              0.720 |          0.579 |          0.709 |
| R2                   |          0.160 | 0.135 |               169.320 |               0.515 |         25 |              0.840 |              0.840 |          0.682 |          0.835 |
| R3                   |          0.120 | 0.120 |               176.400 |              -0.328 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |
| B_L3 (+ distractors) |          0.120 | 0.120 |               177.600 |              -0.177 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.840 absolute, 84.0% relative · SPL drop 0.682 absolute**
- **F_objall: success drop 0.720 absolute, 72.0% relative · SPL drop 0.641 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.579 absolute**
- **R2: success drop 0.840 absolute, 84.0% relative · SPL drop 0.682 absolute**
- **R3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
