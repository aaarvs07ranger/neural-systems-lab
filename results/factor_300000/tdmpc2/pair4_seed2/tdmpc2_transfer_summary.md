# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.768 |                26.800 |              12.626 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.711 |                41.240 |              11.929 |         25 |              0.040 |              0.042 |          0.056 |          0.074 |
| F_clut                                          |          1.000 | 0.806 |                20.040 |              13.233 |         25 |             -0.040 |             -0.042 |         -0.038 |         -0.049 |
| F_obj                                           |          1.000 | 0.784 |                29.920 |              13.135 |         25 |             -0.040 |             -0.042 |         -0.016 |         -0.021 |
| F_tgt                                           |          0.960 | 0.756 |                26.840 |              12.575 |         25 |              0.000 |              0.000 |          0.011 |          0.015 |
| F_mat                                           |          0.920 | 0.660 |                45.320 |              12.012 |         25 |              0.040 |              0.042 |          0.108 |          0.141 |
| F_light                                         |          0.960 | 0.757 |                30.760 |              12.563 |         25 |              0.000 |              0.000 |          0.011 |          0.014 |
| F_sky                                           |          0.960 | 0.770 |                30.120 |              12.555 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| B_L1 (materials + lighting)                     |          0.760 | 0.482 |               107.880 |               9.161 |         25 |              0.200 |              0.208 |          0.286 |          0.372 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.058 |               191.400 |               0.100 |         25 |              0.880 |              0.917 |          0.710 |          0.924 |
| B_L2 (+ object appearance)                      |          0.080 | 0.046 |               186.360 |               0.173 |         25 |              0.880 |              0.917 |          0.722 |          0.940 |
| B_L3 (+ distractors)                            |          0.080 | 0.057 |               192.000 |               0.311 |         25 |              0.880 |              0.917 |          0.711 |          0.926 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.056 absolute**
- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.038 absolute**
- **F_obj: success drop -0.040 absolute, -4.2% relative · SPL drop -0.016 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.108 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.286 absolute**
- **L2noT: success drop 0.880 absolute, 91.7% relative · SPL drop 0.710 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.722 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.711 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
