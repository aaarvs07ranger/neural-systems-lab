# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.717 |                29.920 |              12.085 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               194.440 |              -1.647 |         25 |              0.920 |              0.958 |          0.677 |          0.944 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               194.840 |              -1.798 |         25 |              0.920 |              0.958 |          0.677 |          0.944 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.634 |         25 |              0.960 |              1.000 |          0.717 |          1.000 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.480 |              -1.796 |         25 |              0.920 |              0.958 |          0.677 |          0.944 |

- **L1: success drop 0.920 absolute, 95.8% relative · SPL drop 0.677 absolute**
- **L2noT: success drop 0.920 absolute, 95.8% relative · SPL drop 0.677 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.717 absolute**
- **L3: success drop 0.920 absolute, 95.8% relative · SPL drop 0.677 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
