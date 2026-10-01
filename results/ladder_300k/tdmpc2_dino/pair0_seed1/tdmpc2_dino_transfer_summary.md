# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.792 |                18.840 |              10.955 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.763 |                26.800 |              10.456 |         25 |              0.040 |              0.042 |          0.029 |          0.036 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.762 |                32.960 |              10.804 |         25 |              0.000 |              0.000 |          0.030 |          0.037 |
| B_L2 (+ object appearance)                      |          0.960 | 0.746 |                29.000 |              10.828 |         25 |              0.000 |              0.000 |          0.046 |          0.058 |
| B_L3 (+ distractors)                            |          0.880 | 0.707 |                43.080 |               9.845 |         25 |              0.080 |              0.083 |          0.085 |          0.108 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.029 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.030 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.046 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.085 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
