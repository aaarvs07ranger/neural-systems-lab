# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.778 |                10.680 |              10.687 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.681 |                54.640 |               8.996 |         25 |              0.120 |              0.120 |          0.097 |          0.124 |
| B_L2 (+ object appearance)  |          0.840 | 0.596 |                66.200 |               8.476 |         25 |              0.160 |              0.160 |          0.181 |          0.233 |
| B_L3 (+ distractors)        |          0.960 | 0.723 |                50.480 |               9.858 |         25 |              0.040 |              0.040 |          0.055 |          0.071 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.097 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.181 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.055 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
