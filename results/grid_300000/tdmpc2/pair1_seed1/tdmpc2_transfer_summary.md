# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.713 |                 9.240 |              10.844 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.507 |               106.240 |               5.335 |         25 |              0.400 |              0.400 |          0.205 |          0.288 |
| B_L2 (+ object appearance)  |          0.720 | 0.512 |                95.040 |               6.702 |         25 |              0.280 |              0.280 |          0.201 |          0.282 |
| B_L3 (+ distractors)        |          0.600 | 0.388 |               117.600 |               5.138 |         25 |              0.400 |              0.400 |          0.325 |          0.456 |

- **L1: success drop 0.400 absolute, 40.0% relative · SPL drop 0.205 absolute**
- **L2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.201 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.325 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
