# TDMPC2 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.725 |                18.000 |              11.549 |         25 |
| B (zero-shot visuals) |          0.840 | 0.437 |                83.720 |               9.027 |         25 |

- **Success-rate drop (A - B): 0.160 absolute, 16.0% relative**
- **SPL drop (A - B): 0.289 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
