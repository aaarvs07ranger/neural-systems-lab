# PPO_AUG zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.619 |                30.760 |               9.311 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.481 |                76.640 |               6.262 |         25 |              0.240 |              0.273 |          0.139 |          0.224 |
| F_clut                                          |          0.880 | 0.623 |                30.720 |               9.305 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_obj                                           |          0.840 | 0.583 |                38.160 |               8.764 |         25 |              0.040 |              0.045 |          0.036 |          0.058 |
| F_tgt                                           |          0.680 | 0.521 |                69.280 |               6.810 |         25 |              0.200 |              0.227 |          0.099 |          0.159 |
| F_mat                                           |          0.360 | 0.220 |               130.400 |               2.332 |         25 |              0.520 |              0.591 |          0.399 |          0.645 |
| F_light                                         |          0.880 | 0.625 |                30.680 |               9.298 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| F_sky                                           |          0.840 | 0.583 |                38.360 |               8.788 |         25 |              0.040 |              0.045 |          0.036 |          0.058 |
| B_L1 (materials + lighting)                     |          0.200 | 0.146 |               161.000 |               0.264 |         25 |              0.680 |              0.773 |          0.474 |          0.765 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.186 |               153.240 |               0.806 |         25 |              0.640 |              0.727 |          0.434 |          0.700 |
| B_L2 (+ object appearance)                      |          0.200 | 0.174 |               160.640 |               0.331 |         25 |              0.680 |              0.773 |          0.445 |          0.719 |
| B_L3 (+ distractors)                            |          0.200 | 0.151 |               161.120 |               0.273 |         25 |              0.680 |              0.773 |          0.468 |          0.756 |

- **F_objall: success drop 0.240 absolute, 27.3% relative · SPL drop 0.139 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_obj: success drop 0.040 absolute, 4.5% relative · SPL drop 0.036 absolute**
- **F_tgt: success drop 0.200 absolute, 22.7% relative · SPL drop 0.099 absolute**
- **F_mat: success drop 0.520 absolute, 59.1% relative · SPL drop 0.399 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.036 absolute**
- **L1: success drop 0.680 absolute, 77.3% relative · SPL drop 0.474 absolute**
- **L2noT: success drop 0.640 absolute, 72.7% relative · SPL drop 0.434 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.445 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.468 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
