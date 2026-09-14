# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                 9.600 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.775 |                27.720 |              10.502 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.768 |                29.160 |              10.484 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| B_L2 (+ object appearance)                      |          1.000 | 0.770 |                26.200 |              10.503 |         25 |              0.000 |              0.000 |          0.009 |          0.012 |
| B_L3 (+ distractors)                            |          0.960 | 0.723 |                34.680 |               9.991 |         25 |              0.040 |              0.040 |          0.055 |          0.071 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.055 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
