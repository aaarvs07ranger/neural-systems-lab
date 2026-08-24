# PPO_AUG zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.920 | 0.638 |                27.400 |              10.574 |         25 |
| B (zero-shot visuals) |          0.960 | 0.652 |                20.440 |              11.064 |         25 |

- **Success-rate drop (A - B): -0.040 absolute, -4.3% relative**
- **SPL drop (A - B): -0.014 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
