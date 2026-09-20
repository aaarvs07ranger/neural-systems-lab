# PPO_AUG zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.689 |                25.680 |               9.855 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_clut                                          |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.684 |                32.400 |               9.377 |         25 |              0.040 |              0.043 |          0.010 |          0.014 |
| F_tgt                                           |          0.960 | 0.699 |                18.320 |              10.365 |         25 |             -0.040 |             -0.043 |         -0.005 |         -0.007 |
| F_mat                                           |          0.360 | 0.243 |               131.360 |               2.356 |         25 |              0.560 |              0.609 |          0.451 |          0.650 |
| F_light                                         |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.480 | 0.363 |               109.040 |               4.127 |         25 |              0.440 |              0.478 |          0.332 |          0.477 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.359 |               108.920 |               4.112 |         25 |              0.440 |              0.478 |          0.335 |          0.482 |
| B_L2 (+ object appearance)                      |          0.440 | 0.376 |               116.720 |               3.477 |         25 |              0.480 |              0.522 |          0.318 |          0.459 |
| B_L3 (+ distractors)                            |          0.400 | 0.369 |               124.040 |               2.950 |         25 |              0.520 |              0.565 |          0.326 |          0.469 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.010 absolute**
- **F_tgt: success drop -0.040 absolute, -4.3% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.560 absolute, 60.9% relative · SPL drop 0.451 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.440 absolute, 47.8% relative · SPL drop 0.332 absolute**
- **L2noT: success drop 0.440 absolute, 47.8% relative · SPL drop 0.335 absolute**
- **L2: success drop 0.480 absolute, 52.2% relative · SPL drop 0.318 absolute**
- **L3: success drop 0.520 absolute, 56.5% relative · SPL drop 0.326 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
