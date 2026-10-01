# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.711 |                 9.520 |              10.850 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.673 |                19.080 |              10.316 |         25 |              0.040 |              0.040 |          0.038 |          0.054 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.680 |                19.040 |              10.758 |         25 |              0.000 |              0.000 |          0.031 |          0.043 |
| B_L2 (+ object appearance)                      |          0.760 | 0.516 |                65.800 |               7.685 |         25 |              0.240 |              0.240 |          0.195 |          0.274 |
| B_L3 (+ distractors)                            |          1.000 | 0.687 |                15.160 |              10.793 |         25 |              0.000 |              0.000 |          0.024 |          0.034 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.031 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.195 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.024 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
