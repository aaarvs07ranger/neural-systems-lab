# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.578 |                28.880 |              11.416 |         25 |
| B (zero-shot visuals) |          0.960 | 0.491 |                58.200 |              10.753 |         25 |

- **Success-rate drop (A - B): 0.040 absolute, 4.0% relative**
- **SPL drop (A - B): 0.086 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
