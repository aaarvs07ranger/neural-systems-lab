# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.801 |                12.840 |              11.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.740 |                22.160 |              11.488 |         25 |              0.000 |              0.000 |          0.062 |          0.077 |
| B_L2 (+ object appearance)  |          1.000 | 0.590 |                51.760 |              11.163 |         25 |              0.000 |              0.000 |          0.211 |          0.263 |
| B_L3 (+ distractors)        |          1.000 | 0.646 |                41.040 |              11.276 |         25 |              0.000 |              0.000 |          0.155 |          0.194 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.062 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.211 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.155 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
