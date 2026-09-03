# Visual Variant Summary

- Source: ProcTHOR-10k train split, house index **0**
- Target object type (ObjectNav): **Fridge**
- Variant seed: `1337`
- Levels generated: **L1, L2, L3**
- Structural identity (geometry, object placement, task graph): **verified per level**

> Rungs are cumulative: L2 includes L1's changes, L3 includes both.
> Static checks cannot prove physical footprints are unchanged for
> L2/L3 -- the runtime C1/C2 navmesh verification does that.

## L1 -- materials and lighting

### Wall materials (A -> B)

- `PureWhite` -> `Red2Drywall`
- `LivingRoomFireplacebrickTex` -> `DarkGranite`

### Floor materials (A -> B)

- `OrangeCabinet` -> `TexturesCom_WoodFine0050_1_seamless_S_pale`

### Ceiling material (A -> B)

- `PureWhite` -> `WhiteGraniteClean`

### Lighting (warm tint + dimming)

- `DirectionalLight`: rgb {'r': 1.0, 'g': 1.0, 'b': 1.0} -> {'r': 1.0, 'g': 0.756, 'b': 0.526}, intensity 1 -> 0.6222
- `light_2`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.713, 'b': 0.424}, intensity 0.45 -> 0.3318

### Skybox: `SkyAlbany` -> `SkyGasworks`

## L2 -- object appearance (same type, different asset)

23 object(s) swapped.

- `Apple|surface|2|0` (Apple): `Apple_24` -> `Apple_10`
- `Egg|surface|2|1` (Egg): `Egg_23` -> `Egg_18`
- `SprayBottle|surface|2|2` (SprayBottle): `Spray_Bottle_8` -> `Spray_Bottle_7`
- `Lettuce|surface|2|3` (Lettuce): `Lettuce_19` -> `Lettuce_10`
- `SaltShaker|surface|2|4` (SaltShaker): `RoboTHOR_salt_pepper_shaker_bnyd_salt_v` -> `Salt_Shaker_2`
- `Tomato|surface|2|7` (Tomato): `Tomato_5` -> `Tomato_14`
- `Potato|surface|2|9` (Potato): `Potato_6` -> `Potato_18`
- `Bowl|surface|2|11` (Bowl): `Bowl_22` -> `Bowl_18`
- `Pencil|surface|2|13` (Pencil): `Pencil_3` -> `Pencil_7`
- `SoapBottle|surface|2|14` (SoapBottle): `Soap_Bottle_3` -> `Soap_Bottle_11`
- `Plate|surface|2|15` (Plate): `Plate_11` -> `Plate_2`
- `Ladle|surface|2|16` (Ladle): `Ladle_1` -> `Ladle_2`
- `Fork|surface|2|17` (Fork): `Fork_1` -> `RoboTHOR_fork_ai2_v`
- `Fridge|2|1` (Fridge): `Fridge_19` -> `Fridge_29`
- `Lettuce|surface|2|10` (Lettuce): `Lettuce_7` -> `Lettuce_15`
- `Potato|surface|2|12` (Potato): `Potato_2` -> `Potato_14`
- `HousePlant|2|2|0` (HousePlant): `Houseplant_11` -> `Houseplant_15`
- `GarbageCan|2|3` (GarbageCan): `bin_25` -> `bin_18`
- `GarbageBag|2|4` (GarbageBag): `GarbageBag_21_2` -> `GarbageBag_21_1`
- `Painting|2|5` (Painting): `Wall_Decor_Photo_1V` -> `Wall_Decor_Painting_10`
- `Painting|2|6` (Painting): `Wall_Decor_Photo_2` -> `Wall_Decor_Painting_1V`
- `Painting|2|7` (Painting): `Wall_Decor_Painting_3V` -> `Wall_Decor_Painting_10`
- `Painting|2|8` (Painting): `Wall_Decor_Photo_6` -> `Wall_Decor_Painting_10`

**4 object(s) had no alternative asset and were left unchanged:**

- `CounterTop|2|0` (CounterTop): `Countertop_I_8x2`
- `Kettle|surface|2|5` (Kettle): `Kettle_1`
- `Kettle|surface|2|6` (Kettle): `Kettle_1`
- `WineBottle|surface|2|8` (WineBottle): `Wine_Bottle_1`

## L3 -- distractor objects

4 distractor(s) added, 4 of a type absent from A. All placed on receptacle surfaces; none of the target type.

- `BaseballBat|distractor|0` (BaseballBat, `RoboTHOR_baseball_bat_rawlings_v`) on `CounterTop|2|0`
- `Bread|distractor|1` (Bread, `Bread_9`) on `CounterTop|2|0`
- `DeskLamp|distractor|2` (DeskLamp, `RoboTHOR_desk_lamp_arstid_v`) on `CounterTop|2|0`
- `Dumbbell|distractor|3` (Dumbbell, `Dumbbell_1_1`) on `CounterTop|2|0`

_Note: scaled 8 -> 4: only 1 non-target surface(s) available_
