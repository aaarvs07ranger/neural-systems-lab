# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.785 |                19.760 |              10.951 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.709 |                36.720 |               9.817 |         25 |              0.080 |              0.083 |          0.076 |          0.097 |
| B_L2 (+ object appearance)  |          0.080 | 0.080 |               184.200 |              -0.617 |         25 |              0.880 |              0.917 |          0.705 |          0.898 |
| B_L3 (+ distractors)        |          0.080 | 0.080 |               184.200 |              -0.615 |         25 |              0.880 |              0.917 |          0.705 |          0.898 |

- **L1: success drop 0.080 absolute, 8.3% relative · SPL drop 0.076 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.705 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.705 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
