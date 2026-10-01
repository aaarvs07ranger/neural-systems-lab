# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.528 |                63.440 |              10.500 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.411 |               105.320 |               5.911 |         25 |              0.360 |              0.375 |          0.117 |          0.221 |
| B_L2 (+ object appearance)  |          0.800 | 0.420 |                91.040 |               8.189 |         25 |              0.160 |              0.167 |          0.109 |          0.206 |
| B_L3 (+ distractors)        |          0.720 | 0.466 |                88.280 |               7.224 |         25 |              0.240 |              0.250 |          0.063 |          0.119 |

- **L1: success drop 0.360 absolute, 37.5% relative · SPL drop 0.117 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.109 absolute**
- **L3: success drop 0.240 absolute, 25.0% relative · SPL drop 0.063 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
