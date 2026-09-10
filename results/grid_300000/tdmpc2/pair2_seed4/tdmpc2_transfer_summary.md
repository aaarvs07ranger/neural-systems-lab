# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.777 |                10.040 |              10.711 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.775 |                24.360 |              10.515 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L2 (+ object appearance)  |          1.000 | 0.769 |                40.760 |              10.370 |         25 |              0.000 |              0.000 |          0.008 |          0.010 |
| B_L3 (+ distractors)        |          1.000 | 0.768 |                37.040 |              10.428 |         25 |              0.000 |              0.000 |          0.010 |          0.012 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
