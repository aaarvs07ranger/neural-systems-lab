# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.752 |                12.760 |              10.921 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.709 |                65.520 |               9.807 |         25 |              0.040 |              0.040 |          0.043 |          0.057 |
| B_L2 (+ object appearance)  |          1.000 | 0.744 |                61.400 |              10.279 |         25 |              0.000 |              0.000 |          0.008 |          0.010 |
| B_L3 (+ distractors)        |          0.960 | 0.753 |                45.200 |              10.005 |         25 |              0.040 |              0.040 |         -0.002 |         -0.002 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
