# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.607 |                49.800 |              10.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -0.728 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.926 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.160 |              -0.893 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.160 |              -0.738 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |

- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L2noT: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L2: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L3: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
