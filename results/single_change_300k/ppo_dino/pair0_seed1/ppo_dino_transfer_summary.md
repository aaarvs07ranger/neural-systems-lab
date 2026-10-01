# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                17.160 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.610 |                48.560 |               8.868 |         25 |              0.160 |              0.167 |          0.173 |          0.221 |
| F_clut                                          |          0.960 | 0.783 |                17.200 |              10.960 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.880 | 0.676 |                33.240 |               9.885 |         25 |              0.080 |              0.083 |          0.107 |          0.136 |
| F_tgt                                           |          0.960 | 0.773 |                17.440 |              10.963 |         25 |              0.000 |              0.000 |          0.010 |          0.012 |
| F_mat                                           |          0.920 | 0.752 |                24.920 |              10.616 |         25 |              0.040 |              0.042 |          0.031 |          0.040 |
| F_light                                         |          0.960 | 0.779 |                17.280 |              10.961 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_sky                                           |          0.920 | 0.726 |                25.120 |              10.456 |         25 |              0.040 |              0.042 |          0.056 |          0.072 |
| B_L1 (materials + lighting)                     |          0.960 | 0.765 |                17.920 |              11.090 |         25 |              0.000 |              0.000 |          0.018 |          0.023 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.629 |                47.880 |               8.800 |         25 |              0.160 |              0.167 |          0.154 |          0.197 |
| B_L2 (+ object appearance)                      |          0.800 | 0.633 |                47.880 |               8.776 |         25 |              0.160 |              0.167 |          0.150 |          0.192 |
| B_L3 (+ distractors)                            |          0.800 | 0.635 |                47.880 |               8.788 |         25 |              0.160 |              0.167 |          0.148 |          0.189 |

- **F_objall: success drop 0.160 absolute, 16.7% relative · SPL drop 0.173 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.107 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.056 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.018 absolute**
- **L2noT: success drop 0.160 absolute, 16.7% relative · SPL drop 0.154 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.150 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
