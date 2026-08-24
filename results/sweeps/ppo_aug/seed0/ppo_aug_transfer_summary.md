# PPO_AUG zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.880 | 0.586 |                35.040 |              10.008 |         25 |
| B (zero-shot visuals) |          0.840 | 0.519 |                44.200 |               9.491 |         25 |

- **Success-rate drop (A - B): 0.040 absolute, 4.5% relative**
- **SPL drop (A - B): 0.067 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
