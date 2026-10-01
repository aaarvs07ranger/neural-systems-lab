# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.440 | 0.267 |               133.960 |               5.265 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -2.230 |         25 |              0.440 |              1.000 |          0.267 |          1.000 |
| B_L2 (+ object appearance)  |          0.240 | 0.193 |               162.440 |               0.728 |         25 |              0.200 |              0.455 |          0.074 |          0.277 |
| B_L3 (+ distractors)        |          0.200 | 0.150 |               171.120 |               0.452 |         25 |              0.240 |              0.545 |          0.117 |          0.437 |

- **L1: success drop 0.440 absolute, 100.0% relative · SPL drop 0.267 absolute**
- **L2: success drop 0.200 absolute, 45.5% relative · SPL drop 0.074 absolute**
- **L3: success drop 0.240 absolute, 54.5% relative · SPL drop 0.117 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
