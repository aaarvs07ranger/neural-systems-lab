# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.960 | 0.646 |                35.320 |              10.949 |         25 |
| B (zero-shot visuals) |          0.880 | 0.562 |                54.280 |               9.933 |         25 |

- **Success-rate drop (A - B): 0.080 absolute, 8.3% relative**
- **SPL drop (A - B): 0.084 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
