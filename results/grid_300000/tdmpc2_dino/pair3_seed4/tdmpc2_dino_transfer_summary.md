# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.761 |                19.480 |              12.586 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.596 |                84.640 |               9.225 |         25 |              0.200 |              0.200 |          0.165 |          0.217 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.526 |                89.640 |               8.195 |         25 |              0.280 |              0.280 |          0.235 |          0.308 |
| B_L2 (+ object appearance)                      |          0.520 | 0.434 |               134.240 |               5.432 |         25 |              0.480 |              0.480 |          0.327 |          0.430 |
| B_L3 (+ distractors)                            |          0.400 | 0.285 |               144.120 |               4.024 |         25 |              0.600 |              0.600 |          0.476 |          0.626 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.165 absolute**
- **L2noT: success drop 0.280 absolute, 28.0% relative · SPL drop 0.235 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.327 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.476 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
