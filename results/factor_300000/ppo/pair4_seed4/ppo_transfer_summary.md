# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.599 |                37.560 |              12.652 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.680 | 0.466 |                78.120 |               9.339 |         25 |              0.240 |              0.261 |          0.133 |          0.222 |
| F_clut                                          |          0.920 | 0.599 |                37.560 |              12.652 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.680 | 0.441 |                78.800 |               9.423 |         25 |              0.240 |              0.261 |          0.158 |          0.264 |
| F_tgt                                           |          0.920 | 0.638 |                36.520 |              12.497 |         25 |              0.000 |              0.000 |         -0.039 |         -0.066 |
| F_mat                                           |          0.880 | 0.510 |                48.360 |              11.851 |         25 |              0.040 |              0.043 |          0.089 |          0.149 |
| F_light                                         |          0.960 | 0.612 |                29.760 |              13.151 |         25 |             -0.040 |             -0.043 |         -0.013 |         -0.022 |
| F_sky                                           |          0.880 | 0.578 |                44.640 |              12.171 |         25 |              0.040 |              0.043 |          0.021 |          0.035 |
| B_L1 (materials + lighting)                     |          0.720 | 0.416 |                73.360 |               9.455 |         25 |              0.200 |              0.217 |          0.183 |          0.306 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.216 |               138.000 |               4.857 |         25 |              0.560 |              0.609 |          0.383 |          0.640 |
| B_L2 (+ object appearance)                      |          0.520 | 0.341 |               107.240 |               6.536 |         25 |              0.400 |              0.435 |          0.258 |          0.430 |
| B_L3 (+ distractors)                            |          0.560 | 0.364 |               100.640 |               7.163 |         25 |              0.360 |              0.391 |          0.235 |          0.393 |

- **F_objall: success drop 0.240 absolute, 26.1% relative · SPL drop 0.133 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.240 absolute, 26.1% relative · SPL drop 0.158 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.039 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.089 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.013 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.021 absolute**
- **L1: success drop 0.200 absolute, 21.7% relative · SPL drop 0.183 absolute**
- **L2noT: success drop 0.560 absolute, 60.9% relative · SPL drop 0.383 absolute**
- **L2: success drop 0.400 absolute, 43.5% relative · SPL drop 0.258 absolute**
- **L3: success drop 0.360 absolute, 39.1% relative · SPL drop 0.235 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
