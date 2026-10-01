# DREAMERV3 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.757 |                13.840 |              10.928 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.559 |                73.400 |               7.208 |         25 |              0.280 |              0.280 |          0.197 |          0.261 |
| B_L2 (+ object appearance)  |          0.760 | 0.565 |                76.880 |               7.589 |         25 |              0.240 |              0.240 |          0.192 |          0.253 |
| B_L3 (+ distractors)        |          0.680 | 0.454 |                78.160 |               6.715 |         25 |              0.320 |              0.320 |          0.302 |          0.399 |

- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.197 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.192 absolute**
- **L3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.302 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
