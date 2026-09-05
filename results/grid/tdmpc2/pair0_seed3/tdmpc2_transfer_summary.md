# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.819 |                14.840 |              11.570 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.595 |                79.000 |               9.149 |         25 |              0.160 |              0.160 |          0.224 |          0.274 |
| B_L2 (+ object appearance)  |          0.760 | 0.464 |               101.240 |               7.817 |         25 |              0.240 |              0.240 |          0.355 |          0.433 |
| B_L3 (+ distractors)        |          0.840 | 0.527 |                93.040 |               8.954 |         25 |              0.160 |              0.160 |          0.292 |          0.356 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.224 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.355 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.292 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
