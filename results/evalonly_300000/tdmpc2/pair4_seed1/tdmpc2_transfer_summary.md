# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.750 |                19.760 |              13.245 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.652 |                62.680 |              11.191 |         25 |              0.120 |              0.120 |          0.097 |          0.130 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.350 |               133.680 |               6.748 |         25 |              0.400 |              0.400 |          0.400 |          0.533 |
| B_L2 (+ object appearance)                      |          0.600 | 0.309 |               125.080 |               6.374 |         25 |              0.400 |              0.400 |          0.440 |          0.588 |
| B_L3 (+ distractors)                            |          0.600 | 0.332 |               133.880 |               6.551 |         25 |              0.400 |              0.400 |          0.418 |          0.557 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.097 absolute**
- **L2noT: success drop 0.400 absolute, 40.0% relative · SPL drop 0.400 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.440 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.418 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
