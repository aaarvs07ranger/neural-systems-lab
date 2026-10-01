# DREAMERV3 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.000 | 0.000 |               200.000 |               0.473 |         25 |              0.000 |                nan |          0.000 |            nan |
| F_clut               |          0.160 | 0.110 |               186.160 |               2.259 |         25 |             -0.160 |                nan |         -0.110 |            nan |
| F_lightsky           |          0.280 | 0.163 |               168.080 |               3.551 |         25 |             -0.280 |                nan |         -0.163 |            nan |
| F_objall             |          0.200 | 0.182 |               183.480 |               2.717 |         25 |             -0.200 |                nan |         -0.182 |            nan |
| F_mat                |          0.080 | 0.059 |               188.080 |              -0.596 |         25 |             -0.080 |                nan |         -0.059 |            nan |
| R2                   |          0.120 | 0.086 |               186.200 |               1.913 |         25 |             -0.120 |                nan |         -0.086 |            nan |
| R3                   |          0.760 | 0.404 |               126.200 |               9.037 |         25 |             -0.760 |                nan |         -0.404 |            nan |
| B_L3 (+ distractors) |          0.080 | 0.080 |               191.880 |              -1.449 |         25 |             -0.080 |                nan |         -0.080 |            nan |

- **F_clut: success drop -0.160 absolute · SPL drop -0.110 absolute**
- **F_lightsky: success drop -0.280 absolute · SPL drop -0.163 absolute**
- **F_objall: success drop -0.200 absolute · SPL drop -0.182 absolute**
- **F_mat: success drop -0.080 absolute · SPL drop -0.059 absolute**
- **R2: success drop -0.120 absolute · SPL drop -0.086 absolute**
- **R3: success drop -0.760 absolute · SPL drop -0.404 absolute**
- **L3: success drop -0.080 absolute · SPL drop -0.080 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
