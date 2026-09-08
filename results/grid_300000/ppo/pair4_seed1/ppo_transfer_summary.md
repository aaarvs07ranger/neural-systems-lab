# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.661 |                22.880 |              13.758 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.383 |                95.760 |               7.615 |         25 |              0.400 |              0.400 |          0.278 |          0.420 |
| B_L2 (+ object appearance)  |          0.360 | 0.251 |               136.160 |               4.230 |         25 |              0.640 |              0.640 |          0.410 |          0.620 |
| B_L3 (+ distractors)        |          0.280 | 0.195 |               149.920 |               3.166 |         25 |              0.720 |              0.720 |          0.466 |          0.705 |

- **L1: success drop 0.400 absolute, 40.0% relative · SPL drop 0.278 absolute**
- **L2: success drop 0.640 absolute, 64.0% relative · SPL drop 0.410 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.466 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
