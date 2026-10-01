# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.766 |                15.040 |              10.907 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.774 |                36.440 |              10.427 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.772 |                42.080 |              10.372 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| B_L2 (+ object appearance)                      |          1.000 | 0.777 |                38.360 |              10.418 |         25 |              0.000 |              0.000 |         -0.011 |         -0.015 |
| B_L3 (+ distractors)                            |          1.000 | 0.773 |                44.120 |              10.355 |         25 |              0.000 |              0.000 |         -0.008 |         -0.010 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.011 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
