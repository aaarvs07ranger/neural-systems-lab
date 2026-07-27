# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.333 | 0.266 |                38.000 |               3.377 |          3 |
| B (zero-shot visuals) |          0.333 | 0.266 |                38.000 |               3.377 |          3 |

- **Success-rate drop (A - B): 0.000 absolute, 0.0% relative**
- **SPL drop (A - B): 0.000 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
