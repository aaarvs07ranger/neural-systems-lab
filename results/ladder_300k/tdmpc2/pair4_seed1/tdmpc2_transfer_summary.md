# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.745 |                26.520 |              12.576 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.668 |                59.160 |              12.279 |         25 |              0.000 |              0.000 |          0.077 |          0.104 |
| B_L2 (+ object appearance)  |          0.520 | 0.325 |               134.080 |               5.291 |         25 |              0.440 |              0.458 |          0.420 |          0.564 |
| B_L3 (+ distractors)        |          0.480 | 0.289 |               138.720 |               5.145 |         25 |              0.480 |              0.500 |          0.456 |          0.612 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.077 absolute**
- **L2: success drop 0.440 absolute, 45.8% relative · SPL drop 0.420 absolute**
- **L3: success drop 0.480 absolute, 50.0% relative · SPL drop 0.456 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
