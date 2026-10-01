# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.752 |                13.600 |              10.960 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.520 | 0.416 |               114.160 |               4.743 |         25 |              0.480 |              0.480 |          0.337 |          0.447 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.552 |                78.640 |               6.715 |         25 |              0.320 |              0.320 |          0.200 |          0.266 |
| B_L2 (+ object appearance)                      |          0.680 | 0.513 |                87.400 |               6.662 |         25 |              0.320 |              0.320 |          0.239 |          0.317 |
| B_L3 (+ distractors)                            |          0.640 | 0.510 |                87.000 |               6.235 |         25 |              0.360 |              0.360 |          0.242 |          0.322 |

- **L1: success drop 0.480 absolute, 48.0% relative · SPL drop 0.337 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.200 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.239 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.242 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
