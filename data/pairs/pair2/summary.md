# Visual Variant Summary

- Source: ProcTHOR-10k train split, house index **250**
- Target object type (ObjectNav): **Bed**
- Variant seed: `1339`
- Levels generated: **L1, L2, L3**
- Structural identity (geometry, object placement, task graph): **verified per level**

> Rungs are cumulative: L2 includes L1's changes, L3 includes both.
> Static checks cannot prove physical footprints are unchanged for
> L2/L3 -- the runtime C1/C2 navmesh verification does that.

## L1 -- materials and lighting

### Wall materials (A -> B)

- `PureWhite` -> `OrangeDrywall`
- `DarkGranite` -> `WhiteGraniteClean`

### Floor materials (A -> B)

- `LightWoodCounters` -> `WoodFloorsCross`

### Ceiling material (A -> B)

- `PureWhite` -> `FireplaceTiles`

### Lighting (warm tint + dimming)

- `DirectionalLight`: rgb {'r': 1.0, 'g': 1.0, 'b': 1.0} -> {'r': 1.0, 'g': 0.682, 'b': 0.545}, intensity 1 -> 0.6482
- `light_2`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.776, 'b': 0.463}, intensity 0.45 -> 0.2995

### Skybox: `SkySeaStacks` -> `SkySFGarden`

## L2 -- object appearance (same type, different asset)

12 object(s) swapped.

- `Pillow|2|0|2` (Pillow): `pillow_30` -> `RoboTHOR_pillow_sanglarka_1_v`
- `Pillow|2|0|1` (Pillow): `pillow_30` -> `pillow_1`
- `BasketBall|surface|2|1` (BasketBall): `RoboTHOR_basketball_rhode_island_novelty_v` -> `Basketball_1`
- `RemoteControl|surface|2|2` (RemoteControl): `Remote_2` -> `Remote_3`
- `AlarmClock|surface|2|3` (AlarmClock): `Alarm_Clock_6` -> `Alarm_Clock_18`
- `CreditCard|surface|2|6` (CreditCard): `CreditCard_3` -> `CreditCard_4`
- `Mug|surface|2|7` (Mug): `Mug_1` -> `Mug_2`
- `Box|2|2` (Box): `Box_19` -> `Box_17`
- `Box|surface|2|0` (Box): `Box_27` -> `Box_14`
- `Box|2|4` (Box): `Box_18` -> `Box_15`
- `Painting|2|5` (Painting): `Wall_Decor_Painting_1V` -> `Wall_Decor_Painting_7`
- `Painting|2|6` (Painting): `Wall_Decor_Painting_8` -> `Wall_Decor_Painting_6`

**5 object(s) had no alternative asset and were left unchanged:**

- `Bed|2|0|0` (Bed): `Bed_19`
- `Dresser|2|1` (Dresser): `Dresser_318_2`
- `Desk|2|3` (Desk): `RoboTHOR_desk_lisabo`
- `BaseballBat|surface|2|4` (BaseballBat): `RoboTHOR_baseball_bat_rawlings_v`
- `CD|surface|2|5` (CD): `CD_1`

## L3 -- distractor objects

8 distractor(s) added, 8 of a type absent from A. All placed on receptacle surfaces; none of the target type.

- `Knife|distractor|0` (Knife, `Knife_2`) on `Dresser|2|1`
- `HousePlant|distractor|1` (HousePlant, `Houseplant_27`) on `Dresser|2|1`
- `ButterKnife|distractor|2` (ButterKnife, `RoboTHOR_butter_knife_ai2_1_v`) on `Dresser|2|1`
- `SoapBottle|distractor|3` (SoapBottle, `Soap_Bottle_24`) on `Dresser|2|1`
- `Bottle|distractor|4` (Bottle, `Bottle_1`) on `Dresser|2|1`
- `Candle|distractor|5` (Candle, `Candle_4`) on `Dresser|2|1`
- `Vase|distractor|6` (Vase, `Vase_Flat_5`) on `Dresser|2|1`
- `SprayBottle|distractor|7` (SprayBottle, `Spray_Bottle_6`) on `Dresser|2|1`
