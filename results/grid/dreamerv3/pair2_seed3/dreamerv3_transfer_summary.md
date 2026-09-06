# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.480 | 0.377 |               119.400 |               4.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.769 |                21.080 |              10.576 |         25 |             -0.520 |             -1.083 |         -0.392 |         -1.042 |
| B_L2 (+ object appearance)  |          1.000 | 0.765 |                28.880 |              10.498 |         25 |             -0.520 |             -1.083 |         -0.389 |         -1.032 |
| B_L3 (+ distractors)        |          1.000 | 0.766 |                28.200 |              10.539 |         25 |             -0.520 |             -1.083 |         -0.390 |         -1.035 |

- **L1: success drop -0.520 absolute, -108.3% relative · SPL drop -0.392 absolute**
- **L2: success drop -0.520 absolute, -108.3% relative · SPL drop -0.389 absolute**
- **L3: success drop -0.520 absolute, -108.3% relative · SPL drop -0.390 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
