# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.651 |                37.240 |               8.792 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.600 | 0.444 |                83.880 |               5.732 |         25 |              0.240 |              0.286 |          0.207 |          0.318 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.484 |                75.960 |               6.248 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |
| B_L2 (+ object appearance)                      |          0.640 | 0.484 |                75.960 |               6.248 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |
| B_L3 (+ distractors)                            |          0.640 | 0.484 |                75.920 |               6.242 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |

- **L1: success drop 0.240 absolute, 28.6% relative · SPL drop 0.207 absolute**
- **L2noT: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **L2: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **L3: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
