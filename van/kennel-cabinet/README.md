# VN-002 · Van kennel cabinet with sliding desk top

A ¾″ ash-ply cabinet in the van: a dog kennel at the bottom (open on the passenger side), a
shelf above it, and a lid that slides out sideways and drops to become a desk, or swings down to
hang flat so the top is open. Rebuilt in SolidCraft from the Onshape model *Van Kennel and
Cabinate* V1, part studio **Groove2** (the parts the *study* document's **Kennel Cabinet**
assembly uses), then redesigned for a new build: the v1 dowel tracks broke out and the desk bounced.

| | |
|---|---|
| Status | v1 = as built (Onshape rebuild, in git history). v5 = new build from scratch, designed, not yet cut |
| Process | Shaper Origin (panels, plate pockets, relief grooves); track plates laser-cut by SendCutSend |
| Material | ¾″ white-ash plywood (**thickness unverified**: measure the sheet); 0.190″ 6061-T6 aluminium plates |
| Hardware | 4 × ⅜″ steel dowel pins, 48 × #6 82° flat-head screws |
| Key dims | 15 W × 21 D × 32 H in; kennel opening 13.5 × 12 in; shelf at 12 in; desk surface 22.7 in at its lowest |

## How the lid works
Each side rail is an L: a 15″ × ¾″ bar along the top's end grain plus a 1.5″ wide drop leg at
the front. The leg carries two pins 3″ apart that run in slots in an aluminium plate on the
**outside** face of each side panel:

1. **Install:** the drop slot runs out through the top edge of each plate (as v1's groove did).
   Hold the lid level beside the aft end with the rail legs over the side panels and lower it: the
   pins drop into the slots from above until they reach the tracks.
2. **Stowed:** slide the lid forward along the two horizontal tracks; it sits on top.
3. **Hang (stored at the top of the run):** slide the lid 13.5″ aft to the end of the tracks, keep
   its inner edge up and let the outer end swing down. The upper pin stays in the top corner; the
   lower pin follows a curved slot (radius 3″ = the pin spacing, about the upper pin) from the end of
   the lower track up into the upper track. The lid turns 90° and hangs flat on the aft face,
   16¼–29¾″ off the floor (top 2¼″ below the cabinet top), clear of anything stored below. Both
   pins end up on the upper track and the lid rests flat on the face, so it is locked.
   - If the inner edge drops instead, the upper pin runs down the drop slot while the lower pin runs
     forward along the lower track, and the lid ends up hanging 3″ lower (13¼–26¾″), also locked.
     That path cannot be blocked: it is the same corner the pins use to drop into desk mode.
4. **Desk:** from the end of the slide, hold the lid level and push it down the vertical slot ¾″ in
   from the aft edge. The desk stays at any height you leave it: its weight twists the pins against
   opposite slot walls and friction holds it (as in v1). The lowest desk height is 22.7″.

Parameters: `desk` 0 = stowed, 1 = desk at its lowest; `fold` 0 = flat, 1 = hanging (with desk = 1).

Two clearances are geometry, not tuning:
- The lid clears the aft panel on the way down only when `pin_x + groove_edge = fill_w`
  (0.75 + 0.75 = 1.5″). In desk mode the top's inner edge is exactly flush with the aft face.
- Hanging, the lid's underside lands exactly on the aft face because the upper pin is 0.75″ in
  from that face and 0.75″ below the lid's underside. The swing never crosses the face.

The hang curve runs between the two tracks, so it cuts a quarter-round **insert** loose from the
plate (5.2 in², bounded by the curve, the upper track and the drop slot). It is its own part, cut
from the same DXF and screwed down with two screws. It is lightly loaded: only a desk set within an
inch of the top bears on it. `hang_drop` moves the pivot down the drop slot if a lower hang is ever
wanted (the curve has to stay clear of the tracks, or below the lower one, to avoid more inserts).

## Why v1 broke and bounced
- In desk mode the whole lid is a cantilever held by a couple of two dowels **1.5″ apart**.
  The lid alone is ~2.6 kg at ~7″; with ~150 N of forearms and laptop at ~10″ the moment is
  ~43 N·m, ~21 N·m per side, so each dowel pushes **~560 N** sideways.
- The upper dowel pushes towards the aft edge, on the ply between the drop groove and the edge:
  **14 mm wide and only 9.5 mm deep** (half the panel). Shear-out area ~2 × 14 × 9.5 ≈ 270 mm²;
  at ~2 MPa plywood rolling shear that is **~540 N**: about the load. That matches the break.
- Bounce: a ⅜″ dowel in a routed ⅜″ groove has ~0.3–0.5 mm play per dowel. Over a 38 mm couple
  that is **~10 mm of free play at a 20″ desk edge**, before any ply flex.

## Design (v5)
- **Aluminium track plates.** An L-shaped 0.190″ 6061 plate let in flush on each side panel
  (band across the top 5″, a leg down the aft edge, a foot carrying the hang curve), slots cut in
  the metal. The pins bear only on aluminium; a relief groove (7/16″ wide, ¼″ below the pocket
  floor) behind every slot keeps them off the ply. 24 countersunk #6 screws per plate (2 of them in
  the curve insert), the edge
  rows into the front/aft panel end grain. With the drop slot open at the top, the strip above the
  upper track and the strip behind the drop slot are each held only at one end, so both carry a
  row of screws. The ¾″ web behind the drop slot is ~108 MPa worst
  case (SF ≈ 2.2) with the pins carrying the whole desk.
