# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.780 |                13.960 |              10.633 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.698 |                29.880 |               9.684 |         25 |              0.080 |              0.080 |          0.082 |          0.105 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.699 |                24.400 |               9.729 |         25 |              0.080 |              0.080 |          0.082 |          0.105 |
| B_L2 (+ object appearance)                      |          0.960 | 0.738 |                22.640 |              10.162 |         25 |              0.040 |              0.040 |          0.042 |          0.054 |
| B_L3 (+ distractors)                            |          1.000 | 0.779 |                14.200 |              10.646 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.082 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.082 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
