# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.702 |                20.400 |              11.483 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.652 |                35.240 |              11.345 |         25 |              0.000 |              0.000 |          0.051 |          0.072 |
| B_L2 (+ object appearance)  |          1.000 | 0.628 |                44.080 |              11.220 |         25 |              0.000 |              0.000 |          0.074 |          0.106 |
| B_L3 (+ distractors)        |          1.000 | 0.660 |                36.600 |              11.316 |         25 |              0.000 |              0.000 |          0.043 |          0.061 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.051 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.074 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.043 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
