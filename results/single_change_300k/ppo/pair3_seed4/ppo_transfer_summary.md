# PPO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.730 |                27.960 |              11.952 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.120 | 0.120 |               177.160 |               1.150 |         25 |              0.840 |              0.875 |          0.610 |          0.836 |
| F_clut                                          |          0.960 | 0.730 |                27.960 |              11.952 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.672 |                40.880 |              10.688 |         25 |              0.080 |              0.083 |          0.058 |          0.079 |
| F_tgt                                           |          0.200 | 0.178 |               162.960 |               2.468 |         25 |              0.760 |              0.792 |          0.552 |          0.756 |
| F_mat                                           |          0.040 | 0.025 |               192.400 |              -1.684 |         25 |              0.920 |              0.958 |          0.705 |          0.966 |
| F_light                                         |          0.960 | 0.730 |                28.040 |              11.947 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.560 | 0.412 |                97.760 |               5.812 |         25 |              0.400 |              0.417 |          0.319 |          0.437 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.672 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.747 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.879 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.879 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |

- **F_objall: success drop 0.840 absolute, 87.5% relative · SPL drop 0.610 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.058 absolute**
- **F_tgt: success drop 0.760 absolute, 79.2% relative · SPL drop 0.552 absolute**
- **F_mat: success drop 0.920 absolute, 95.8% relative · SPL drop 0.705 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.400 absolute, 41.7% relative · SPL drop 0.319 absolute**
- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L2noT: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
