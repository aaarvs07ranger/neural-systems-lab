# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.778 |                12.080 |              10.676 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.653 |                48.400 |               9.042 |         25 |              0.120 |              0.120 |          0.124 |          0.160 |
| B_L2 (+ object appearance)  |          0.960 | 0.769 |                40.480 |               9.944 |         25 |              0.040 |              0.040 |          0.009 |          0.012 |
| B_L3 (+ distractors)        |          0.920 | 0.697 |                38.880 |               9.566 |         25 |              0.080 |              0.080 |          0.081 |          0.104 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.124 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.009 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.081 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
