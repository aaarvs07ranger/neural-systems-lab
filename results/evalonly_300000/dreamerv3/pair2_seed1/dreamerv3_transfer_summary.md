# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.752 |                13.400 |              10.936 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.750 |                40.120 |              10.515 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.716 |                65.680 |               9.407 |         25 |              0.080 |              0.080 |          0.035 |          0.047 |
| B_L2 (+ object appearance)                      |          0.960 | 0.756 |                58.160 |               9.860 |         25 |              0.040 |              0.040 |         -0.004 |         -0.005 |
| B_L3 (+ distractors)                            |          0.960 | 0.756 |                65.360 |               9.800 |         25 |              0.040 |              0.040 |         -0.004 |         -0.005 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.035 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop -0.004 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.004 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
