# TDMPC2_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.760 |                21.640 |              12.576 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.761 |                22.400 |              12.562 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_lightsky           |          1.000 | 0.756 |                23.160 |              12.550 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |
| F_objall             |          0.920 | 0.695 |                44.400 |              11.308 |         25 |              0.080 |              0.080 |          0.065 |          0.086 |
| F_mat                |          0.680 | 0.488 |                93.760 |               7.746 |         25 |              0.320 |              0.320 |          0.272 |          0.358 |
| R2                   |          0.960 | 0.724 |                30.000 |              11.896 |         25 |              0.040 |              0.040 |          0.036 |          0.047 |
| R3                   |          0.920 | 0.686 |                41.160 |              11.552 |         25 |              0.080 |              0.080 |          0.074 |          0.098 |
| B_L3 (+ distractors) |          0.400 | 0.285 |               152.200 |               3.800 |         25 |              0.600 |              0.600 |          0.475 |          0.625 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.065 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.272 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.074 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.475 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
