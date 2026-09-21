# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.682 |                29.000 |               9.346 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.650 |                22.440 |               9.863 |         25 |             -0.040 |             -0.045 |          0.032 |          0.047 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.647 |                22.720 |               9.869 |         25 |             -0.040 |             -0.045 |          0.035 |          0.051 |
| B_L2 (+ object appearance)                      |          0.880 | 0.604 |                30.880 |               9.412 |         25 |              0.000 |              0.000 |          0.078 |          0.114 |
| B_L3 (+ distractors)                            |          0.880 | 0.604 |                30.360 |               9.395 |         25 |              0.000 |              0.000 |          0.078 |          0.114 |

- **L1: success drop -0.040 absolute, -4.5% relative · SPL drop 0.032 absolute**
- **L2noT: success drop -0.040 absolute, -4.5% relative · SPL drop 0.035 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.078 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.078 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
