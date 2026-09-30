# DREAMERV3 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.758 |                13.520 |              11.587 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.756 |                13.120 |              11.592 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_lightsky           |          1.000 | 0.656 |                30.360 |              11.394 |         25 |              0.000 |              0.000 |          0.102 |          0.134 |
| F_objall             |          1.000 | 0.765 |                13.520 |              11.580 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_mat                |          1.000 | 0.701 |                18.480 |              11.528 |         25 |              0.000 |              0.000 |          0.057 |          0.075 |
| R2                   |          1.000 | 0.659 |                31.240 |              11.390 |         25 |              0.000 |              0.000 |          0.099 |          0.131 |
| R3                   |          1.000 | 0.592 |                55.720 |              11.133 |         25 |              0.000 |              0.000 |          0.166 |          0.219 |
| B_L3 (+ distractors) |          1.000 | 0.652 |                33.800 |              11.352 |         25 |              0.000 |              0.000 |          0.106 |          0.140 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.102 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.057 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.099 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.166 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.106 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
