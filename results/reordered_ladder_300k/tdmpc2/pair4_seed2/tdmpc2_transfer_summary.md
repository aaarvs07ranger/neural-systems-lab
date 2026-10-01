# TDMPC2 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.768 |                27.000 |              12.617 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.809 |                19.520 |              13.230 |         25 |             -0.040 |             -0.042 |         -0.041 |         -0.053 |
| F_lightsky           |          0.880 | 0.604 |                96.720 |              11.011 |         25 |              0.080 |              0.083 |          0.165 |          0.214 |
| F_objall             |          0.960 | 0.758 |                27.720 |              12.500 |         25 |              0.000 |              0.000 |          0.011 |          0.014 |
| F_mat                |          0.840 | 0.634 |                53.000 |              10.799 |         25 |              0.120 |              0.125 |          0.135 |          0.176 |
| R2                   |          0.880 | 0.627 |                95.440 |              10.906 |         25 |              0.080 |              0.083 |          0.141 |          0.184 |
| R3                   |          0.160 | 0.092 |               177.600 |               1.281 |         25 |              0.800 |              0.833 |          0.676 |          0.880 |
| B_L3 (+ distractors) |          0.080 | 0.033 |               186.240 |               0.208 |         25 |              0.880 |              0.917 |          0.735 |          0.957 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.041 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.165 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.135 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.141 absolute**
- **R3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.676 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.735 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
