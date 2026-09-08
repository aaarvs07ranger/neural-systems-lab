# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.806 |                19.560 |              13.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.040 |               192.120 |              -0.844 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.120 |              -1.111 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.120 |              -1.183 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |

- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
