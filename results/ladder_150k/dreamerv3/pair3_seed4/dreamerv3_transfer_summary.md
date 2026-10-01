# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.536 |                81.880 |              10.298 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.005 |               198.600 |              -1.991 |         25 |              0.800 |              0.952 |          0.531 |          0.991 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -2.529 |         25 |              0.840 |              1.000 |          0.536 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -2.807 |         25 |              0.840 |              1.000 |          0.536 |          1.000 |

- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.531 absolute**
- **L2: success drop 0.840 absolute, 100.0% relative · SPL drop 0.536 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.536 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
