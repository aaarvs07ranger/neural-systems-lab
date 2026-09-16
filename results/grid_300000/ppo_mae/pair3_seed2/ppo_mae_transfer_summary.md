# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.660 |                41.240 |              10.807 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.160 | 0.103 |               169.880 |               0.200 |         25 |              0.720 |              0.818 |          0.557 |          0.843 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.082 |               178.080 |              -0.250 |         25 |              0.760 |              0.864 |          0.578 |          0.876 |
| B_L2 (+ object appearance)                      |          0.040 | 0.016 |               192.240 |              -1.503 |         25 |              0.840 |              0.955 |          0.644 |          0.976 |
| B_L3 (+ distractors)                            |          0.040 | 0.016 |               192.240 |              -1.503 |         25 |              0.840 |              0.955 |          0.644 |          0.976 |

- **L1: success drop 0.720 absolute, 81.8% relative · SPL drop 0.557 absolute**
- **L2noT: success drop 0.760 absolute, 86.4% relative · SPL drop 0.578 absolute**
- **L2: success drop 0.840 absolute, 95.5% relative · SPL drop 0.644 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.644 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
