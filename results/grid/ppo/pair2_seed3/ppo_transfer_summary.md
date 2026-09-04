# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.659 |                30.880 |               9.250 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.657 |                30.760 |               9.258 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L2 (+ object appearance)  |          0.880 | 0.657 |                30.680 |               9.250 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L3 (+ distractors)        |          0.880 | 0.657 |                30.680 |               9.250 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
