# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.780 |                17.520 |              10.971 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.497 |                79.040 |               6.966 |         25 |              0.320 |              0.333 |          0.284 |          0.364 |
| F_clut                                          |          0.960 | 0.780 |                17.520 |              10.971 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.608 |                48.920 |               8.959 |         25 |              0.160 |              0.167 |          0.173 |          0.221 |
| F_tgt                                           |          0.840 | 0.708 |                40.160 |               9.495 |         25 |              0.120 |              0.125 |          0.073 |          0.093 |
| F_mat                                           |          0.960 | 0.780 |                17.600 |              10.987 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_light                                         |          0.960 | 0.777 |                17.640 |              10.979 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_sky                                           |          0.960 | 0.767 |                17.760 |              10.965 |         25 |              0.000 |              0.000 |          0.013 |          0.017 |
| B_L1 (materials + lighting)                     |          0.880 | 0.714 |                32.520 |               9.871 |         25 |              0.080 |              0.083 |          0.067 |          0.085 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.513 |                70.720 |               7.354 |         25 |              0.280 |              0.292 |          0.267 |          0.343 |
| B_L2 (+ object appearance)                      |          0.360 | 0.288 |               131.120 |               3.076 |         25 |              0.600 |              0.625 |          0.493 |          0.631 |
| B_L3 (+ distractors)                            |          0.360 | 0.299 |               130.520 |               2.923 |         25 |              0.600 |              0.625 |          0.482 |          0.617 |

- **F_objall: success drop 0.320 absolute, 33.3% relative · SPL drop 0.284 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.160 absolute, 16.7% relative · SPL drop 0.173 absolute**
- **F_tgt: success drop 0.120 absolute, 12.5% relative · SPL drop 0.073 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **L1: success drop 0.080 absolute, 8.3% relative · SPL drop 0.067 absolute**
- **L2noT: success drop 0.280 absolute, 29.2% relative · SPL drop 0.267 absolute**
- **L2: success drop 0.600 absolute, 62.5% relative · SPL drop 0.493 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.482 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
