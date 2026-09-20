# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.684 |                41.000 |              11.230 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.669 |                41.160 |              11.385 |         25 |              0.000 |              0.000 |          0.015 |          0.022 |
| F_clut                                          |          0.880 | 0.671 |                40.360 |              11.303 |         25 |              0.000 |              0.000 |          0.012 |          0.018 |
| F_obj                                           |          0.880 | 0.671 |                41.160 |              11.379 |         25 |              0.000 |              0.000 |          0.012 |          0.018 |
| F_tgt                                           |          0.880 | 0.691 |                40.800 |              11.198 |         25 |              0.000 |              0.000 |         -0.007 |         -0.010 |
| F_mat                                           |          0.000 | 0.000 |               200.000 |              -1.600 |         25 |              0.880 |              1.000 |          0.684 |          1.000 |
| F_light                                         |          0.880 | 0.677 |                40.840 |              11.229 |         25 |              0.000 |              0.000 |          0.007 |          0.010 |
| F_sky                                           |          0.840 | 0.636 |                47.320 |              10.665 |         25 |              0.040 |              0.045 |          0.047 |          0.069 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.369 |         25 |              0.880 |              1.000 |          0.684 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.054 |         25 |              0.880 |              1.000 |          0.684 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.060 |         25 |              0.880 |              1.000 |          0.684 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.123 |         25 |              0.880 |              1.000 |          0.684 |          1.000 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_mat: success drop 0.880 absolute, 100.0% relative · SPL drop 0.684 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.047 absolute**
- **L1: success drop 0.880 absolute, 100.0% relative · SPL drop 0.684 absolute**
- **L2noT: success drop 0.880 absolute, 100.0% relative · SPL drop 0.684 absolute**
- **L2: success drop 0.880 absolute, 100.0% relative · SPL drop 0.684 absolute**
- **L3: success drop 0.880 absolute, 100.0% relative · SPL drop 0.684 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
