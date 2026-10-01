# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.676 |                48.080 |              11.522 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.022 |               195.000 |              -1.921 |         25 |              0.880 |              0.957 |          0.654 |          0.968 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               195.240 |              -2.201 |         25 |              0.880 |              0.957 |          0.636 |          0.941 |
| B_L3 (+ distractors)        |          0.080 | 0.080 |               185.320 |              -1.305 |         25 |              0.840 |              0.913 |          0.596 |          0.882 |

- **L1: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.636 absolute**
- **L3: success drop 0.840 absolute, 91.3% relative · SPL drop 0.596 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
