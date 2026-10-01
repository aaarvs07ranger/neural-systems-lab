# PPO_JEPA zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.694 |                21.840 |               9.908 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.614 |                37.120 |               8.932 |         25 |              0.080 |              0.087 |          0.080 |          0.115 |
| F_lightsky           |          0.920 | 0.700 |                21.800 |               9.899 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_objall             |          0.680 | 0.544 |                68.600 |               6.708 |         25 |              0.240 |              0.261 |          0.150 |          0.216 |
| F_mat                |          0.240 | 0.240 |               152.320 |               0.917 |         25 |              0.680 |              0.739 |          0.454 |          0.654 |
| R2                   |          0.920 | 0.694 |                21.840 |               9.904 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| R3                   |          0.280 | 0.280 |               145.000 |               1.563 |         25 |              0.640 |              0.696 |          0.414 |          0.597 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |

- **F_clut: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_objall: success drop 0.240 absolute, 26.1% relative · SPL drop 0.150 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.454 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **R3: success drop 0.640 absolute, 69.6% relative · SPL drop 0.414 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
