# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.716 |                 9.880 |              10.839 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.693 |                10.600 |              10.861 |         25 |              0.000 |              0.000 |          0.024 |          0.033 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.700 |                18.960 |              10.758 |         25 |              0.000 |              0.000 |          0.016 |          0.022 |
| B_L2 (+ object appearance)                      |          1.000 | 0.703 |                12.680 |              10.844 |         25 |              0.000 |              0.000 |          0.013 |          0.018 |
| B_L3 (+ distractors)                            |          1.000 | 0.709 |                13.280 |              10.827 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.024 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.016 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
