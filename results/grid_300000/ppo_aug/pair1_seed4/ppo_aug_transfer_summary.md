# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.660 |                30.720 |               9.398 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.583 |                57.880 |               7.642 |         25 |              0.120 |              0.136 |          0.077 |          0.116 |
| B_L2 (+ object appearance)  |          0.440 | 0.316 |               116.920 |               3.591 |         25 |              0.440 |              0.500 |          0.344 |          0.522 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.460 |          0.697 |

- **L1: success drop 0.120 absolute, 13.6% relative · SPL drop 0.077 absolute**
- **L2: success drop 0.440 absolute, 50.0% relative · SPL drop 0.344 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.460 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
