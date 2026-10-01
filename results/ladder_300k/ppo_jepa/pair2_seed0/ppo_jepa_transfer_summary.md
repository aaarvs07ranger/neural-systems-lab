# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.740 |                16.040 |              10.224 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.780 |                 9.080 |              10.709 |         25 |             -0.040 |             -0.042 |         -0.040 |         -0.054 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| B_L2 (+ object appearance)                      |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| B_L3 (+ distractors)                            |          0.920 | 0.700 |                23.680 |               9.717 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |

- **L1: success drop -0.040 absolute, -4.2% relative · SPL drop -0.040 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
