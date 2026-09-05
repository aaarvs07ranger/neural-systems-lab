# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.778 |                10.960 |              10.684 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.776 |                16.960 |              10.628 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L2 (+ object appearance)  |          1.000 | 0.775 |                21.240 |              10.567 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L3 (+ distractors)        |          0.960 | 0.734 |                28.240 |              10.109 |         25 |              0.040 |              0.040 |          0.044 |          0.057 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.044 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
