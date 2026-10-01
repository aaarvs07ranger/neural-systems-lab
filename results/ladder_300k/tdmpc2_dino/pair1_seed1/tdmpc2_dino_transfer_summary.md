# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.718 |                 8.120 |              10.845 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.671 |                23.480 |              10.262 |         25 |              0.040 |              0.040 |          0.047 |          0.065 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.676 |                23.920 |              10.285 |         25 |              0.040 |              0.040 |          0.043 |          0.059 |
| B_L2 (+ object appearance)                      |          1.000 | 0.698 |                17.400 |              10.795 |         25 |              0.000 |              0.000 |          0.020 |          0.028 |
| B_L3 (+ distractors)                            |          0.920 | 0.639 |                35.520 |               9.676 |         25 |              0.080 |              0.080 |          0.079 |          0.110 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.047 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
