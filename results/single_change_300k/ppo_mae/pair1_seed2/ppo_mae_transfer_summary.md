# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.695 |                21.760 |               9.908 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.647 |                30.080 |               9.416 |         25 |              0.040 |              0.043 |          0.048 |          0.069 |
| F_clut                                          |          0.920 | 0.699 |                21.720 |               9.897 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_obj                                           |          0.880 | 0.657 |                29.640 |               9.427 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_tgt                                           |          1.000 | 0.721 |                 6.720 |              10.902 |         25 |             -0.080 |             -0.087 |         -0.026 |         -0.038 |
| F_mat                                           |          0.240 | 0.240 |               152.440 |               0.964 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| F_light                                         |          0.880 | 0.657 |                29.440 |               9.403 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_sky                                           |          0.920 | 0.697 |                21.720 |               9.897 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.440 |               0.876 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.440 |               0.876 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.495 |          0.712 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.495 |          0.712 |

- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.048 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_tgt: success drop -0.080 absolute, -8.7% relative · SPL drop -0.026 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **F_light: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.495 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
