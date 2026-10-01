# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.713 |                 9.800 |              10.844 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.480 | 0.330 |               131.640 |               3.500 |         25 |              0.520 |              0.520 |          0.383 |          0.537 |
| B_L2 (+ object appearance)  |          0.520 | 0.385 |               120.200 |               4.212 |         25 |              0.480 |              0.480 |          0.328 |          0.461 |
| B_L3 (+ distractors)        |          0.400 | 0.365 |               138.680 |               2.740 |         25 |              0.600 |              0.600 |          0.348 |          0.488 |

- **L1: success drop 0.520 absolute, 52.0% relative · SPL drop 0.383 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.328 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.348 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
