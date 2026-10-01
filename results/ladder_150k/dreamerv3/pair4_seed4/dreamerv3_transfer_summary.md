# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.373 |                68.080 |              11.097 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.501 |                66.520 |              10.412 |         25 |              0.040 |              0.048 |         -0.128 |         -0.343 |
| B_L2 (+ object appearance)  |          0.880 | 0.617 |                58.880 |              11.186 |         25 |             -0.040 |             -0.048 |         -0.244 |         -0.653 |
| B_L3 (+ distractors)        |          0.880 | 0.556 |                69.880 |              11.256 |         25 |             -0.040 |             -0.048 |         -0.183 |         -0.491 |

- **L1: success drop 0.040 absolute, 4.8% relative · SPL drop -0.128 absolute**
- **L2: success drop -0.040 absolute, -4.8% relative · SPL drop -0.244 absolute**
- **L3: success drop -0.040 absolute, -4.8% relative · SPL drop -0.183 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