- **Pins 3″ apart** (was 1.5″): half the force per pin (~280 N). The rail leg grows to 5.25″.
- **Steel pins**, ⅜″ hardened dowel pins pressed through the rail leg into the relief groove.
- **No brackets.** v2 had folding brackets under the desk; folded, they would sit where the lid
  hangs. The pins carry the desk: 0.15 mm clearance in aluminium over a 3″ couple is ~1 mm of free
  play at the desk edge (v1: ~10 mm). If it still feels lively, flush swing-out arms pocketed into
  the aft panel can be added later without changing anything else.
- **Desk height by friction.** Holding under the lid's own weight needs a friction coefficient
  above ~0.2 (pin spacing / (2 × lever arm) = 3 / (2 × 7.5)). Dry steel on anodized aluminium is
  well above that, so **don't wax the pins or slots**. Test it once the plates arrive.

Both plates are the same flat part: the passenger one is the outside one flipped over.

### Unverified (measure before cutting / ordering)
| Value | Model | Why it matters |
|---|---|---|
| Ply thickness `t` | 0.75″ nominal | every joint; screw edge distances |
| Plate thickness `plate_t` | 0.190″ (SendCutSend stock) | pocket depth; measure the plates and set it |
| Pin diameter / length | ⅜″ × 1-1/8″ | slot is pin + 0.15 mm; buy the pins, measure, then set `pin_d` and the length |
| #6 countersink | 0.307″ × 82° (SendCutSend), pilot 0.164″ | head must sit flush or below: the rail slides over it |
| Desk-height friction | assumed μ > 0.2 | if the desk creeps down, add a detent or skip the anodize in the drop slot |

### Open issue: aft-edge screws
10 screws sit in 0.56″-wide strips: 6 behind the drop slot (`XA`) and 4 above the upper track
(`ZS`). With the 0.307″ countersink that leaves only **0.126″** each side, and SendCutSend's
guidelines warn against countersinks that close to edges. Switch those 10 to #4 (0.255″) before
ordering, or accept SendCutSend's verdict on the quote.

## Parts
**Make**
| Part | Qty | From |
|---|---|---|
| Front, Aft | 2 | ¾″ ash ply, 19½ × 31¼ |
| Outside side, Passenger side (plate pocket + relief grooves) | 2 | ¾″ ash ply, 15 × 31¼ |
| Shelf | 1 | ¾″ ash ply, 13½ × 19½ |
| Top, Top filler | 2 | ¾″ ash ply, 13½ × 21 and 1½ × 21 |
| Side rails (L, 5.25″ leg, pin holes 3″ apart) | 2 | ¾″ ash ply |
| Track plate + curve insert (`sendcutsend/vn002-track-plate.dxf`: both pieces, order qty 2) | 2 + 2 | SendCutSend 6061-T6 0.190″, 24 × #6 82° countersinks per set, black anodize |

**Buy**
| Item | Qty | Spec |
|---|---|---|
| Dowel pins | 4 | ⅜″ hardened steel, ~1-1/8″ (nearest stocked length; adjust the model) |
| Flat-head screws | 48 | #6 82°, black oxide; length to suit ¾″ ply |

