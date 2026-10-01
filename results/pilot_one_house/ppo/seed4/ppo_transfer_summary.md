# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.880 | 0.605 |                33.680 |              10.096 |         25 |
| B (zero-shot visuals) |          0.440 | 0.343 |               115.520 |               4.093 |         25 |

- **Success-rate drop (A - B): 0.440 absolute, 50.0% relative**
- **SPL drop (A - B): 0.262 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
