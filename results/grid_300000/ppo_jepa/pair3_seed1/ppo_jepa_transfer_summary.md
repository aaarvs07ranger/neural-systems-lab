# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.597 |                55.080 |               9.748 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.315 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.120 |               177.080 |              -0.037 |         25 |              0.680 |              0.850 |          0.477 |          0.799 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -1.273 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -1.139 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |

- **L1: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **L2noT: success drop 0.680 absolute, 85.0% relative · SPL drop 0.477 absolute**
- **L2: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
