# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.617 |                49.040 |              10.897 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.616 |                49.080 |              10.853 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_clut                                          |          0.960 | 0.704 |                27.560 |              12.533 |         25 |             -0.120 |             -0.143 |         -0.087 |         -0.141 |
| F_obj                                           |          0.800 | 0.595 |                55.920 |              10.362 |         25 |              0.040 |              0.048 |          0.022 |          0.036 |
| F_tgt                                           |          0.840 | 0.620 |                48.920 |              10.884 |         25 |              0.000 |              0.000 |         -0.002 |         -0.004 |
| F_mat                                           |          0.600 | 0.414 |                91.120 |               7.114 |         25 |              0.240 |              0.286 |          0.203 |          0.330 |
| F_light                                         |          0.840 | 0.611 |                49.200 |              10.903 |         25 |              0.000 |              0.000 |          0.007 |          0.011 |
| F_sky                                           |          0.920 | 0.705 |                33.800 |              11.922 |         25 |             -0.080 |             -0.095 |         -0.088 |         -0.142 |
| B_L1 (materials + lighting)                     |          0.640 | 0.475 |                83.440 |               7.825 |         25 |              0.200 |              0.238 |          0.142 |          0.230 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.480 |                77.320 |               7.939 |         25 |              0.160 |              0.190 |          0.138 |          0.223 |
| B_L2 (+ object appearance)                      |          0.600 | 0.440 |                91.280 |               6.881 |         25 |              0.240 |              0.286 |          0.177 |          0.287 |
| B_L3 (+ distractors)                            |          0.640 | 0.464 |                83.840 |               7.368 |         25 |              0.200 |              0.238 |          0.153 |          0.248 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_clut: success drop -0.120 absolute, -14.3% relative · SPL drop -0.087 absolute**
- **F_obj: success drop 0.040 absolute, 4.8% relative · SPL drop 0.022 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.240 absolute, 28.6% relative · SPL drop 0.203 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_sky: success drop -0.080 absolute, -9.5% relative · SPL drop -0.088 absolute**
- **L1: success drop 0.200 absolute, 23.8% relative · SPL drop 0.142 absolute**
- **L2noT: success drop 0.160 absolute, 19.0% relative · SPL drop 0.138 absolute**
- **L2: success drop 0.240 absolute, 28.6% relative · SPL drop 0.177 absolute**
- **L3: success drop 0.200 absolute, 23.8% relative · SPL drop 0.153 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
