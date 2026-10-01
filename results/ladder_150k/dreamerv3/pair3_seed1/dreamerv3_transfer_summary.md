# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.200 | 0.153 |               168.960 |               2.935 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.055 |               189.200 |              -1.409 |         25 |              0.120 |              0.600 |          0.098 |          0.642 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -1.750 |         25 |              0.200 |              1.000 |          0.153 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -1.646 |         25 |              0.200 |              1.000 |          0.153 |          1.000 |

- **L1: success drop 0.120 absolute, 60.0% relative · SPL drop 0.098 absolute**
- **L2: success drop 0.200 absolute, 100.0% relative · SPL drop 0.153 absolute**
- **L3: success drop 0.200 absolute, 100.0% relative · SPL drop 0.153 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
