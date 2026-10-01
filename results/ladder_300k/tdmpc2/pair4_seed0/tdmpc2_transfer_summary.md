# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.786 |                22.360 |              13.203 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.409 |               102.240 |               8.990 |         25 |              0.240 |              0.240 |          0.377 |          0.480 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.221 |               145.200 |               5.039 |         25 |              0.520 |              0.520 |          0.565 |          0.719 |
| B_L2 (+ object appearance)                      |          0.480 | 0.228 |               141.800 |               4.438 |         25 |              0.520 |              0.520 |          0.558 |          0.710 |
| B_L3 (+ distractors)                            |          0.400 | 0.186 |               146.760 |               3.673 |         25 |              0.600 |              0.600 |          0.600 |          0.764 |

- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.377 absolute**
- **L2noT: success drop 0.520 absolute, 52.0% relative · SPL drop 0.565 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.558 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.600 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
