# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.520 | 0.407 |               125.640 |               6.628 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.120 |              -2.097 |         25 |              0.480 |              0.923 |          0.367 |          0.902 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -1.929 |         25 |              0.480 |              0.923 |          0.367 |          0.902 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -2.212 |         25 |              0.480 |              0.923 |          0.367 |          0.902 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.774 |         25 |              0.520 |              1.000 |          0.407 |          1.000 |

- **L1: success drop 0.480 absolute, 92.3% relative · SPL drop 0.367 absolute**
- **L2noT: success drop 0.480 absolute, 92.3% relative · SPL drop 0.367 absolute**
- **L2: success drop 0.480 absolute, 92.3% relative · SPL drop 0.367 absolute**
- **L3: success drop 0.520 absolute, 100.0% relative · SPL drop 0.407 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
