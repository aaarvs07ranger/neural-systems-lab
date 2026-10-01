# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.690 |                33.760 |              11.455 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.360 | 0.219 |               134.520 |               3.590 |         25 |              0.560 |              0.609 |          0.471 |          0.682 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.166 |               148.280 |               2.457 |         25 |              0.640 |              0.696 |          0.524 |          0.759 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.160 |              -0.583 |         25 |              0.880 |              0.957 |          0.650 |          0.942 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.160 |              -0.613 |         25 |              0.880 |              0.957 |          0.650 |          0.942 |

- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.471 absolute**
- **L2noT: success drop 0.640 absolute, 69.6% relative · SPL drop 0.524 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.650 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.650 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
