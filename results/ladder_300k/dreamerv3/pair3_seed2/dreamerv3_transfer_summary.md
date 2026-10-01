# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.552 |                54.880 |              10.849 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.040 |               192.160 |              -1.734 |         25 |              0.800 |              0.952 |          0.512 |          0.928 |
| B_L2 (+ object appearance)  |          0.240 | 0.177 |               173.320 |               1.289 |         25 |              0.600 |              0.714 |          0.375 |          0.680 |
| B_L3 (+ distractors)        |          0.160 | 0.160 |               179.040 |               0.400 |         25 |              0.680 |              0.810 |          0.392 |          0.710 |

- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.512 absolute**
- **L2: success drop 0.600 absolute, 71.4% relative · SPL drop 0.375 absolute**
- **L3: success drop 0.680 absolute, 81.0% relative · SPL drop 0.392 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
