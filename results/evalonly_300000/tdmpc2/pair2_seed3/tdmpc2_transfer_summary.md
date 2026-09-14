# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                10.760 |              10.700 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.695 |                28.560 |               9.623 |         25 |              0.080 |              0.080 |          0.085 |          0.109 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.734 |                31.320 |              10.016 |         25 |              0.040 |              0.040 |          0.046 |          0.059 |
| B_L2 (+ object appearance)                      |          0.920 | 0.695 |                41.520 |               9.512 |         25 |              0.080 |              0.080 |          0.084 |          0.108 |
| B_L3 (+ distractors)                            |          0.840 | 0.613 |                49.280 |               8.523 |         25 |              0.160 |              0.160 |          0.166 |          0.213 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.085 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.046 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.084 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.166 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
