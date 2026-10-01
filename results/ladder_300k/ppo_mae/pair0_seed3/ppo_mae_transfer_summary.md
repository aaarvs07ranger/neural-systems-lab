# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.686 |                34.520 |              10.000 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.755 |                26.680 |              10.392 |         25 |             -0.040 |             -0.045 |         -0.069 |         -0.100 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.710 |                27.400 |              10.493 |         25 |             -0.040 |             -0.045 |         -0.024 |         -0.035 |
| B_L2 (+ object appearance)                      |          0.800 | 0.642 |                50.440 |               8.909 |         25 |              0.080 |              0.091 |          0.044 |          0.064 |
| B_L3 (+ distractors)                            |          0.800 | 0.642 |                50.440 |               8.909 |         25 |              0.080 |              0.091 |          0.044 |          0.064 |

- **L1: success drop -0.040 absolute, -4.5% relative · SPL drop -0.069 absolute**
- **L2noT: success drop -0.040 absolute, -4.5% relative · SPL drop -0.024 absolute**
- **L2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.044 absolute**
- **L3: success drop 0.080 absolute, 9.1% relative · SPL drop 0.044 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
