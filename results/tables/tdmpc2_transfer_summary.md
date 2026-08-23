# TDMPC2 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.730 |                13.920 |              11.590 |         25 |
| B (zero-shot visuals) |          0.760 | 0.519 |                82.640 |               7.989 |         25 |

- **Success-rate drop (A - B): 0.240 absolute, 24.0% relative**
- **SPL drop (A - B): 0.211 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
