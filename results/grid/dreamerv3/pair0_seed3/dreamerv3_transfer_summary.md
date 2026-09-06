# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.730 |                20.600 |              11.494 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.592 |                50.080 |              10.680 |         25 |              0.040 |              0.040 |          0.138 |          0.189 |
| B_L2 (+ object appearance)  |          0.880 | 0.484 |                82.520 |               9.507 |         25 |              0.120 |              0.120 |          0.246 |          0.337 |
| B_L3 (+ distractors)        |          0.920 | 0.499 |                83.440 |               9.918 |         25 |              0.080 |              0.080 |          0.231 |          0.317 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.138 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.246 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.231 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
