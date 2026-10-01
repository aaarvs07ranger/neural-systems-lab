# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.814 |                20.600 |              13.198 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.680 | 0.458 |               121.800 |               7.783 |         25 |              0.320 |              0.320 |          0.356 |          0.437 |
| B_L2 (+ object appearance)  |          0.120 | 0.083 |               185.400 |               0.725 |         25 |              0.880 |              0.880 |          0.731 |          0.898 |
| B_L3 (+ distractors)        |          0.040 | 0.010 |               192.960 |               0.054 |         25 |              0.960 |              0.960 |          0.804 |          0.988 |

- **L1: success drop 0.320 absolute, 32.0% relative · SPL drop 0.356 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.731 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.804 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
