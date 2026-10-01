# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.560 |                50.640 |              11.071 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.593 |                57.320 |              10.476 |         25 |              0.040 |              0.048 |         -0.033 |         -0.059 |
| F_clut                                          |          0.880 | 0.578 |                43.240 |              11.633 |         25 |             -0.040 |             -0.048 |         -0.019 |         -0.034 |
| F_obj                                           |          0.720 | 0.506 |                72.760 |               9.683 |         25 |              0.120 |              0.143 |          0.054 |          0.097 |
| F_tgt                                           |          0.840 | 0.597 |                49.560 |              10.916 |         25 |              0.000 |              0.000 |         -0.037 |         -0.066 |
| F_mat                                           |          0.800 | 0.482 |                59.280 |              10.192 |         25 |              0.040 |              0.048 |          0.078 |          0.139 |
| F_light                                         |          0.880 | 0.577 |                43.400 |              11.651 |         25 |             -0.040 |             -0.048 |         -0.017 |         -0.031 |
| F_sky                                           |          0.880 | 0.565 |                42.720 |              11.553 |         25 |             -0.040 |             -0.048 |         -0.006 |         -0.010 |
| B_L1 (materials + lighting)                     |          0.760 | 0.423 |                68.000 |               9.692 |         25 |              0.080 |              0.095 |          0.136 |          0.243 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.292 |               116.480 |               5.899 |         25 |              0.360 |              0.429 |          0.268 |          0.479 |
| B_L2 (+ object appearance)                      |          0.520 | 0.343 |               108.800 |               6.128 |         25 |              0.320 |              0.381 |          0.216 |          0.386 |
| B_L3 (+ distractors)                            |          0.520 | 0.351 |               108.520 |               6.095 |         25 |              0.320 |              0.381 |          0.208 |          0.372 |

- **F_objall: success drop 0.040 absolute, 4.8% relative · SPL drop -0.033 absolute**
- **F_clut: success drop -0.040 absolute, -4.8% relative · SPL drop -0.019 absolute**
- **F_obj: success drop 0.120 absolute, 14.3% relative · SPL drop 0.054 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.037 absolute**
- **F_mat: success drop 0.040 absolute, 4.8% relative · SPL drop 0.078 absolute**
- **F_light: success drop -0.040 absolute, -4.8% relative · SPL drop -0.017 absolute**
- **F_sky: success drop -0.040 absolute, -4.8% relative · SPL drop -0.006 absolute**
- **L1: success drop 0.080 absolute, 9.5% relative · SPL drop 0.136 absolute**
- **L2noT: success drop 0.360 absolute, 42.9% relative · SPL drop 0.268 absolute**
- **L2: success drop 0.320 absolute, 38.1% relative · SPL drop 0.216 absolute**
- **L3: success drop 0.320 absolute, 38.1% relative · SPL drop 0.208 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
