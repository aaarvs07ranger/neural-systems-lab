# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.320 | 0.162 |               163.240 |               5.546 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.411 |                81.880 |              11.677 |         25 |             -0.560 |             -1.750 |         -0.249 |         -1.538 |
| B_L2 (+ object appearance)  |          0.920 | 0.423 |                80.760 |              11.705 |         25 |             -0.600 |             -1.875 |         -0.261 |         -1.614 |
| B_L3 (+ distractors)        |          0.880 | 0.398 |                81.280 |              11.088 |         25 |             -0.560 |             -1.750 |         -0.236 |         -1.457 |

- **L1: success drop -0.560 absolute, -175.0% relative · SPL drop -0.249 absolute**
- **L2: success drop -0.600 absolute, -187.5% relative · SPL drop -0.261 absolute**
- **L3: success drop -0.560 absolute, -175.0% relative · SPL drop -0.236 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
