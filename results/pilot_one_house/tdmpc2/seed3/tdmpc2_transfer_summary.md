# TDMPC2 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.726 |                18.120 |              11.542 |         25 |
| B (zero-shot visuals) |          0.880 | 0.598 |                55.600 |               9.804 |         25 |

- **Success-rate drop (A - B): 0.120 absolute, 12.0% relative**
- **SPL drop (A - B): 0.128 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
