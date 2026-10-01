# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                17.960 |              10.971 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.711 |                32.320 |              10.528 |         25 |              0.040 |              0.042 |          0.072 |          0.092 |
| F_clut                                          |          0.960 | 0.789 |                17.840 |              10.950 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_obj                                           |          1.000 | 0.807 |                17.920 |              11.521 |         25 |             -0.040 |             -0.042 |         -0.024 |         -0.030 |
| F_tgt                                           |          0.960 | 0.786 |                18.240 |              10.956 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_mat                                           |          0.960 | 0.772 |                18.800 |              10.960 |         25 |              0.000 |              0.000 |          0.011 |          0.014 |
| F_light                                         |          0.960 | 0.786 |                18.920 |              10.956 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_sky                                           |          0.960 | 0.783 |                18.400 |              10.962 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L1 (materials + lighting)                     |          0.920 | 0.754 |                29.880 |              10.416 |         25 |              0.040 |              0.042 |          0.030 |          0.038 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.719 |                32.520 |              10.512 |         25 |              0.040 |              0.042 |          0.064 |          0.082 |
| B_L2 (+ object appearance)                      |          1.000 | 0.751 |                49.920 |              11.182 |         25 |             -0.040 |             -0.042 |          0.033 |          0.042 |
| B_L3 (+ distractors)                            |          0.840 | 0.657 |                50.240 |               9.446 |         25 |              0.120 |              0.125 |          0.126 |          0.161 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.072 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_obj: success drop -0.040 absolute, -4.2% relative · SPL drop -0.024 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.030 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.064 absolute**
- **L2: success drop -0.040 absolute, -4.2% relative · SPL drop 0.033 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.126 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
