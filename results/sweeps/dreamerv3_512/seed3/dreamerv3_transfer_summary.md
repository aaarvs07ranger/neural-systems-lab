# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.635 |                17.720 |              11.585 |         25 |
| B (zero-shot visuals) |          1.000 | 0.549 |                42.040 |              11.312 |         25 |

- **Success-rate drop (A - B): 0.000 absolute, 0.0% relative**
- **SPL drop (A - B): 0.086 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
