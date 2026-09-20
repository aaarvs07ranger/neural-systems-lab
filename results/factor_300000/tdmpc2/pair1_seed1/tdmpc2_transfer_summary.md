# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.716 |                10.320 |              10.827 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.714 |                 8.360 |              10.878 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_clut                                          |          1.000 | 0.712 |                11.560 |              10.808 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_obj                                           |          1.000 | 0.713 |                 7.600 |              10.864 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_tgt                                           |          1.000 | 0.711 |                 8.600 |              10.847 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_mat                                           |          0.560 | 0.439 |               117.560 |               4.447 |         25 |              0.440 |              0.440 |          0.276 |          0.386 |
| F_light                                         |          1.000 | 0.711 |                11.240 |              10.833 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_sky                                           |          1.000 | 0.713 |                 8.920 |              10.844 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| B_L1 (materials + lighting)                     |          0.560 | 0.432 |               101.520 |               4.778 |         25 |              0.440 |              0.440 |          0.284 |          0.397 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.467 |                94.200 |               6.292 |         25 |              0.320 |              0.320 |          0.249 |          0.348 |
| B_L2 (+ object appearance)                      |          0.600 | 0.416 |               109.520 |               5.268 |         25 |              0.400 |              0.400 |          0.299 |          0.418 |
| B_L3 (+ distractors)                            |          0.920 | 0.647 |                65.880 |               9.320 |         25 |              0.080 |              0.080 |          0.069 |          0.096 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_mat: success drop 0.440 absolute, 44.0% relative · SPL drop 0.276 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L1: success drop 0.440 absolute, 44.0% relative · SPL drop 0.284 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.249 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.299 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.069 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
