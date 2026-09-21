# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.757 |                24.800 |              10.472 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.758 |                25.040 |              10.459 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.712 |                32.560 |               9.859 |         25 |              0.040 |              0.043 |          0.045 |          0.059 |
| B_L2 (+ object appearance)                      |          0.840 | 0.677 |                40.080 |               9.391 |         25 |              0.080 |              0.087 |          0.080 |          0.106 |
| B_L3 (+ distractors)                            |          0.840 | 0.675 |                40.080 |               9.386 |         25 |              0.080 |              0.087 |          0.082 |          0.109 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L2noT: success drop 0.040 absolute, 4.3% relative · SPL drop 0.045 absolute**
- **L2: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **L3: success drop 0.080 absolute, 8.7% relative · SPL drop 0.082 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
