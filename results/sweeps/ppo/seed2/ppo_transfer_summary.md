# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.880 | 0.606 |                34.960 |              10.093 |         25 |
| B (zero-shot visuals) |          0.240 | 0.198 |               153.800 |               1.450 |         25 |

- **Success-rate drop (A - B): 0.640 absolute, 72.7% relative**
- **SPL drop (A - B): 0.408 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
