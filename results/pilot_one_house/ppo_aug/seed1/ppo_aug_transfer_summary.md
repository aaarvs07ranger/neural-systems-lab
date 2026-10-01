# PPO_AUG zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.840 | 0.591 |                43.240 |               9.451 |         25 |
| B (zero-shot visuals) |          0.400 | 0.273 |               125.640 |               3.351 |         25 |

- **Success-rate drop (A - B): 0.440 absolute, 52.4% relative**
- **SPL drop (A - B): 0.318 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
