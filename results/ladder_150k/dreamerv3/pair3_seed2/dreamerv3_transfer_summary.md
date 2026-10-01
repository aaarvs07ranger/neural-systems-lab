# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.360 | 0.223 |               167.000 |               4.579 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.040 |               192.160 |              -2.368 |         25 |              0.320 |              0.889 |          0.183 |          0.820 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.200 |              -2.288 |         25 |              0.320 |              0.889 |          0.183 |          0.820 |
| B_L3 (+ distractors)        |          0.080 | 0.044 |               199.040 |              -1.783 |         25 |              0.280 |              0.778 |          0.179 |          0.803 |

- **L1: success drop 0.320 absolute, 88.9% relative · SPL drop 0.183 absolute**
- **L2: success drop 0.320 absolute, 88.9% relative · SPL drop 0.183 absolute**
- **L3: success drop 0.280 absolute, 77.8% relative · SPL drop 0.179 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
