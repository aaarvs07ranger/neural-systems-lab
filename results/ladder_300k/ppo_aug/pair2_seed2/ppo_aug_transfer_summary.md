# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.779 |                 9.680 |              10.674 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.699 |                24.920 |               9.711 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| B_L2 (+ object appearance)  |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |
| B_L3 (+ distractors)        |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
