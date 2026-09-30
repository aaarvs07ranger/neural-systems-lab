# PPO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.648 |                49.360 |              10.279 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.648 |                49.360 |              10.279 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.680 | 0.471 |                78.160 |               7.935 |         25 |              0.160 |              0.190 |          0.177 |          0.273 |
| F_objall             |          0.600 | 0.463 |                93.120 |               7.076 |         25 |              0.240 |              0.286 |          0.184 |          0.285 |
| F_mat                |          0.000 | 0.000 |               200.000 |              -2.000 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |
| R2                   |          0.680 | 0.471 |                78.160 |               7.935 |         25 |              0.160 |              0.190 |          0.177 |          0.273 |
| R3                   |          0.600 | 0.420 |                92.320 |               6.616 |         25 |              0.240 |              0.286 |          0.228 |          0.352 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.004 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.160 absolute, 19.0% relative · SPL drop 0.177 absolute**
- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.184 absolute**
- **F_mat: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**
- **R2: success drop 0.160 absolute, 19.0% relative · SPL drop 0.177 absolute**
- **R3: success drop 0.240 absolute, 28.6% relative · SPL drop 0.228 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
