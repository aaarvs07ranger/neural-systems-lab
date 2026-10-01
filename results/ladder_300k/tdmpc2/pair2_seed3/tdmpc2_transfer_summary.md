# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.780 |                12.600 |              10.659 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.739 |                32.680 |              10.011 |         25 |              0.040 |              0.040 |          0.041 |          0.052 |
| B_L2 (+ object appearance)  |          0.960 | 0.735 |                38.360 |               9.970 |         25 |              0.040 |              0.040 |          0.045 |          0.058 |
| B_L3 (+ distractors)        |          1.000 | 0.775 |                39.680 |              10.389 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.045 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
