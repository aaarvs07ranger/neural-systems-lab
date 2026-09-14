# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.514 |                50.880 |              10.985 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.600 | 0.358 |                92.760 |               7.121 |         25 |              0.240 |              0.286 |          0.156 |          0.303 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.187 |               150.680 |               2.586 |         25 |              0.560 |              0.667 |          0.327 |          0.636 |
| B_L2 (+ object appearance)                      |          0.360 | 0.248 |               135.800 |               3.683 |         25 |              0.480 |              0.571 |          0.266 |          0.518 |
| B_L3 (+ distractors)                            |          0.440 | 0.302 |               122.240 |               4.987 |         25 |              0.400 |              0.476 |          0.212 |          0.412 |

- **L1: success drop 0.240 absolute, 28.6% relative · SPL drop 0.156 absolute**
- **L2noT: success drop 0.560 absolute, 66.7% relative · SPL drop 0.327 absolute**
- **L2: success drop 0.480 absolute, 57.1% relative · SPL drop 0.266 absolute**
- **L3: success drop 0.400 absolute, 47.6% relative · SPL drop 0.212 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
