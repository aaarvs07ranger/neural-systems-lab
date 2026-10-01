# PPO_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.607 |                49.800 |              10.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.607 |                49.800 |              10.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.760 | 0.550 |                62.880 |               9.259 |         25 |              0.080 |              0.095 |          0.058 |          0.095 |
| F_objall             |          0.840 | 0.618 |                49.800 |              10.533 |         25 |              0.000 |              0.000 |         -0.011 |         -0.018 |
| F_mat                |          0.040 | 0.040 |               192.160 |              -0.747 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| R2                   |          0.800 | 0.579 |                56.440 |               9.881 |         25 |              0.040 |              0.048 |          0.028 |          0.047 |
| R3                   |          0.760 | 0.575 |                62.840 |               9.459 |         25 |              0.080 |              0.095 |          0.032 |          0.053 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.160 |              -0.738 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 9.5% relative · SPL drop 0.058 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.011 absolute**
- **F_mat: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **R2: success drop 0.040 absolute, 4.8% relative · SPL drop 0.028 absolute**
- **R3: success drop 0.080 absolute, 9.5% relative · SPL drop 0.032 absolute**
- **L3: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
