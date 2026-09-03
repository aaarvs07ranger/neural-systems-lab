# Visual Variant Summary

- Source: ProcTHOR-10k train split, house index **286**
- Target object type (ObjectNav): **Television**
- Variant seed: `1341`
- Levels generated: **L1, L2, L3**
- Structural identity (geometry, object placement, task graph): **verified per level**

> Rungs are cumulative: L2 includes L1's changes, L3 includes both.
> Static checks cannot prove physical footprints are unchanged for
> L2/L3 -- the runtime C1/C2 navmesh verification does that.

## L1 -- materials and lighting

### Wall materials (A -> B)

- `YellowDrywall 1` -> `EggshellDrywall`
- `PureWhite` -> `SubwayTiles2`
- `RedDrywall` -> `FireplaceTiles2`

### Floor materials (A -> B)

- `WoodFineDarkFloorsRedNRM2` -> `OrangeCabinet 1`
- `LightWoodCounters3` -> `DarkWood2`

### Ceiling material (A -> B)

- `PureWhite` -> `Porcelain_Off_White_Mat`

### Lighting (warm tint + dimming)

- `DirectionalLight`: rgb {'r': 1.0, 'g': 1.0, 'b': 1.0} -> {'r': 1.0, 'g': 0.711, 'b': 0.545}, intensity 1 -> 0.5843
- `light_2`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.733, 'b': 0.545}, intensity 0.45 -> 0.2508
- `light_3`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.749, 'b': 0.566}, intensity 0.45 -> 0.2969

### Skybox: `SkyMountain` -> `SkySeaStacks`

## L2 -- object appearance (same type, different asset)

32 object(s) swapped.

- `Bowl|surface|2|0` (Bowl): `Bowl_27` -> `Bowl_14`
- `Microwave|surface|2|1` (Microwave): `Microwave_22` -> `Microwave_19`
- `Ladle|surface|2|2` (Ladle): `Ladle_1` -> `Ladle_2`
- `CreditCard|surface|2|4` (CreditCard): `CreditCard_4` -> `CreditCard_3`
- `HousePlant|surface|2|6` (HousePlant): `Houseplant_24` -> `Houseplant_14`
- `Statue|surface|2|7` (Statue): `Fertility_Statue_2` -> `Stone_Statue_3`
- `Pen|surface|2|8` (Pen): `Pen_2` -> `RoboTHOR_pen_signo_v`
- `PepperShaker|surface|2|9` (PepperShaker): `Pepper_Shaker_2` -> `RoboTHOR_salt_pepper_shaker_bnyd_pepper_v`
- `Potato|surface|2|10` (Potato): `Potato_3` -> `Potato_18`
- `Pot|surface|2|11` (Pot): `Pot_27` -> `Pot_18`
- `Mug|surface|2|14` (Mug): `Mug_1` -> `Mug_2`
- `Fridge|2|1` (Fridge): `Fridge_5` -> `Fridge_15`
- `Tomato|surface|2|5` (Tomato): `Tomato_9` -> `Tomato_11`
- `Egg|surface|2|12` (Egg): `Egg_21` -> `Egg_10`
- `Egg|surface|2|13` (Egg): `Egg_14` -> `Egg_11`
- `GarbageBag|2|2` (GarbageBag): `GarbageBag_21_2` -> `GarbageBag_21_1`
- `TVStand|3|0|0` (TVStand): `TV_Stand_222_1` -> `TV_Stand_211_1`
- `Television|3|0|2` (Television): `Television_14` -> `Television_3`
- `Pencil|surface|3|15` (Pencil): `RoboTHOR_pencil_amazon_basics_v` -> `Pencil_4`
- `Candle|surface|3|19` (Candle): `RoboTHOR_candle_glittrig_3_v` -> `RoboTHOR_candle_glittrig_1_v`
- `Pillow|surface|3|21` (Pillow): `pillow_28` -> `pillow_12`
- `Watch|surface|3|16` (Watch): `Watch_2` -> `Watch_1`
- `Pencil|surface|3|17` (Pencil): `Pencil_3` -> `Pencil_5`
- `Statue|surface|3|18` (Statue): `Fertility_Statue_3` -> `Stone_Statue_1`
- `Book|surface|3|20` (Book): `Book_20` -> `Book_14`
- `RemoteControl|surface|3|22` (RemoteControl): `Remote_1` -> `Remote_2`
- `ArmChair|3|2|0` (ArmChair): `RoboTHOR_armchair_overallt` -> `Armchair_201_3`
- `FloorLamp|3|2|1` (FloorLamp): `Floor_Lamp_18` -> `Floor_Lamp_10`
- `Painting|3|3` (Painting): `Wall_Decor_Painting_6` -> `Wall_Decor_Painting_7`
- `Painting|3|4` (Painting): `Wall_Decor_Photo_1V` -> `Wall_Decor_Painting_6`
- `Painting|3|5` (Painting): `Wall_Decor_Photo_6` -> `Wall_Decor_Painting_6`
- `Painting|3|6` (Painting): `Wall_Decor_Painting_3V` -> `Wall_Decor_Painting_7`

**4 object(s) had no alternative asset and were left unchanged:**

- `CounterTop|2|0` (CounterTop): `Countertop_C_8x6`
- `Spoon|surface|2|3` (Spoon): `Spoon_1`
- `Sofa|3|0|1` (Sofa): `RoboTHOR_sofa_alrid`
- `DiningTable|3|1` (DiningTable): `Dining_Table_21_2`

## L3 -- distractor objects

8 distractor(s) added, 8 of a type absent from A. All placed on receptacle surfaces; none of the target type.

- `CD|distractor|0` (CD, `CD_1`) on `Fridge|2|1`
- `Spatula|distractor|1` (Spatula, `Spatula_1`) on `Sofa|3|0|1`
- `Bottle|distractor|2` (Bottle, `Bottle_1`) on `CounterTop|2|0`
- `Plate|distractor|3` (Plate, `Plate_27`) on `DiningTable|3|1`
- `TeddyBear|distractor|4` (TeddyBear, `Teddy_Bear_2`) on `DiningTable|3|1`
- `Newspaper|distractor|5` (Newspaper, `Newspaper_2`) on `TVStand|3|0|0`
- `TennisRacket|distractor|6` (TennisRacket, `Tennis_Racquet_1`) on `CounterTop|2|0`
- `ButterKnife|distractor|7` (ButterKnife, `ButterKnife_1`) on `CounterTop|2|0`
