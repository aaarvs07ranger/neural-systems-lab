# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.520 | 0.382 |               103.360 |               4.865 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.674 |                54.280 |               9.423 |         25 |             -0.400 |             -0.769 |         -0.292 |         -0.764 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.769 |                30.960 |              10.454 |         25 |             -0.480 |             -0.923 |         -0.387 |         -1.011 |
| B_L2 (+ object appearance)                      |          0.960 | 0.752 |                34.480 |              10.010 |         25 |             -0.440 |             -0.846 |         -0.370 |         -0.968 |
| B_L3 (+ distractors)                            |          0.920 | 0.715 |                30.440 |               9.652 |         25 |             -0.400 |             -0.769 |         -0.333 |         -0.871 |

- **L1: success drop -0.400 absolute, -76.9% relative · SPL drop -0.292 absolute**
- **L2noT: success drop -0.480 absolute, -92.3% relative · SPL drop -0.387 absolute**
- **L2: success drop -0.440 absolute, -84.6% relative · SPL drop -0.370 absolute**
- **L3: success drop -0.400 absolute, -76.9% relative · SPL drop -0.333 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
