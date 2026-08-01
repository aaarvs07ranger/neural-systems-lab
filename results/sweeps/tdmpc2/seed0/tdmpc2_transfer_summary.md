# TDMPC2 zero-shot visual transfer

| variant               |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |
|:----------------------|---------------:|------:|----------------------:|--------------------:|-----------:|
| A (train visuals)     |          1.000 | 0.729 |                16.600 |              11.575 |         25 |
| B (zero-shot visuals) |          0.800 | 0.440 |                85.440 |               8.559 |         25 |

- **Success-rate drop (A - B): 0.200 absolute, 20.0% relative**
- **SPL drop (A - B): 0.289 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
