# TDMPC2_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.760 |                20.240 |              12.577 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.760 |                21.480 |              12.552 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_lightsky           |          0.840 | 0.594 |                51.760 |              10.637 |         25 |              0.160 |              0.160 |          0.166 |          0.219 |
| F_objall             |          0.960 | 0.731 |                30.200 |              11.924 |         25 |              0.040 |              0.040 |          0.029 |          0.038 |
| F_mat                |          0.520 | 0.343 |               113.200 |               5.781 |         25 |              0.480 |              0.480 |          0.417 |          0.549 |
| R2                   |          0.840 | 0.609 |                50.640 |              10.536 |         25 |              0.160 |              0.160 |          0.151 |          0.199 |
| R3                   |          0.800 | 0.630 |                63.160 |               9.675 |         25 |              0.200 |              0.200 |          0.130 |          0.171 |
| B_L3 (+ distractors) |          0.480 | 0.323 |               124.760 |               4.642 |         25 |              0.520 |              0.520 |          0.437 |          0.576 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.166 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.029 absolute**
- **F_mat: success drop 0.480 absolute, 48.0% relative · SPL drop 0.417 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.151 absolute**
- **R3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.130 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.437 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
