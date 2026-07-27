# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.960 | 0.692 |                21.560 |              11.057 |         25 |
| B (zero-shot visuals) |          0.880 | 0.628 |                35.960 |              10.037 |         25 |

- **Success-rate drop (A - B): 0.080 absolute, 8.3% relative**
- **SPL drop (A - B): 0.064 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
