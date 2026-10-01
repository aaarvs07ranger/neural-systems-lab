# DREAMERV3 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.585 |                25.280 |              13.904 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.587 |                25.440 |              13.908 |         25 |              0.000 |              0.000 |         -0.002 |         -0.004 |
| F_lightsky           |          0.960 | 0.561 |                31.280 |              13.173 |         25 |              0.040 |              0.040 |          0.024 |          0.041 |
| F_objall             |          1.000 | 0.652 |                23.800 |              13.668 |         25 |              0.000 |              0.000 |         -0.067 |         -0.115 |
| F_mat                |          0.960 | 0.490 |                35.560 |              13.197 |         25 |              0.040 |              0.040 |          0.095 |          0.162 |
| R2                   |          1.000 | 0.588 |                26.280 |              13.890 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| R3                   |          0.960 | 0.630 |                31.400 |              13.011 |         25 |              0.040 |              0.040 |         -0.045 |         -0.078 |
| B_L3 (+ distractors) |          0.880 | 0.483 |                49.000 |              11.863 |         25 |              0.120 |              0.120 |          0.102 |          0.175 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.024 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.067 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.095 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.045 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.102 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
