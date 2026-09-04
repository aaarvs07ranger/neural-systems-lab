# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.687 |                22.720 |               9.890 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.680 |                31.520 |               9.295 |         25 |              0.040 |              0.043 |          0.007 |          0.011 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.800 |               0.382 |         25 |              0.720 |              0.783 |          0.487 |          0.709 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.800 |               0.382 |         25 |              0.720 |              0.783 |          0.487 |          0.709 |

- **L1: success drop 0.040 absolute, 4.3% relative · SPL drop 0.007 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.487 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.487 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
