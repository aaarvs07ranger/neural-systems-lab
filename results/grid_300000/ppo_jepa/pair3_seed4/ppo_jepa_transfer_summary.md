# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.671 |                42.720 |              10.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.600 | 0.424 |                92.000 |               6.812 |         25 |              0.280 |              0.318 |          0.247 |          0.368 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.470 |                84.600 |               7.288 |         25 |              0.240 |              0.273 |          0.201 |          0.299 |
| B_L2 (+ object appearance)                      |          0.360 | 0.244 |               134.120 |               3.923 |         25 |              0.520 |              0.591 |          0.427 |          0.637 |
| B_L3 (+ distractors)                            |          0.360 | 0.245 |               134.160 |               3.968 |         25 |              0.520 |              0.591 |          0.426 |          0.635 |

- **L1: success drop 0.280 absolute, 31.8% relative · SPL drop 0.247 absolute**
- **L2noT: success drop 0.240 absolute, 27.3% relative · SPL drop 0.201 absolute**
- **L2: success drop 0.520 absolute, 59.1% relative · SPL drop 0.427 absolute**
- **L3: success drop 0.520 absolute, 59.1% relative · SPL drop 0.426 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
