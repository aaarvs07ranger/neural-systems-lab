# PPO zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.920 | 0.666 |                26.960 |              10.514 |         25 |
| B (zero-shot visuals) |          0.880 | 0.621 |                34.280 |              10.029 |         25 |

- **Success-rate drop (A - B): 0.040 absolute, 4.3% relative**
- **SPL drop (A - B): 0.045 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
