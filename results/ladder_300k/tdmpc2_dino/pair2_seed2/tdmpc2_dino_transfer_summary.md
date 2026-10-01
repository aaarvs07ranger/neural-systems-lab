# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.780 |                 9.000 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.779 |                12.600 |              10.651 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.778 |                12.800 |              10.675 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| B_L2 (+ object appearance)                      |          1.000 | 0.779 |                10.520 |              10.685 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L3 (+ distractors)                            |          1.000 | 0.780 |                14.720 |              10.629 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
