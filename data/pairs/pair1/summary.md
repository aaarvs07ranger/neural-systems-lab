# Visual Variant Summary

- Source: ProcTHOR-10k train split, house index **2**
- Target object type (ObjectNav): **Bed**
- Variant seed: `1338`
- Levels generated: **L1, L2, L3**
- Structural identity (geometry, object placement, task graph): **verified per level**

> Rungs are cumulative: L2 includes L1's changes, L3 includes both.
> Static checks cannot prove physical footprints are unchanged for
> L2/L3 -- the runtime C1/C2 navmesh verification does that.

## L1 -- materials and lighting

### Wall materials (A -> B)

- `FireplaceTiles` -> `SubwayTilesRough`
- `LightWhite` -> `YellowDrywall 1`

### Floor materials (A -> B)

- `Wood 1` -> `GreyFloor`

### Ceiling material (A -> B)

- `OrangeDrywall 1` -> `TexturesCom_BrickRound0044_1_seamless_S`

### Lighting (warm tint + dimming)

- `DirectionalLight`: rgb {'r': 1.0, 'g': 1.0, 'b': 1.0} -> {'r': 1.0, 'g': 0.63, 'b': 0.474}, intensity 1 -> 0.61
- `light_2`: rgb {'r': 1.0, 'g': 0.855, 'b': 0.722} -> {'r': 1.0, 'g': 0.717, 'b': 0.528}, intensity 0.45 -> 0.3274

### Skybox: `SkyEmeryville` -> `SkySeaStacks`

## L2 -- object appearance (same type, different asset)

10 object(s) swapped.

- `Bed|2|0` (Bed): `Bed_20` -> `Bed_3`
- `BasketBall|surface|2|1` (BasketBall): `RoboTHOR_basketball_rhode_island_novelty_v` -> `Basketball_1`
- `TennisRacket|surface|2|2` (TennisRacket): `Tennis_Racquet_3` -> `Tennis_Racquet_4`
- `Pillow|surface|2|4` (Pillow): `pillow_3` -> `RoboTHOR_pillow_sanglarka_1_v`
- `AlarmClock|surface|2|0` (AlarmClock): `Alarm_Clock_2` -> `Alarm_Clock_18`
- `Pencil|surface|2|3` (Pencil): `RoboTHOR_pencil_amazon_basics_v` -> `Pencil_7`
- `HousePlant|2|2|0` (HousePlant): `Houseplant_18` -> `Houseplant_10`
- `GarbageCan|2|3` (GarbageCan): `bin_26` -> `bin_17`
- `Painting|2|4` (Painting): `Wall_Decor_Painting_6` -> `Wall_Decor_Painting_7`
- `Painting|2|5` (Painting): `Wall_Decor_Photo_6` -> `Wall_Decor_Painting_3`

**1 object(s) had no alternative asset and were left unchanged:**

- `Dresser|2|1` (Dresser): `RoboTHOR_dresser_rast_v`

## L3 -- distractor objects

2 distractor(s) added, 2 of a type absent from A. All placed on receptacle surfaces; none of the target type.

- `DeskLamp|distractor|0` (DeskLamp, `Desk_Lamp_2`) on `Dresser|2|1`
- `Pan|distractor|1` (Pan, `Pan_14`) on `Dresser|2|1`

_Note: scaled 8 -> 4: only 1 non-target surface(s) available_
