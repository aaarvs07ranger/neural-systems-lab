# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.784 |                19.960 |              13.254 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.587 |                81.320 |              11.139 |         25 |              0.120 |              0.120 |          0.196 |          0.251 |
| B_L2 (+ object appearance)  |          0.760 | 0.466 |                94.560 |               8.984 |         25 |              0.240 |              0.240 |          0.318 |          0.405 |
| B_L3 (+ distractors)        |          0.720 | 0.425 |               115.240 |               8.437 |         25 |              0.280 |              0.280 |          0.359 |          0.458 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.196 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.318 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.359 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
