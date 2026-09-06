# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.200 | 0.164 |               162.840 |               0.786 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.717 |                49.760 |               9.815 |         25 |             -0.760 |             -3.800 |         -0.553 |         -3.374 |
| B_L2 (+ object appearance)  |          0.840 | 0.586 |                79.840 |               8.243 |         25 |             -0.640 |             -3.200 |         -0.422 |         -2.575 |
| B_L3 (+ distractors)        |          0.720 | 0.539 |                78.840 |               6.976 |         25 |             -0.520 |             -2.600 |         -0.375 |         -2.285 |

- **L1: success drop -0.760 absolute, -380.0% relative · SPL drop -0.553 absolute**
- **L2: success drop -0.640 absolute, -320.0% relative · SPL drop -0.422 absolute**
- **L3: success drop -0.520 absolute, -260.0% relative · SPL drop -0.375 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
