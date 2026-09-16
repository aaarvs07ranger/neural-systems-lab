# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.770 |                18.280 |              10.960 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.612 |                55.920 |               8.327 |         25 |              0.200 |              0.208 |          0.158 |          0.205 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.513 |                79.560 |               6.946 |         25 |              0.320 |              0.333 |          0.258 |          0.334 |
| B_L2 (+ object appearance)                      |          0.640 | 0.492 |                79.520 |               6.857 |         25 |              0.320 |              0.333 |          0.278 |          0.361 |
| B_L3 (+ distractors)                            |          0.640 | 0.492 |                79.520 |               6.846 |         25 |              0.320 |              0.333 |          0.278 |          0.361 |

- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.158 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.258 absolute**
- **L2: success drop 0.320 absolute, 33.3% relative · SPL drop 0.278 absolute**
- **L3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.278 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
