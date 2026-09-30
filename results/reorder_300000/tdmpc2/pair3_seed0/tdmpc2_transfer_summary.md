# TDMPC2 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.760 |                34.080 |              12.446 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.717 |                31.480 |              12.057 |         25 |              0.040 |              0.040 |          0.043 |          0.056 |
| F_lightsky           |          0.760 | 0.541 |                86.800 |               9.094 |         25 |              0.240 |              0.240 |          0.219 |          0.288 |
| F_objall             |          0.960 | 0.706 |                40.200 |              11.963 |         25 |              0.040 |              0.040 |          0.054 |          0.071 |
| F_mat                |          0.440 | 0.289 |               142.520 |               3.924 |         25 |              0.560 |              0.560 |          0.471 |          0.620 |
| R2                   |          0.680 | 0.508 |                87.560 |               7.944 |         25 |              0.320 |              0.320 |          0.252 |          0.331 |
| R3                   |          0.840 | 0.609 |                71.360 |               9.783 |         25 |              0.160 |              0.160 |          0.150 |          0.198 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               198.400 |              -1.898 |         25 |              0.960 |              0.960 |          0.720 |          0.947 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **F_lightsky: success drop 0.240 absolute, 24.0% relative · SPL drop 0.219 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.054 absolute**
- **F_mat: success drop 0.560 absolute, 56.0% relative · SPL drop 0.471 absolute**
- **R2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.252 absolute**
- **R3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.150 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.720 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
