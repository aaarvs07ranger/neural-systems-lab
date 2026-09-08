# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.737 |                27.440 |              10.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.253 |               146.440 |               1.706 |         25 |              0.640 |              0.696 |          0.484 |          0.657 |
| B_L2 (+ object appearance)  |          0.200 | 0.180 |               161.560 |               0.541 |         25 |              0.720 |              0.783 |          0.557 |          0.756 |
| B_L3 (+ distractors)        |          0.200 | 0.180 |               161.560 |               0.485 |         25 |              0.720 |              0.783 |          0.557 |          0.756 |

- **L1: success drop 0.640 absolute, 69.6% relative · SPL drop 0.484 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.557 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
