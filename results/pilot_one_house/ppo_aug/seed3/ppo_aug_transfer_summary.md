# PPO_AUG zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.880 | 0.631 |                35.320 |              10.054 |         25 |
| B (zero-shot visuals) |          0.360 | 0.269 |               133.280 |               3.011 |         25 |

- **Success-rate drop (A - B): 0.520 absolute, 59.1% relative**
- **SPL drop (A - B): 0.362 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
