# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.608 |                55.480 |               9.789 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.280 | 0.169 |               147.960 |               2.177 |         25 |              0.520 |              0.650 |          0.439 |          0.721 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.209 |               140.200 |               2.583 |         25 |              0.480 |              0.600 |          0.399 |          0.656 |
| B_L2 (+ object appearance)                      |          0.120 | 0.069 |               177.160 |              -0.218 |         25 |              0.680 |              0.850 |          0.539 |          0.886 |
| B_L3 (+ distractors)                            |          0.120 | 0.069 |               177.160 |              -0.219 |         25 |              0.680 |              0.850 |          0.539 |          0.886 |

- **L1: success drop 0.520 absolute, 65.0% relative · SPL drop 0.439 absolute**
- **L2noT: success drop 0.480 absolute, 60.0% relative · SPL drop 0.399 absolute**
- **L2: success drop 0.680 absolute, 85.0% relative · SPL drop 0.539 absolute**
- **L3: success drop 0.680 absolute, 85.0% relative · SPL drop 0.539 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
