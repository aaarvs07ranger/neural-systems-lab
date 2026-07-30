# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.920 | 0.644 |                27.120 |              10.589 |         25 |
| B (zero-shot visuals) |          0.640 | 0.475 |                79.120 |               6.748 |         25 |

- **Success-rate drop (A - B): 0.280 absolute, 30.4% relative**
- **SPL drop (A - B): 0.168 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
