# Visual Variant Summary

- Source: ProcTHOR-10k train split, house index **44**
- Target object type (ObjectNav): **Bed**
- Variant seed: `1340`
- Levels generated: **L1, L2, L3**
- Structural identity (geometry, object placement, task graph): **verified per level**

> Rungs are cumulative: L2 includes L1's changes, L3 includes both.
> Static checks cannot prove physical footprints are unchanged for
> L2/L3 -- the runtime C1/C2 navmesh verification does that.

## L1 -- materials and lighting

### Wall materials (A -> B)

- `RedBricks 1` -> `DrywallBeige`
- `WallDrywallWhite3` -> `bathroomTilesTan3`
- `GreenCountertop` -> `DarkGranite`

### Floor materials (A -> B)

- `WoodSlashhatch` -> `TexturesCom_WoodFine0050_1_seamless_S_rich`
- `SMOOTHWOODWood2` -> `WoodFineDarkFloorsRedNRM`

### Ceiling material (A -> B)

- `EggshellDrywall 1` -> `SubwayTilesRough 1`

### Lighting (warm tint + dimming)

- `DirectionalLight`: rgb {'r': 1.0, 'g': 1.0, 'b': 1.0} -> {'r': 1.0, 'g': 0.63, 'b': 0.496}, intensity 1 -> 0.7266
- `light_2`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.663, 'b': 0.502}, intensity 0.45 -> 0.3121
- `light_3`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.741, 'b': 0.56}, intensity 0.45 -> 0.2932

### Skybox: `SkyGasworks` -> `SkyOakland`

## L2 -- object appearance (same type, different asset)

30 object(s) swapped.

- `Bed|2|0|0` (Bed): `Bed_19` -> `Bed_1`
- `Pillow|2|0|2` (Pillow): `pillow_30` -> `pillow_16`
- `Pillow|2|0|1` (Pillow): `pillow_30` -> `pillow_12`
- `AlarmClock|surface|2|13` (AlarmClock): `Alarm_Clock_19` -> `Alarm_Clock_18`
- `Book|surface|2|0` (Book): `RoboTHOR_book_ai2_2_v` -> `Book_17`
- `Pen|surface|2|3` (Pen): `Pen_3` -> `Pen_2`
- `Bowl|surface|2|5` (Bowl): `Bowl_8` -> `Bowl_18`
- `HousePlant|surface|2|6` (HousePlant): `Houseplant_15` -> `Houseplant_2`
- `Laptop|surface|2|10` (Laptop): `Laptop_22` -> `Laptop_15`
- `KeyChain|surface|2|12` (KeyChain): `Keychain_2` -> `Keychain_3`
- `CellPhone|surface|2|1` (CellPhone): `Cellphone_8` -> `RoboTHOR_cellphone_blackberry_v`
- `CellPhone|surface|2|2` (CellPhone): `Cellphone_5` -> `Cellphone_7`
- `DeskLamp|surface|2|4` (DeskLamp): `Desk_Lamp_6` -> `Desk_Lamp_12`
- `Pencil|surface|2|7` (Pencil): `Pencil_5` -> `Pencil_4`
- `Pencil|surface|2|8` (Pencil): `Pencil_3` -> `Pencil_7`
- `CreditCard|surface|2|9` (CreditCard): `CreditCard_4` -> `CreditCard_3`
- `Book|surface|2|11` (Book): `Book_15` -> `Book_17`
- `Chair|2|2|1` (Chair): `RoboTHOR_chair_antnas` -> `Chair_007_1`
- `ToiletPaper|surface|3|14` (ToiletPaper): `Toilet_Paper` -> `Toilet_Paper_Used_Up`
- `Sink|3|1|0` (Sink): `Sink_19` -> `Sink_15`
- `Faucet|3|1|1` (Faucet): `Bathroom_Faucet_15` -> `Bathroom_Faucet_21`
- `GarbageCan|3|2` (GarbageCan): `bin_13` -> `bin_17`
- `Plunger|3|3` (Plunger): `Plunger_1` -> `Plunger_2`
- `SideTable|3|4` (SideTable): `Side_Table_302_1_5` -> `RoboTHOR_side_table_hol`
- `HousePlant|surface|3|15` (HousePlant): `Houseplant_4` -> `Houseplant_18`
- `Painting|2|3` (Painting): `Wall_Decor_Painting_10` -> `Wall_Decor_Painting_3V`
- `Painting|2|4` (Painting): `Wall_Decor_Photo_3` -> `Wall_Decor_Painting_3`
- `Painting|3|5` (Painting): `Wall_Decor_Painting_3` -> `Wall_Decor_Painting_10`
- `Painting|3|6` (Painting): `Wall_Decor_Photo_1` -> `Wall_Decor_Painting_6`
- `Painting|3|7` (Painting): `Wall_Decor_Photo_10` -> `Wall_Decor_Painting_3`

**3 object(s) had no alternative asset and were left unchanged:**

- `Dresser|2|1` (Dresser): `Dresser_318_1`
- `DiningTable|2|2|0` (DiningTable): `Dining_Table_27_1`
- `Toilet|3|0` (Toilet): `Toilet_1`

## L3 -- distractor objects

8 distractor(s) added, 8 of a type absent from A. All placed on receptacle surfaces; none of the target type.

- `Pan|distractor|0` (Pan, `Pan_26`) on `DiningTable|2|2|0`
- `Cloth|distractor|1` (Cloth, `Cloth_11`) on `Toilet|3|0`
- `Bread|distractor|2` (Bread, `Bread_29`) on `SideTable|3|4`
- `CD|distractor|3` (CD, `CD_1`) on `Dresser|2|1`
- `Potato|distractor|4` (Potato, `Potato_10`) on `Dresser|2|1`
- `Spoon|distractor|5` (Spoon, `Spoon_1`) on `Toilet|3|0`
- `Bottle|distractor|6` (Bottle, `Bottle_1`) on `Sink|3|1|0`
- `Statue|distractor|7` (Statue, `Dog_Statue_2`) on `Sink|3|1|0`
