# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.040 | 0.006 |               192.680 |               2.336 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.324 |               106.680 |              10.448 |         25 |             -0.760 |            -19.000 |         -0.318 |        -55.709 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.340 |               117.240 |              10.059 |         25 |             -0.720 |            -18.000 |         -0.334 |        -58.453 |
| B_L2 (+ object appearance)                      |          1.000 | 0.584 |                53.880 |              12.918 |         25 |             -0.960 |            -24.000 |         -0.578 |       -101.142 |
| B_L3 (+ distractors)                            |          0.960 | 0.540 |                59.120 |              12.406 |         25 |             -0.920 |            -23.000 |         -0.535 |        -93.577 |

- **L1: success drop -0.760 absolute, -1900.0% relative · SPL drop -0.318 absolute**
- **L2noT: success drop -0.720 absolute, -1800.0% relative · SPL drop -0.334 absolute**
- **L2: success drop -0.960 absolute, -2400.0% relative · SPL drop -0.578 absolute**
- **L3: success drop -0.920 absolute, -2300.0% relative · SPL drop -0.535 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
