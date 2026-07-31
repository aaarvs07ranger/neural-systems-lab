# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.600 |                22.760 |              11.532 |         25 |
| B (zero-shot visuals) |          1.000 | 0.524 |                39.720 |              11.344 |         25 |

- **Success-rate drop (A - B): 0.000 absolute, 0.0% relative**
- **SPL drop (A - B): 0.076 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
