# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.712 |                29.400 |              12.058 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.065 |               184.480 |              -1.138 |         25 |              0.880 |              0.917 |          0.647 |          0.909 |
| B_L2 (+ object appearance)  |          0.120 | 0.089 |               177.040 |              -0.568 |         25 |              0.840 |              0.875 |          0.623 |          0.875 |
| B_L3 (+ distractors)        |          0.120 | 0.089 |               177.040 |              -0.568 |         25 |              0.840 |              0.875 |          0.623 |          0.875 |

- **L1: success drop 0.880 absolute, 91.7% relative · SPL drop 0.647 absolute**
- **L2: success drop 0.840 absolute, 87.5% relative · SPL drop 0.623 absolute**
- **L3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.623 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
