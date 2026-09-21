# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.659 |                29.520 |               9.285 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.698 |                22.040 |               9.753 |         25 |             -0.040 |             -0.045 |         -0.039 |         -0.059 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.578 |                45.520 |               8.307 |         25 |              0.080 |              0.091 |          0.081 |          0.123 |
| B_L2 (+ object appearance)                      |          0.800 | 0.578 |                45.520 |               8.307 |         25 |              0.080 |              0.091 |          0.081 |          0.123 |
| B_L3 (+ distractors)                            |          0.840 | 0.618 |                38.240 |               8.790 |         25 |              0.040 |              0.045 |          0.041 |          0.062 |

- **L1: success drop -0.040 absolute, -4.5% relative · SPL drop -0.039 absolute**
- **L2noT: success drop 0.080 absolute, 9.1% relative · SPL drop 0.081 absolute**
- **L2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.081 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.041 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
