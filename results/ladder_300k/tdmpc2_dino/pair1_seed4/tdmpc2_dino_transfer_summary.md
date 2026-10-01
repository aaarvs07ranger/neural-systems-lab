# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.716 |                 7.640 |              10.860 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.684 |                17.000 |              10.362 |         25 |              0.040 |              0.040 |          0.032 |          0.045 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.681 |                20.000 |              10.327 |         25 |              0.040 |              0.040 |          0.036 |          0.050 |
| B_L2 (+ object appearance)                      |          0.960 | 0.666 |                18.920 |              10.328 |         25 |              0.040 |              0.040 |          0.051 |          0.071 |
| B_L3 (+ distractors)                            |          0.920 | 0.656 |                25.480 |               9.828 |         25 |              0.080 |              0.080 |          0.060 |          0.084 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.032 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.051 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.060 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
