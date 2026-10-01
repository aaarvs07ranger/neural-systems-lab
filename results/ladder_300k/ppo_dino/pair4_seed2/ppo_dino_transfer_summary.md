# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.766 |                20.320 |              13.234 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.558 |                54.560 |              10.317 |         25 |              0.200 |              0.200 |          0.208 |          0.272 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.613 |                42.160 |              11.348 |         25 |              0.120 |              0.120 |          0.153 |          0.200 |
| B_L2 (+ object appearance)                      |          0.840 | 0.596 |                49.000 |              10.809 |         25 |              0.160 |              0.160 |          0.169 |          0.221 |
| B_L3 (+ distractors)                            |          0.880 | 0.620 |                41.960 |              11.330 |         25 |              0.120 |              0.120 |          0.146 |          0.191 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.208 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.153 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.169 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.146 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
