# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.819 |                13.040 |              11.573 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.588 |                82.560 |               7.940 |         25 |              0.240 |              0.240 |          0.230 |          0.281 |
| B_L2 (+ object appearance)  |          0.520 | 0.357 |               130.880 |               4.520 |         25 |              0.480 |              0.480 |          0.462 |          0.564 |
| B_L3 (+ distractors)        |          0.520 | 0.353 |               138.600 |               4.657 |         25 |              0.480 |              0.480 |          0.466 |          0.569 |

- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.230 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.462 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.466 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
