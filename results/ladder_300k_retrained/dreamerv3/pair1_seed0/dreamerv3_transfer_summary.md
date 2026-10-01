# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.620 |                33.000 |              10.220 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.565 |                53.360 |               8.661 |         25 |              0.120 |              0.125 |          0.056 |          0.090 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.606 |                48.440 |               9.580 |         25 |              0.040 |              0.042 |          0.014 |          0.023 |
| B_L2 (+ object appearance)                      |          0.880 | 0.606 |                50.520 |               9.128 |         25 |              0.080 |              0.083 |          0.014 |          0.023 |
| B_L3 (+ distractors)                            |          0.840 | 0.568 |                78.880 |               8.390 |         25 |              0.120 |              0.125 |          0.052 |          0.084 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.056 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.014 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.014 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.052 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
