# TDMPC2 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.719 |                20.600 |              11.540 |         25 |
| B (zero-shot visuals) |          1.000 | 0.591 |                52.360 |              11.222 |         25 |

- **Success-rate drop (A - B): 0.000 absolute, 0.0% relative**
- **SPL drop (A - B): 0.128 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
