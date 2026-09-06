# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.756 |                24.600 |              10.509 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.759 |                28.800 |              10.471 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| B_L2 (+ object appearance)  |          1.000 | 0.762 |                25.880 |              10.502 |         25 |              0.000 |              0.000 |         -0.006 |         -0.007 |
| B_L3 (+ distractors)        |          0.960 | 0.724 |                29.560 |              10.057 |         25 |              0.040 |              0.040 |          0.033 |          0.043 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
