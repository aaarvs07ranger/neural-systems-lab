# DREAMERV3 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          0.960 | 0.640 |                29.680 |              11.039 |         25 |
| B (zero-shot visuals) |          1.000 | 0.641 |                20.600 |              11.546 |         25 |

- **Success-rate drop (A - B): -0.040 absolute, -4.2% relative**
- **SPL drop (A - B): -0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
