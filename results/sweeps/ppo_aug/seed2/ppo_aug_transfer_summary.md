# PPO_AUG zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.960 | 0.604 |                22.360 |              11.020 |         25 |
| B (zero-shot visuals) |          0.840 | 0.459 |                47.840 |               9.412 |         25 |

- **Success-rate drop (A - B): 0.120 absolute, 12.5% relative**
- **SPL drop (A - B): 0.145 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
