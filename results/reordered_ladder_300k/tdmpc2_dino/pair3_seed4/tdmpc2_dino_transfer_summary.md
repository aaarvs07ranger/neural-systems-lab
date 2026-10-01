# TDMPC2_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.762 |                20.320 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.761 |                19.800 |              12.603 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_lightsky           |          1.000 | 0.761 |                20.320 |              12.579 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_objall             |          1.000 | 0.763 |                22.640 |              12.555 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          0.680 | 0.491 |                84.000 |               7.802 |         25 |              0.320 |              0.320 |          0.272 |          0.356 |
| R2                   |          1.000 | 0.759 |                21.240 |              12.577 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| R3                   |          1.000 | 0.755 |                30.240 |              12.485 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| B_L3 (+ distractors) |          0.320 | 0.205 |               151.840 |               2.719 |         25 |              0.680 |              0.680 |          0.557 |          0.731 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.272 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
