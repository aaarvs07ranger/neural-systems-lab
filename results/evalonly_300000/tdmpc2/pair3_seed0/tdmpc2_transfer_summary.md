# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.721 |                31.520 |              12.036 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.080 | 0.044 |               189.600 |              -1.370 |         25 |              0.880 |              0.917 |          0.677 |          0.939 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.207 |               161.640 |               1.340 |         25 |              0.680 |              0.708 |          0.514 |          0.713 |
| B_L2 (+ object appearance)                      |          0.080 | 0.080 |               186.360 |              -1.150 |         25 |              0.880 |              0.917 |          0.641 |          0.889 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.572 |         25 |              0.960 |              1.000 |          0.721 |          1.000 |

- **L1: success drop 0.880 absolute, 91.7% relative · SPL drop 0.677 absolute**
- **L2noT: success drop 0.680 absolute, 70.8% relative · SPL drop 0.514 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.641 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.721 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
