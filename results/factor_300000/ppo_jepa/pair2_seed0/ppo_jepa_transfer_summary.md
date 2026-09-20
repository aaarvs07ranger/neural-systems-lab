# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.740 |                16.000 |              10.221 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.698 |                23.880 |               9.731 |         25 |              0.040 |              0.042 |          0.042 |          0.057 |
| F_clut                                          |          0.960 | 0.740 |                16.000 |              10.221 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.698 |                23.880 |               9.731 |         25 |              0.040 |              0.042 |          0.042 |          0.057 |
| F_mat                                           |          1.000 | 0.780 |                 8.880 |              10.709 |         25 |             -0.040 |             -0.042 |         -0.040 |         -0.054 |
| F_light                                         |          0.960 | 0.740 |                16.040 |              10.223 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.960 | 0.737 |                16.160 |              10.212 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| B_L1 (materials + lighting)                     |          1.000 | 0.780 |                 9.080 |              10.709 |         25 |             -0.040 |             -0.042 |         -0.040 |         -0.054 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| B_L2 (+ object appearance)                      |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| B_L3 (+ distractors)                            |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.042 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.042 absolute**
- **F_mat: success drop -0.040 absolute, -4.2% relative · SPL drop -0.040 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L1: success drop -0.040 absolute, -4.2% relative · SPL drop -0.040 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
