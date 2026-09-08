# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.480 | 0.363 |               109.040 |               4.127 |         25 |              0.440 |              0.478 |          0.332 |          0.477 |
| B_L2 (+ object appearance)  |          0.440 | 0.376 |               116.720 |               3.477 |         25 |              0.480 |              0.522 |          0.318 |          0.459 |
| B_L3 (+ distractors)        |          0.400 | 0.369 |               124.040 |               2.950 |         25 |              0.520 |              0.565 |          0.326 |          0.469 |

- **L1: success drop 0.440 absolute, 47.8% relative · SPL drop 0.332 absolute**
- **L2: success drop 0.480 absolute, 52.2% relative · SPL drop 0.318 absolute**
- **L3: success drop 0.520 absolute, 56.5% relative · SPL drop 0.326 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
