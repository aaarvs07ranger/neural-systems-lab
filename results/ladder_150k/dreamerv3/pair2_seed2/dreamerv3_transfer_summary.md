# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.751 |                13.960 |              10.959 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.777 |                26.200 |              10.618 |         25 |              0.000 |              0.000 |         -0.026 |         -0.034 |
| B_L2 (+ object appearance)  |          1.000 | 0.776 |                30.400 |              10.570 |         25 |              0.000 |              0.000 |         -0.025 |         -0.033 |
| B_L3 (+ distractors)        |          1.000 | 0.778 |                25.640 |              10.558 |         25 |              0.000 |              0.000 |         -0.027 |         -0.035 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.026 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.025 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.027 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
