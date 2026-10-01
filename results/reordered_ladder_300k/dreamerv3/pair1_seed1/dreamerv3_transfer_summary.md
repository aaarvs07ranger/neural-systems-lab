# DREAMERV3 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.640 | 0.459 |                86.320 |               6.485 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.600 | 0.418 |                97.240 |               5.996 |         25 |              0.040 |              0.063 |          0.041 |          0.089 |
| F_lightsky           |          0.640 | 0.390 |                92.440 |               6.438 |         25 |              0.000 |              0.000 |          0.069 |          0.150 |
| F_objall             |          0.920 | 0.611 |                48.080 |               9.787 |         25 |             -0.280 |             -0.438 |         -0.152 |         -0.331 |
| F_mat                |          0.240 | 0.202 |               166.680 |               1.451 |         25 |              0.400 |              0.625 |          0.256 |          0.559 |
| R2                   |          0.520 | 0.373 |               105.680 |               5.083 |         25 |              0.120 |              0.188 |          0.085 |          0.186 |
| R3                   |          1.000 | 0.661 |                33.640 |              10.605 |         25 |             -0.360 |             -0.562 |         -0.203 |         -0.442 |
| B_L3 (+ distractors) |          0.400 | 0.328 |               133.760 |               3.578 |         25 |              0.240 |              0.375 |          0.131 |          0.285 |

- **F_clut: success drop 0.040 absolute, 6.3% relative · SPL drop 0.041 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.069 absolute**
- **F_objall: success drop -0.280 absolute, -43.8% relative · SPL drop -0.152 absolute**
- **F_mat: success drop 0.400 absolute, 62.5% relative · SPL drop 0.256 absolute**
- **R2: success drop 0.120 absolute, 18.8% relative · SPL drop 0.085 absolute**
- **R3: success drop -0.360 absolute, -56.2% relative · SPL drop -0.203 absolute**
- **L3: success drop 0.240 absolute, 37.5% relative · SPL drop 0.131 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
