# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.805 |                20.200 |              13.204 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.478 |                90.920 |               8.822 |         25 |              0.280 |              0.280 |          0.327 |          0.407 |
| B_L2 (+ object appearance)  |          0.600 | 0.339 |               121.040 |               6.958 |         25 |              0.400 |              0.400 |          0.466 |          0.579 |
| B_L3 (+ distractors)        |          0.480 | 0.236 |               145.800 |               5.040 |         25 |              0.520 |              0.520 |          0.569 |          0.706 |

- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.327 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.466 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.569 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
