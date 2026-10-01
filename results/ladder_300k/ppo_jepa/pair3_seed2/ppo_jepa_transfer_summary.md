# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.616 |                53.600 |               9.577 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.080 | 0.066 |               185.080 |              -0.464 |         25 |              0.720 |              0.900 |          0.550 |          0.893 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.051 |               185.360 |              -0.684 |         25 |              0.720 |              0.900 |          0.565 |          0.917 |
| B_L2 (+ object appearance)                      |          0.040 | 0.026 |               193.000 |              -1.144 |         25 |              0.760 |              0.950 |          0.590 |          0.958 |
| B_L3 (+ distractors)                            |          0.040 | 0.026 |               193.000 |              -1.158 |         25 |              0.760 |              0.950 |          0.590 |          0.958 |

- **L1: success drop 0.720 absolute, 90.0% relative · SPL drop 0.550 absolute**
- **L2noT: success drop 0.720 absolute, 90.0% relative · SPL drop 0.565 absolute**
- **L2: success drop 0.760 absolute, 95.0% relative · SPL drop 0.590 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.590 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
