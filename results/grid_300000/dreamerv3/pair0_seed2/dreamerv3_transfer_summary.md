# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.776 |                13.040 |              11.587 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.740 |                19.360 |              11.524 |         25 |              0.000 |              0.000 |          0.036 |          0.047 |
| B_L2 (+ object appearance)  |          1.000 | 0.631 |                39.040 |              11.294 |         25 |              0.000 |              0.000 |          0.145 |          0.187 |
| B_L3 (+ distractors)        |          1.000 | 0.648 |                32.400 |              11.360 |         25 |              0.000 |              0.000 |          0.128 |          0.165 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.036 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.145 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.128 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
