# DREAMERV3 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.768 |                18.480 |              10.886 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.767 |                14.960 |              10.894 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          1.000 | 0.772 |                18.760 |              10.750 |         25 |              0.000 |              0.000 |         -0.005 |         -0.006 |
| F_objall             |          1.000 | 0.768 |                15.520 |              10.891 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          1.000 | 0.777 |                22.240 |              10.575 |         25 |              0.000 |              0.000 |         -0.010 |         -0.013 |
| R2                   |          1.000 | 0.775 |                19.840 |              10.728 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| R3                   |          1.000 | 0.771 |                16.920 |              10.788 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| B_L3 (+ distractors) |          1.000 | 0.772 |                33.400 |              10.461 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.010 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
