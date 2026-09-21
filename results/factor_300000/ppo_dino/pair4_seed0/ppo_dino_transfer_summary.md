# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.771 |                21.080 |              13.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.712 |                27.720 |              12.469 |         25 |              0.040 |              0.040 |          0.059 |          0.076 |
| F_clut                                          |          0.960 | 0.746 |                28.480 |              12.716 |         25 |              0.040 |              0.040 |          0.025 |          0.032 |
| F_obj                                           |          0.960 | 0.707 |                27.840 |              12.493 |         25 |              0.040 |              0.040 |          0.064 |          0.082 |
| F_tgt                                           |          0.960 | 0.733 |                28.000 |              12.692 |         25 |              0.040 |              0.040 |          0.038 |          0.049 |
| F_mat                                           |          0.280 | 0.216 |               148.320 |               3.680 |         25 |              0.720 |              0.720 |          0.555 |          0.720 |
| F_light                                         |          1.000 | 0.778 |                20.720 |              13.210 |         25 |              0.000 |              0.000 |         -0.007 |         -0.010 |
| F_sky                                           |          1.000 | 0.765 |                21.200 |              13.197 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| B_L1 (materials + lighting)                     |          0.320 | 0.241 |               140.640 |               4.061 |         25 |              0.680 |              0.680 |          0.530 |          0.688 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.191 |               148.440 |               3.482 |         25 |              0.720 |              0.720 |          0.579 |          0.752 |
| B_L2 (+ object appearance)                      |          0.240 | 0.203 |               156.240 |               3.158 |         25 |              0.760 |              0.760 |          0.568 |          0.737 |
| B_L3 (+ distractors)                            |          0.320 | 0.255 |               142.400 |               4.217 |         25 |              0.680 |              0.680 |          0.516 |          0.669 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.059 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.064 absolute**
- **F_tgt: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.555 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **L1: success drop 0.680 absolute, 68.0% relative · SPL drop 0.530 absolute**
- **L2noT: success drop 0.720 absolute, 72.0% relative · SPL drop 0.579 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.568 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.516 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
