# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.780 |                17.520 |              10.971 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.709 |                32.600 |               9.865 |         25 |              0.080 |              0.083 |          0.072 |          0.092 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.509 |                70.800 |               7.347 |         25 |              0.280 |              0.292 |          0.272 |          0.348 |
| B_L2 (+ object appearance)                      |          0.400 | 0.315 |               124.280 |               3.652 |         25 |              0.560 |              0.583 |          0.465 |          0.596 |
| B_L3 (+ distractors)                            |          0.400 | 0.329 |               123.680 |               3.541 |         25 |              0.560 |              0.583 |          0.452 |          0.579 |

- **L1: success drop 0.080 absolute, 8.3% relative · SPL drop 0.072 absolute**
- **L2noT: success drop 0.280 absolute, 29.2% relative · SPL drop 0.272 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.465 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.452 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
