# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.558 |                54.600 |              10.846 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.578 |         25 |              0.800 |              0.952 |          0.518 |          0.928 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -1.297 |         25 |              0.800 |              0.952 |          0.518 |          0.928 |
| B_L2 (+ object appearance)                      |          0.160 | 0.140 |               184.080 |               0.426 |         25 |              0.680 |              0.810 |          0.418 |          0.749 |
| B_L3 (+ distractors)                            |          0.200 | 0.171 |               170.040 |               0.724 |         25 |              0.640 |              0.762 |          0.387 |          0.693 |

- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.518 absolute**
- **L2noT: success drop 0.800 absolute, 95.2% relative · SPL drop 0.518 absolute**
- **L2: success drop 0.680 absolute, 81.0% relative · SPL drop 0.418 absolute**
- **L3: success drop 0.640 absolute, 76.2% relative · SPL drop 0.387 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
