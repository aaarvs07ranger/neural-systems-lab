# PPO_MAE zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.720 | 0.567 |                61.320 |               7.352 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.720 | 0.567 |                61.320 |               7.352 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.680 | 0.525 |                68.600 |               6.770 |         25 |              0.040 |              0.056 |          0.042 |          0.073 |
| F_objall             |          0.600 | 0.447 |                83.840 |               5.874 |         25 |              0.120 |              0.167 |          0.120 |          0.212 |
| F_mat                |          0.120 | 0.120 |               176.240 |              -0.477 |         25 |              0.600 |              0.833 |          0.447 |          0.788 |
| R2                   |          0.720 | 0.565 |                60.920 |               7.250 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| R3                   |          0.640 | 0.485 |                75.840 |               6.281 |         25 |              0.080 |              0.111 |          0.082 |          0.144 |
| B_L3 (+ distractors) |          0.080 | 0.080 |               184.400 |              -1.038 |         25 |              0.640 |              0.889 |          0.487 |          0.859 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 5.6% relative · SPL drop 0.042 absolute**
- **F_objall: success drop 0.120 absolute, 16.7% relative · SPL drop 0.120 absolute**
- **F_mat: success drop 0.600 absolute, 83.3% relative · SPL drop 0.447 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.080 absolute, 11.1% relative · SPL drop 0.082 absolute**
- **L3: success drop 0.640 absolute, 88.9% relative · SPL drop 0.487 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
