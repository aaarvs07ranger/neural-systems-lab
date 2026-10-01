# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.718 |                 8.400 |              10.847 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.520 | 0.364 |               124.440 |               4.100 |         25 |              0.480 |              0.480 |          0.355 |          0.494 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.517 |                99.600 |               5.867 |         25 |              0.360 |              0.360 |          0.202 |          0.281 |
| B_L2 (+ object appearance)                      |          0.600 | 0.444 |               108.200 |               5.251 |         25 |              0.400 |              0.400 |          0.274 |          0.382 |
| B_L3 (+ distractors)                            |          0.720 | 0.560 |               101.360 |               6.879 |         25 |              0.280 |              0.280 |          0.158 |          0.220 |

- **L1: success drop 0.480 absolute, 48.0% relative · SPL drop 0.355 absolute**
- **L2noT: success drop 0.360 absolute, 36.0% relative · SPL drop 0.202 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.274 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.158 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
