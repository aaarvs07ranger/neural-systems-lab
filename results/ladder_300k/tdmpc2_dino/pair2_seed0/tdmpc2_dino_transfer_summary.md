# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                 9.320 |              10.662 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.776 |                10.160 |              10.660 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.778 |                11.280 |              10.664 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L2 (+ object appearance)                      |          1.000 | 0.779 |                10.600 |              10.676 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| B_L3 (+ distractors)                            |          1.000 | 0.779 |                 9.800 |              10.689 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
