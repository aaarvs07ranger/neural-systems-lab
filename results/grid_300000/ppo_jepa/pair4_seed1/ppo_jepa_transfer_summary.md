# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.706 |                34.440 |              12.091 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.448 |                84.440 |               7.504 |         25 |              0.280 |              0.304 |          0.258 |          0.365 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.182 |               155.160 |               2.552 |         25 |              0.680 |              0.739 |          0.525 |          0.743 |
| B_L2 (+ object appearance)                      |          0.400 | 0.274 |               126.680 |               4.616 |         25 |              0.520 |              0.565 |          0.432 |          0.612 |
| B_L3 (+ distractors)                            |          0.280 | 0.218 |               148.680 |               3.182 |         25 |              0.640 |              0.696 |          0.488 |          0.691 |

- **L1: success drop 0.280 absolute, 30.4% relative · SPL drop 0.258 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.525 absolute**
- **L2: success drop 0.520 absolute, 56.5% relative · SPL drop 0.432 absolute**
- **L3: success drop 0.640 absolute, 69.6% relative · SPL drop 0.488 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
