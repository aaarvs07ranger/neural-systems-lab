# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.744 |                17.720 |              11.530 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.749 |                15.720 |              11.521 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_clut                                          |          1.000 | 0.779 |                16.600 |              11.534 |         25 |              0.000 |              0.000 |         -0.035 |         -0.047 |
| F_obj                                           |          1.000 | 0.751 |                17.120 |              11.554 |         25 |              0.000 |              0.000 |         -0.007 |         -0.010 |
| F_tgt                                           |          1.000 | 0.775 |                15.040 |              11.517 |         25 |              0.000 |              0.000 |         -0.031 |         -0.042 |
| F_mat                                           |          1.000 | 0.686 |                40.040 |              11.300 |         25 |              0.000 |              0.000 |          0.058 |          0.078 |
| F_light                                         |          1.000 | 0.761 |                16.760 |              11.534 |         25 |              0.000 |              0.000 |         -0.017 |         -0.023 |
| F_sky                                           |          0.800 | 0.593 |                64.120 |               8.396 |         25 |              0.200 |              0.200 |          0.151 |          0.203 |
| B_L1 (materials + lighting)                     |          0.840 | 0.561 |                58.720 |               9.201 |         25 |              0.160 |              0.160 |          0.184 |          0.247 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.564 |                65.440 |              10.069 |         25 |              0.080 |              0.080 |          0.180 |          0.242 |
| B_L2 (+ object appearance)                      |          0.840 | 0.493 |                75.800 |               9.066 |         25 |              0.160 |              0.160 |          0.251 |          0.338 |
| B_L3 (+ distractors)                            |          0.920 | 0.579 |                74.280 |              10.068 |         25 |              0.080 |              0.080 |          0.165 |          0.222 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.035 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.031 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.058 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.017 absolute**
- **F_sky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.151 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.184 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.180 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.251 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.165 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
