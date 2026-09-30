# PPO_AUG zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.777 |                 7.440 |              10.698 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                 7.440 |              10.698 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.697 |                23.120 |               9.733 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| F_objall             |          0.880 | 0.658 |                30.600 |               9.262 |         25 |              0.120 |              0.120 |          0.118 |          0.152 |
| F_mat                |          0.880 | 0.657 |                30.520 |               9.256 |         25 |              0.120 |              0.120 |          0.120 |          0.154 |
| R2                   |          0.920 | 0.697 |                23.120 |               9.733 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| R3                   |          0.880 | 0.659 |                30.440 |               9.249 |         25 |              0.120 |              0.120 |          0.118 |          0.152 |
| B_L3 (+ distractors) |          0.880 | 0.657 |                30.520 |               9.256 |         25 |              0.120 |              0.120 |          0.120 |          0.154 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.118 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **R3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.118 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
