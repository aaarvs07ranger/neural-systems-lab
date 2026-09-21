# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.714 |                26.920 |              12.098 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.280 | 0.251 |               147.200 |               2.487 |         25 |              0.680 |              0.708 |          0.464 |          0.649 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.251 |               147.240 |               2.465 |         25 |              0.680 |              0.708 |          0.464 |          0.649 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -0.712 |         25 |              0.920 |              0.958 |          0.674 |          0.944 |
| B_L3 (+ distractors)                            |          0.080 | 0.080 |               185.200 |              -0.291 |         25 |              0.880 |              0.917 |          0.634 |          0.888 |

- **L1: success drop 0.680 absolute, 70.8% relative · SPL drop 0.464 absolute**
- **L2noT: success drop 0.680 absolute, 70.8% relative · SPL drop 0.464 absolute**
- **L2: success drop 0.920 absolute, 95.8% relative · SPL drop 0.674 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.634 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
