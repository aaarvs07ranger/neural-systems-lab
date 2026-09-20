# PPO_AUG zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.730 |                26.800 |              11.973 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.538 |                75.320 |               8.708 |         25 |              0.240 |              0.250 |          0.193 |          0.264 |
| F_clut                                          |          0.960 | 0.730 |                26.800 |              11.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.681 |                39.800 |              10.720 |         25 |              0.080 |              0.083 |          0.049 |          0.067 |
| F_tgt                                           |          0.920 | 0.684 |                36.960 |              11.433 |         25 |              0.040 |              0.042 |          0.047 |          0.064 |
| F_mat                                           |          0.520 | 0.407 |               101.680 |               5.107 |         25 |              0.440 |              0.458 |          0.323 |          0.442 |
| F_light                                         |          0.960 | 0.733 |                26.600 |              11.974 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_sky                                           |          0.920 | 0.709 |                34.040 |              11.362 |         25 |              0.040 |              0.042 |          0.021 |          0.028 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.263 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.275 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.230 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.230 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |

- **F_objall: success drop 0.240 absolute, 25.0% relative · SPL drop 0.193 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.049 absolute**
- **F_tgt: success drop 0.040 absolute, 4.2% relative · SPL drop 0.047 absolute**
- **F_mat: success drop 0.440 absolute, 45.8% relative · SPL drop 0.323 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.021 absolute**
- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L2noT: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
