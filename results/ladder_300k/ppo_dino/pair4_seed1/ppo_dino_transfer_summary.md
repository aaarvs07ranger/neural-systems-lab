# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.737 |                26.320 |              12.557 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.406 |                83.600 |               7.915 |         25 |              0.320 |              0.333 |          0.331 |          0.449 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.392 |                83.760 |               8.130 |         25 |              0.320 |              0.333 |          0.344 |          0.467 |
| B_L2 (+ object appearance)                      |          0.640 | 0.429 |                84.040 |               8.013 |         25 |              0.320 |              0.333 |          0.308 |          0.418 |
| B_L3 (+ distractors)                            |          0.640 | 0.425 |                84.240 |               8.038 |         25 |              0.320 |              0.333 |          0.312 |          0.423 |

- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.331 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.344 absolute**
- **L2: success drop 0.320 absolute, 33.3% relative · SPL drop 0.308 absolute**
- **L3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.312 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
