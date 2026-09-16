# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.590 |                56.080 |              10.400 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.477 |                83.480 |               7.611 |         25 |              0.160 |              0.200 |          0.114 |          0.193 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.477 |                77.520 |               7.943 |         25 |              0.120 |              0.150 |          0.113 |          0.192 |
| B_L2 (+ object appearance)                      |          0.640 | 0.469 |                83.600 |               7.371 |         25 |              0.160 |              0.200 |          0.122 |          0.206 |
| B_L3 (+ distractors)                            |          0.640 | 0.469 |                83.600 |               7.371 |         25 |              0.160 |              0.200 |          0.122 |          0.206 |

- **L1: success drop 0.160 absolute, 20.0% relative · SPL drop 0.114 absolute**
- **L2noT: success drop 0.120 absolute, 15.0% relative · SPL drop 0.113 absolute**
- **L2: success drop 0.160 absolute, 20.0% relative · SPL drop 0.122 absolute**
- **L3: success drop 0.160 absolute, 20.0% relative · SPL drop 0.122 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
