# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.756 |                21.840 |              12.554 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.520 | 0.391 |               113.840 |               5.413 |         25 |              0.480 |              0.480 |          0.365 |          0.483 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.400 | 0.269 |               149.160 |               4.110 |         25 |              0.600 |              0.600 |          0.487 |          0.644 |
| B_L2 (+ object appearance)                      |          0.120 | 0.120 |               183.480 |               0.597 |         25 |              0.880 |              0.880 |          0.636 |          0.841 |
| B_L3 (+ distractors)                            |          0.120 | 0.120 |               179.280 |               0.393 |         25 |              0.880 |              0.880 |          0.636 |          0.841 |

- **L1: success drop 0.480 absolute, 48.0% relative · SPL drop 0.365 absolute**
- **L2noT: success drop 0.600 absolute, 60.0% relative · SPL drop 0.487 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.636 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.636 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
