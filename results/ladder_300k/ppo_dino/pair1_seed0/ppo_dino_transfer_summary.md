# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.720 |                 6.520 |              10.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.670 |                14.760 |              10.416 |         25 |              0.040 |              0.040 |          0.050 |          0.070 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.670 |                14.800 |              10.404 |         25 |              0.040 |              0.040 |          0.049 |          0.069 |
| B_L2 (+ object appearance)                      |          0.920 | 0.628 |                22.640 |               9.932 |         25 |              0.080 |              0.080 |          0.091 |          0.127 |
| B_L3 (+ distractors)                            |          0.880 | 0.589 |                30.400 |               9.414 |         25 |              0.120 |              0.120 |          0.131 |          0.182 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.050 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.049 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.091 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.131 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
