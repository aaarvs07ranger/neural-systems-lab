# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.240 | 0.192 |               154.480 |               1.622 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.578 |                78.840 |               9.693 |         25 |             -0.720 |             -3.000 |         -0.386 |         -2.004 |
| B_L2 (+ object appearance)  |          0.520 | 0.344 |               121.480 |               4.405 |         25 |             -0.280 |             -1.167 |         -0.151 |         -0.787 |
| B_L3 (+ distractors)        |          0.840 | 0.560 |                77.840 |               8.451 |         25 |             -0.600 |             -2.500 |         -0.367 |         -1.909 |

- **L1: success drop -0.720 absolute, -300.0% relative · SPL drop -0.386 absolute**
- **L2: success drop -0.280 absolute, -116.7% relative · SPL drop -0.151 absolute**
- **L3: success drop -0.600 absolute, -250.0% relative · SPL drop -0.367 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
