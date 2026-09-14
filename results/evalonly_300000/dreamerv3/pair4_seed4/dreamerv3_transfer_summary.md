# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.760 | 0.429 |                83.600 |              10.576 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.269 |               122.160 |               8.011 |         25 |              0.120 |              0.158 |          0.160 |          0.372 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.251 |               142.440 |               6.958 |         25 |              0.160 |              0.211 |          0.178 |          0.415 |
| B_L2 (+ object appearance)                      |          0.480 | 0.210 |               140.280 |               5.206 |         25 |              0.280 |              0.368 |          0.219 |          0.512 |
| B_L3 (+ distractors)                            |          0.520 | 0.191 |               126.960 |               6.044 |         25 |              0.240 |              0.316 |          0.238 |          0.555 |

- **L1: success drop 0.120 absolute, 15.8% relative · SPL drop 0.160 absolute**
- **L2noT: success drop 0.160 absolute, 21.1% relative · SPL drop 0.178 absolute**
- **L2: success drop 0.280 absolute, 36.8% relative · SPL drop 0.219 absolute**
- **L3: success drop 0.240 absolute, 31.6% relative · SPL drop 0.238 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
