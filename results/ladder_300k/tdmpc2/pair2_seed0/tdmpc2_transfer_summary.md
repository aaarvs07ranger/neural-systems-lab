# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.779 |                11.520 |              10.683 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.771 |                36.200 |              10.414 |         25 |              0.000 |              0.000 |          0.009 |          0.011 |
| B_L2 (+ object appearance)  |          0.960 | 0.725 |                54.120 |               9.801 |         25 |              0.040 |              0.040 |          0.054 |          0.069 |
| B_L3 (+ distractors)        |          0.960 | 0.731 |                50.200 |               9.884 |         25 |              0.040 |              0.040 |          0.048 |          0.062 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.054 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.048 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
