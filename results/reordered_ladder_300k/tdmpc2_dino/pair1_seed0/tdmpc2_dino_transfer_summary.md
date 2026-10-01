# TDMPC2_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.720 |                 9.520 |              10.851 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.714 |                 9.880 |              10.851 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_lightsky           |          1.000 | 0.716 |                 8.880 |              10.863 |         25 |              0.000 |              0.000 |          0.003 |          0.005 |
| F_objall             |          1.000 | 0.714 |                10.080 |              10.881 |         25 |              0.000 |              0.000 |          0.006 |          0.008 |
| F_mat                |          1.000 | 0.700 |                12.240 |              10.834 |         25 |              0.000 |              0.000 |          0.020 |          0.028 |
| R2                   |          1.000 | 0.718 |                 7.720 |              10.858 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R3                   |          1.000 | 0.717 |                 9.360 |              10.900 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| B_L3 (+ distractors) |          1.000 | 0.696 |                13.280 |              10.806 |         25 |              0.000 |              0.000 |          0.023 |          0.033 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.023 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
