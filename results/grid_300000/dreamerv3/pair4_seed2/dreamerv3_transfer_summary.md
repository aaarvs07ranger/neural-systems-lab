# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.583 |                25.720 |              13.915 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.473 |                37.840 |              13.252 |         25 |              0.040 |              0.040 |          0.110 |          0.189 |
| B_L2 (+ object appearance)  |          0.880 | 0.447 |                51.440 |              11.882 |         25 |              0.120 |              0.120 |          0.136 |          0.234 |
| B_L3 (+ distractors)        |          0.960 | 0.492 |                39.760 |              12.996 |         25 |              0.040 |              0.040 |          0.091 |          0.156 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.110 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.136 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.091 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
