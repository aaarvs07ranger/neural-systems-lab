# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.880 | 0.625 |                35.160 |               9.998 |         25 |
| B (zero-shot visuals) |          0.840 | 0.602 |                43.320 |               9.462 |         25 |

- **Success-rate drop (A - B): 0.040 absolute, 4.5% relative**
- **SPL drop (A - B): 0.023 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
