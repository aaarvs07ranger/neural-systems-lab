# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.679 |                16.600 |              10.789 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.639 |                41.800 |              10.519 |         25 |              0.000 |              0.000 |          0.039 |          0.058 |
| B_L2 (+ object appearance)  |          0.560 | 0.433 |               113.040 |               4.813 |         25 |              0.440 |              0.440 |          0.246 |          0.362 |
| B_L3 (+ distractors)        |          0.880 | 0.585 |                61.760 |               8.965 |         25 |              0.120 |              0.120 |          0.093 |          0.138 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.039 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.246 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.093 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
