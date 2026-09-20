# PPO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.694 |                30.560 |               9.282 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.654 |                38.160 |               8.796 |         25 |              0.040 |              0.045 |          0.040 |          0.058 |
| F_clut                                          |          0.880 | 0.694 |                30.560 |               9.282 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.840 | 0.654 |                38.160 |               8.796 |         25 |              0.040 |              0.045 |          0.040 |          0.058 |
| F_mat                                           |          0.920 | 0.699 |                23.040 |               9.724 |         25 |             -0.040 |             -0.045 |         -0.006 |         -0.008 |
| F_light                                         |          0.760 | 0.574 |                53.600 |               7.836 |         25 |              0.120 |              0.136 |          0.120 |          0.173 |
| F_sky                                           |          0.840 | 0.654 |                38.080 |               8.797 |         25 |              0.040 |              0.045 |          0.040 |          0.058 |
| B_L1 (materials + lighting)                     |          0.840 | 0.654 |                38.120 |               8.762 |         25 |              0.040 |              0.045 |          0.040 |          0.058 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.652 |                38.240 |               8.761 |         25 |              0.040 |              0.045 |          0.042 |          0.060 |
| B_L2 (+ object appearance)                      |          0.840 | 0.652 |                38.240 |               8.761 |         25 |              0.040 |              0.045 |          0.042 |          0.060 |
| B_L3 (+ distractors)                            |          0.840 | 0.652 |                38.240 |               8.761 |         25 |              0.040 |              0.045 |          0.042 |          0.060 |

- **F_objall: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_mat: success drop -0.040 absolute, -4.5% relative · SPL drop -0.006 absolute**
- **F_light: success drop 0.120 absolute, 13.6% relative · SPL drop 0.120 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **L2noT: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**
- **L2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
