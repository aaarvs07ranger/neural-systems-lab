# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.759 |                20.440 |              12.574 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.507 |                80.320 |               9.813 |         25 |              0.200 |              0.200 |          0.252 |          0.332 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.490 |                89.640 |               7.670 |         25 |              0.320 |              0.320 |          0.269 |          0.354 |
| B_L2 (+ object appearance)                      |          0.520 | 0.326 |               123.880 |               5.712 |         25 |              0.480 |              0.480 |          0.433 |          0.571 |
| B_L3 (+ distractors)                            |          0.440 | 0.324 |               131.840 |               4.717 |         25 |              0.560 |              0.560 |          0.435 |          0.573 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.252 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.269 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.433 absolute**
- **L3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.435 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
