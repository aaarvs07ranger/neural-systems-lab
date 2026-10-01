# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.774 |                17.960 |              10.597 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.733 |                34.800 |              10.038 |         25 |              0.040 |              0.040 |          0.041 |          0.054 |
| B_L2 (+ object appearance)  |          0.960 | 0.734 |                37.920 |               9.991 |         25 |              0.040 |              0.040 |          0.040 |          0.052 |
| B_L3 (+ distractors)        |          0.960 | 0.762 |                33.440 |              10.020 |         25 |              0.040 |              0.040 |          0.012 |          0.016 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.012 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
