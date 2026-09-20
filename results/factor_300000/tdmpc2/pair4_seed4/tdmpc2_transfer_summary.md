# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.792 |                21.560 |              13.261 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.679 |                41.280 |              11.418 |         25 |              0.120 |              0.120 |          0.113 |          0.143 |
| F_clut                                          |          1.000 | 0.806 |                21.080 |              13.219 |         25 |              0.000 |              0.000 |         -0.014 |         -0.018 |
| F_obj                                           |          0.960 | 0.718 |                30.960 |              12.559 |         25 |              0.040 |              0.040 |          0.074 |          0.093 |
| F_tgt                                           |          1.000 | 0.797 |                19.400 |              13.200 |         25 |              0.000 |              0.000 |         -0.005 |         -0.006 |
| F_mat                                           |          0.760 | 0.485 |                89.120 |               9.036 |         25 |              0.240 |              0.240 |          0.307 |          0.388 |
| F_light                                         |          0.880 | 0.700 |                44.040 |              11.347 |         25 |              0.120 |              0.120 |          0.092 |          0.117 |
| F_sky                                           |          0.920 | 0.721 |                41.240 |              12.005 |         25 |              0.080 |              0.080 |          0.071 |          0.090 |
| B_L1 (materials + lighting)                     |          0.240 | 0.161 |               169.960 |               1.271 |         25 |              0.760 |              0.760 |          0.631 |          0.797 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.024 |               189.080 |              -1.002 |         25 |              0.920 |              0.920 |          0.768 |          0.969 |
| B_L2 (+ object appearance)                      |          0.120 | 0.055 |               182.840 |              -0.219 |         25 |              0.880 |              0.880 |          0.737 |          0.930 |
| B_L3 (+ distractors)                            |          0.080 | 0.050 |               185.520 |              -0.653 |         25 |              0.920 |              0.920 |          0.742 |          0.937 |

- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.113 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.014 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.074 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.307 absolute**
- **F_light: success drop 0.120 absolute, 12.0% relative · SPL drop 0.092 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.071 absolute**
- **L1: success drop 0.760 absolute, 76.0% relative · SPL drop 0.631 absolute**
- **L2noT: success drop 0.920 absolute, 92.0% relative · SPL drop 0.768 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.737 absolute**
- **L3: success drop 0.920 absolute, 92.0% relative · SPL drop 0.742 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
