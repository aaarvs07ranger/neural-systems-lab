# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.777 |                 7.680 |              10.697 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.657 |                30.520 |               9.256 |         25 |              0.120 |              0.120 |          0.120 |          0.154 |
| B_L2 (+ object appearance)  |          0.880 | 0.657 |                30.520 |               9.256 |         25 |              0.120 |              0.120 |          0.120 |          0.154 |
| B_L3 (+ distractors)        |          0.880 | 0.657 |                30.520 |               9.256 |         25 |              0.120 |              0.120 |          0.120 |          0.154 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
