# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.760 |                26.320 |              12.528 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.440 | 0.308 |               147.320 |               3.952 |         25 |              0.560 |              0.560 |          0.452 |          0.595 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.160 |               174.040 |               0.475 |         25 |              0.840 |              0.840 |          0.600 |          0.789 |
| B_L2 (+ object appearance)                      |          0.320 | 0.266 |               161.920 |               2.237 |         25 |              0.680 |              0.680 |          0.493 |          0.649 |
| B_L3 (+ distractors)                            |          0.400 | 0.307 |               157.200 |               3.184 |         25 |              0.600 |              0.600 |          0.453 |          0.596 |

- **L1: success drop 0.560 absolute, 56.0% relative · SPL drop 0.452 absolute**
- **L2noT: success drop 0.840 absolute, 84.0% relative · SPL drop 0.600 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.493 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.453 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
