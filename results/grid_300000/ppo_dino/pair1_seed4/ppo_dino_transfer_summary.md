# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.681 |                14.440 |              10.397 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.506 |                53.760 |               7.875 |         25 |              0.200 |              0.208 |          0.175 |          0.257 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.535 |                53.640 |               7.892 |         25 |              0.200 |              0.208 |          0.147 |          0.215 |
| B_L2 (+ object appearance)                      |          0.720 | 0.467 |                61.640 |               7.396 |         25 |              0.240 |              0.250 |          0.214 |          0.315 |
| B_L3 (+ distractors)                            |          0.760 | 0.509 |                53.760 |               7.924 |         25 |              0.200 |              0.208 |          0.172 |          0.252 |

- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.175 absolute**
- **L2noT: success drop 0.200 absolute, 20.8% relative · SPL drop 0.147 absolute**
- **L2: success drop 0.240 absolute, 25.0% relative · SPL drop 0.214 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.172 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
