# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.647 |                49.240 |              11.096 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.880 | 0.665 |                42.640 |              11.592 |         25 |             -0.040 |             -0.048 |         -0.018 |         -0.028 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.638 |                42.480 |              11.372 |         25 |             -0.040 |             -0.048 |          0.009 |          0.013 |
| B_L2 (+ object appearance)                      |          0.880 | 0.635 |                42.760 |              11.342 |         25 |             -0.040 |             -0.048 |          0.012 |          0.018 |
| B_L3 (+ distractors)                            |          0.880 | 0.638 |                42.680 |              11.345 |         25 |             -0.040 |             -0.048 |          0.009 |          0.014 |

- **L1: success drop -0.040 absolute, -4.8% relative · SPL drop -0.018 absolute**
- **L2noT: success drop -0.040 absolute, -4.8% relative · SPL drop 0.009 absolute**
- **L2: success drop -0.040 absolute, -4.8% relative · SPL drop 0.012 absolute**
- **L3: success drop -0.040 absolute, -4.8% relative · SPL drop 0.009 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
