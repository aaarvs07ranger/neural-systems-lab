# TDMPC2_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.812 |                18.360 |              13.238 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.815 |                19.040 |              13.228 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_lightsky           |          0.960 | 0.776 |                25.320 |              12.602 |         25 |              0.040 |              0.040 |          0.036 |          0.044 |
| F_objall             |          0.920 | 0.739 |                32.000 |              12.019 |         25 |              0.080 |              0.080 |          0.074 |          0.091 |
| F_mat                |          0.960 | 0.748 |                27.200 |              12.556 |         25 |              0.040 |              0.040 |          0.065 |          0.079 |
| R2                   |          0.960 | 0.734 |                25.400 |              12.619 |         25 |              0.040 |              0.040 |          0.079 |          0.097 |
| R3                   |          0.960 | 0.771 |                25.720 |              12.569 |         25 |              0.040 |              0.040 |          0.041 |          0.051 |
| B_L3 (+ distractors) |          0.800 | 0.628 |                72.040 |              10.056 |         25 |              0.200 |              0.200 |          0.184 |          0.227 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.074 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.065 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.079 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.184 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
