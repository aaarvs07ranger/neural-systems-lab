# PPO_AUG zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.514 |                50.880 |              10.984 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.720 | 0.437 |                70.720 |               9.226 |         25 |              0.120 |              0.143 |          0.077 |          0.150 |
| F_lightsky           |          0.760 | 0.458 |                64.320 |               9.894 |         25 |              0.080 |              0.095 |          0.056 |          0.108 |
| F_objall             |          0.600 | 0.410 |                93.560 |               7.466 |         25 |              0.240 |              0.286 |          0.104 |          0.202 |
| F_mat                |          0.680 | 0.409 |                79.000 |               8.435 |         25 |              0.160 |              0.190 |          0.104 |          0.203 |
| R2                   |          0.760 | 0.448 |                64.120 |               9.824 |         25 |              0.080 |              0.095 |          0.066 |          0.129 |
| R3                   |          0.520 | 0.359 |               105.600 |               6.199 |         25 |              0.320 |              0.381 |          0.154 |          0.301 |
| B_L3 (+ distractors) |          0.400 | 0.276 |               128.480 |               4.306 |         25 |              0.440 |              0.524 |          0.238 |          0.463 |

- **F_clut: success drop 0.120 absolute, 14.3% relative · SPL drop 0.077 absolute**
- **F_lightsky: success drop 0.080 absolute, 9.5% relative · SPL drop 0.056 absolute**
- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.104 absolute**
- **F_mat: success drop 0.160 absolute, 19.0% relative · SPL drop 0.104 absolute**
- **R2: success drop 0.080 absolute, 9.5% relative · SPL drop 0.066 absolute**
- **R3: success drop 0.320 absolute, 38.1% relative · SPL drop 0.154 absolute**
- **L3: success drop 0.440 absolute, 52.4% relative · SPL drop 0.238 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
