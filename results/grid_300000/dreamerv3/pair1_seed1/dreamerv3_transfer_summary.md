# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.560 | 0.380 |               101.760 |               5.510 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.166 |               165.600 |               2.043 |         25 |              0.280 |              0.500 |          0.214 |          0.564 |
| B_L2 (+ object appearance)  |          0.400 | 0.292 |               148.760 |               3.544 |         25 |              0.160 |              0.286 |          0.088 |          0.231 |
| B_L3 (+ distractors)        |          0.520 | 0.310 |               126.400 |               4.846 |         25 |              0.040 |              0.071 |          0.070 |          0.184 |

- **L1: success drop 0.280 absolute, 50.0% relative · SPL drop 0.214 absolute**
- **L2: success drop 0.160 absolute, 28.6% relative · SPL drop 0.088 absolute**
- **L3: success drop 0.040 absolute, 7.1% relative · SPL drop 0.070 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
