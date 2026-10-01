# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                22.600 |               9.747 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.659 |                30.000 |               9.270 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_clut                                          |          0.920 | 0.698 |                22.600 |               9.747 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.659 |                30.000 |               9.270 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_mat                                           |          0.720 | 0.498 |                60.640 |               7.331 |         25 |              0.200 |              0.217 |          0.200 |          0.287 |
| F_light                                         |          0.880 | 0.659 |                29.960 |               9.269 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_sky                                           |          0.880 | 0.659 |                30.240 |               9.264 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| B_L1 (materials + lighting)                     |          0.760 | 0.538 |                52.840 |               7.820 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L2 (+ object appearance)                      |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L3 (+ distractors)                            |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |

- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_mat: success drop 0.200 absolute, 21.7% relative · SPL drop 0.200 absolute**
- **F_light: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **L1: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L2noT: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
