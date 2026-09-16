# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.750 |                18.120 |              10.960 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.714 |                25.720 |              10.396 |         25 |              0.040 |              0.042 |          0.036 |          0.048 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.485 |                79.160 |               6.746 |         25 |              0.320 |              0.333 |          0.265 |          0.353 |
| B_L2 (+ object appearance)                      |          0.520 | 0.407 |               102.000 |               5.225 |         25 |              0.440 |              0.458 |          0.343 |          0.457 |
| B_L3 (+ distractors)                            |          0.560 | 0.435 |                95.280 |               5.705 |         25 |              0.400 |              0.417 |          0.315 |          0.420 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.036 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.265 absolute**
- **L2: success drop 0.440 absolute, 45.8% relative · SPL drop 0.343 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.315 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
