# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.595 |                46.280 |              12.055 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.572 |                78.880 |              11.932 |         25 |              0.000 |              0.000 |          0.023 |          0.039 |
| B_L2 (+ object appearance)  |          1.000 | 0.614 |                59.560 |              12.882 |         25 |             -0.080 |             -0.087 |         -0.019 |         -0.031 |
| B_L3 (+ distractors)        |          0.880 | 0.525 |                85.680 |              11.388 |         25 |              0.040 |              0.043 |          0.070 |          0.118 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.023 absolute**
- **L2: success drop -0.080 absolute, -8.7% relative · SPL drop -0.019 absolute**
- **L3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.070 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
