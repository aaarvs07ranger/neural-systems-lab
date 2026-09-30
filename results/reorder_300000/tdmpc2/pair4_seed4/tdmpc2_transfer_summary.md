# TDMPC2 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.768 |                27.160 |              12.603 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.794 |                19.680 |              13.219 |         25 |             -0.040 |             -0.042 |         -0.026 |         -0.034 |
| F_lightsky           |          0.840 | 0.639 |                62.760 |              10.759 |         25 |              0.120 |              0.125 |          0.129 |          0.168 |
| F_objall             |          0.920 | 0.678 |                36.160 |              11.845 |         25 |              0.040 |              0.042 |          0.091 |          0.118 |
| F_mat                |          0.760 | 0.426 |               108.960 |               9.042 |         25 |              0.200 |              0.208 |          0.343 |          0.446 |
| R2                   |          0.760 | 0.573 |                68.320 |               9.778 |         25 |              0.200 |              0.208 |          0.196 |          0.255 |
| R3                   |          0.680 | 0.436 |                98.240 |               8.084 |         25 |              0.280 |              0.292 |          0.333 |          0.433 |
| B_L3 (+ distractors) |          0.040 | 0.006 |               194.280 |              -1.638 |         25 |              0.920 |              0.958 |          0.763 |          0.993 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.026 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.5% relative · SPL drop 0.129 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.091 absolute**
- **F_mat: success drop 0.200 absolute, 20.8% relative · SPL drop 0.343 absolute**
- **R2: success drop 0.200 absolute, 20.8% relative · SPL drop 0.196 absolute**
- **R3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.333 absolute**
- **L3: success drop 0.920 absolute, 95.8% relative · SPL drop 0.763 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
