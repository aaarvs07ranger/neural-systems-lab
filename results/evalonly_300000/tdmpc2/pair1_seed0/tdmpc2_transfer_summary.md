# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.712 |                 8.160 |              10.856 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.492 |               115.360 |               5.670 |         25 |              0.360 |              0.360 |          0.221 |          0.310 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.652 |                77.160 |               8.763 |         25 |              0.120 |              0.120 |          0.060 |          0.084 |
| B_L2 (+ object appearance)                      |          0.680 | 0.498 |               117.880 |               6.226 |         25 |              0.320 |              0.320 |          0.215 |          0.301 |
| B_L3 (+ distractors)                            |          0.720 | 0.505 |                96.560 |               6.886 |         25 |              0.280 |              0.280 |          0.207 |          0.291 |

- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.221 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.060 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.215 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.207 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
