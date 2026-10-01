# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.775 |                13.600 |              10.654 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.728 |                44.960 |               9.867 |         25 |              0.040 |              0.040 |          0.047 |          0.061 |
| B_L2 (+ object appearance)  |          1.000 | 0.766 |                42.080 |              10.346 |         25 |              0.000 |              0.000 |          0.009 |          0.012 |
| B_L3 (+ distractors)        |          1.000 | 0.772 |                32.000 |              10.452 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.047 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