## Finish
Matches the van interior: grey felt walls, black trim, grey streaky woodgrain laminate cabinets
with black edges and hardware.

1. Machine everything first (pockets, grooves, holes). **1/8″ roundover** on exposed edges, ply
   layers showing. Keep square: glued joints, the top/filler seam, plate pocket edges, panel edges
   under the rails. Lay parts out with the face grain **horizontal** (as the laminate).
2. **Kennel** floor, lower walls and opening edges: sand 150, mask a clean line, 3–4 coats of
   water-based poly (non-yellowing). Before any oil: a film will not bond over oil.
3. **Everything else:** sand 120–150, **dark grey tinted hardwax oil**, 2 coats, both faces of
   every panel (a van cycles damp and heat). Extra coat on the desk surface. Test the shade on an
   offcut of the actual sheet next to the cabinet laminate first: ash ply takes tint unevenly.
4. **Plates:** black anodize (SendCutSend; ~0.01 mm per side, the slot fit is unaffected).
   Black-oxide screws. Pins bare steel, **not waxed** (the desk height relies on friction); paste
   wax only on the rails' inner faces, where they slide over the plate.
5. Fit the plates after the finish has cured.

## Files
- `kennel-cabinet.json`: source of truth (SolidCraft script, parameters in inches). `./build.sh` regenerates the rest.
- Bodies: `Front`, `Aft`, `PassengerSide`, `OutsideSide`, `Shelf`, `Top`, `TopFiller`,
  `PlateOutside`, `PlatePassenger`, `RailOutside`, `RailPassenger`, `Pin{Outside,Passenger}{Upper,Lower}`.
- `drawing.json` → `out/drawing-{panels,sides,plate}.{svg,pdf,png}`: shop drawings in inches.
- `sendcutsend/plate_dxf.py` writes `sendcutsend/vn002-track-plate.dxf` (true circles; holes at
  SendCutSend's #6 countersink pilot, 0.164″). It mirrors the plate parameters in the script by
  hand: change both together.
- `out/desk-iso.png`, `out/hang-iso.png`: desk and hanging positions.

## Checks
- v1 against the Onshape BOM (660 kg/m³): front/aft 4943.0 g (Onshape 4943.0), shelf 2135.4
  (2135.4), top 2299.6 (2299.6), filler 255.5 (255.5), outside panel 3737.6 (3740.2), passenger
  side 2423.5 (2426.1), rail 126.1 (125.3; its 0.1″ edge rounds are left out).
- v5 volumes against hand numbers (shapely areas × depths): outside panel 329.107 in³ (expected
  329.107), passenger side 207.607 (207.607), plate 13.423 + insert 0.970 = 14.393 (DXF net area
  × 0.190 − countersinks = 14.393; insert bbox 3.947–6.56 × 27.697–30.31″ in both), rails 13.344.
- v5 hanging (`desk` 1, `fold` 1): top x 7.5–8.25″, z 16.25–29.75″; both pins on the upper track
  (lower pin at 3.75″, the end of the curve).
- Plate DXF: 2 outlines (plate with the slots open at the top edge, curve insert), 24 holes.

## Log
- 2026-11-08: v1 rebuilt from Onshape (public API feature list + drawings). As built, the
  groove walls broke out and the desk bounces.
- 2026-11-08: v2 designed for a new build: aluminium track plates, pins at 3″ pitch, desk
  brackets; finish chosen (dark grey hardwax oil, poly kennel, black anodized plates).
- 2026-11-08: v3: the lid also swings down to hang on the aft face (hang curve in the plate);
  brackets dropped so it can hang flush and the desk height stays adjustable; plate 0.190″ and
  SendCutSend countersinks in the model.
- 2026-11-08: v4: the lid hangs high (pivot 3¾″ below the upper track, lid 12.5–26″ off the
  floor) so stored things below don't interfere; the drop slot runs out through the top edge so
  the lid installs from above, as v1.
- 2026-11-08: v5: hang from the end of the slide (highest: 16¼–29¾″); the curve crosses between
  the tracks and leaves a separate quarter-round insert. 24 screws per plate set. Shop drawings.
  Not yet ordered or cut.
