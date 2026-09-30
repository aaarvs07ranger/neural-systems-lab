# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                17.680 |              10.649 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.738 |                19.320 |              10.195 |         25 |              0.040 |              0.040 |          0.039 |          0.050 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.779 |                18.320 |              10.595 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| B_L2 (+ object appearance)                      |          1.000 | 0.776 |                11.840 |              10.671 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L3 (+ distractors)                            |          1.000 | 0.776 |                11.600 |              10.686 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
