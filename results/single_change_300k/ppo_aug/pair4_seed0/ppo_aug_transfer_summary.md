# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.740 |                25.320 |              12.578 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.799 |                18.440 |              13.217 |         25 |             -0.040 |             -0.042 |         -0.059 |         -0.080 |
| F_clut                                          |          0.960 | 0.740 |                25.240 |              12.603 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.774 |                18.600 |              13.258 |         25 |             -0.040 |             -0.042 |         -0.034 |         -0.047 |
| F_tgt                                           |          0.960 | 0.742 |                25.320 |              12.572 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_mat                                           |          0.640 | 0.461 |                82.040 |               7.599 |         25 |              0.320 |              0.333 |          0.279 |          0.377 |
| F_light                                         |          0.960 | 0.740 |                25.320 |              12.574 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          1.000 | 0.767 |                18.720 |              13.256 |         25 |             -0.040 |             -0.042 |         -0.027 |         -0.037 |
| B_L1 (materials + lighting)                     |          0.640 | 0.432 |                82.360 |               7.710 |         25 |              0.320 |              0.333 |          0.307 |          0.416 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.520 | 0.369 |               106.600 |               6.062 |         25 |              0.440 |              0.458 |          0.371 |          0.501 |
| B_L2 (+ object appearance)                      |          0.400 | 0.319 |               125.240 |               4.226 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |
| B_L3 (+ distractors)                            |          0.400 | 0.319 |               125.240 |               4.205 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |

- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.059 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.040 absolute, -4.2% relative · SPL drop -0.034 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.279 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop -0.040 absolute, -4.2% relative · SPL drop -0.027 absolute**
- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.307 absolute**
- **L2noT: success drop 0.440 absolute, 45.8% relative · SPL drop 0.371 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
