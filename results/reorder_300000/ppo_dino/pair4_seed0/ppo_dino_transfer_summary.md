# PPO_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.771 |                21.080 |              13.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.752 |                28.520 |              12.698 |         25 |              0.040 |              0.040 |          0.019 |          0.024 |
| F_lightsky           |          1.000 | 0.766 |                21.120 |              13.207 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_objall             |          0.960 | 0.712 |                27.720 |              12.469 |         25 |              0.040 |              0.040 |          0.059 |          0.076 |
| F_mat                |          0.280 | 0.214 |               148.360 |               3.725 |         25 |              0.720 |              0.720 |          0.557 |          0.722 |
| R2                   |          0.960 | 0.746 |                28.760 |              12.713 |         25 |              0.040 |              0.040 |          0.025 |          0.032 |
| R3                   |          1.000 | 0.759 |                21.120 |              13.165 |         25 |              0.000 |              0.000 |          0.012 |          0.016 |
| B_L3 (+ distractors) |          0.320 | 0.233 |               142.920 |               4.049 |         25 |              0.680 |              0.680 |          0.537 |          0.697 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.019 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.059 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.557 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.537 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
