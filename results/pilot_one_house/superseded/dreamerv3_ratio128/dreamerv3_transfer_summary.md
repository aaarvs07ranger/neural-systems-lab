# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.440 | 0.177 |               138.320 |               3.145 |         25 |
| B (zero-shot visuals) |          0.360 | 0.162 |               150.480 |               2.201 |         25 |

- **Success-rate drop (A - B): 0.080 absolute, 18.2% relative**
- **SPL drop (A - B): 0.015 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
