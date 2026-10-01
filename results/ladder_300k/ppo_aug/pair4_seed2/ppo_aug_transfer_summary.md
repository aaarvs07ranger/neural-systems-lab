# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.745 |                23.280 |              13.185 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.020 |               192.200 |              -1.584 |         25 |              0.960 |              0.960 |          0.725 |          0.973 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -2.053 |         25 |              1.000 |              1.000 |          0.745 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -2.064 |         25 |              1.000 |              1.000 |          0.745 |          1.000 |

- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.725 absolute**
- **L2: success drop 1.000 absolute, 100.0% relative · SPL drop 0.745 absolute**
- **L3: success drop 1.000 absolute, 100.0% relative · SPL drop 0.745 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
