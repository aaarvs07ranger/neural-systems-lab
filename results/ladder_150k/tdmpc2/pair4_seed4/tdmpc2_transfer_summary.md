# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.717 |                37.120 |              12.752 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.120 | 0.052 |               181.920 |              -0.256 |         25 |              0.840 |              0.875 |          0.665 |          0.927 |
| B_L2 (+ object appearance)  |          0.040 | 0.036 |               193.800 |              -1.223 |         25 |              0.920 |              0.958 |          0.681 |          0.949 |
| B_L3 (+ distractors)        |          0.080 | 0.018 |               186.200 |              -1.764 |         25 |              0.880 |              0.917 |          0.699 |          0.975 |

- **L1: success drop 0.840 absolute, 87.5% relative · SPL drop 0.665 absolute**
- **L2: success drop 0.920 absolute, 95.8% relative · SPL drop 0.681 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.699 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
