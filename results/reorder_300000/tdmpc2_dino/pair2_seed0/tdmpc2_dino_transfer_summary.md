# TDMPC2_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.780 |                 8.480 |              10.677 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                10.400 |              10.671 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_lightsky           |          1.000 | 0.779 |                 9.440 |              10.669 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_objall             |          1.000 | 0.780 |                11.000 |              10.661 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                |          1.000 | 0.777 |                 9.120 |              10.670 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| R2                   |          0.960 | 0.739 |                15.720 |              10.201 |         25 |              0.040 |              0.040 |          0.041 |          0.052 |
| R3                   |          0.960 | 0.737 |                19.920 |              10.180 |         25 |              0.040 |              0.040 |          0.043 |          0.055 |
| B_L3 (+ distractors) |          0.960 | 0.739 |                19.960 |              10.173 |         25 |              0.040 |              0.040 |          0.042 |          0.053 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
