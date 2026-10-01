# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 9.960 |              10.705 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.725 |                49.920 |               9.845 |         25 |              0.040 |              0.040 |          0.052 |          0.067 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.726 |                48.360 |               9.860 |         25 |              0.040 |              0.040 |          0.051 |          0.066 |
| B_L2 (+ object appearance)                      |          0.920 | 0.723 |                51.880 |               9.424 |         25 |              0.080 |              0.080 |          0.053 |          0.069 |
| B_L3 (+ distractors)                            |          0.880 | 0.643 |                65.040 |               8.875 |         25 |              0.120 |              0.120 |          0.134 |          0.172 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.052 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.051 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.053 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.134 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
