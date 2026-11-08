# VN-002 · Van kennel cabinet with sliding desk top

A ¾″ ash-ply cabinet in the van: a dog kennel at the bottom (open on the passenger side), a
shelf above it, and a lid that slides out sideways and drops to become a desk. Rebuilt in
SolidCraft from the Onshape model *Van Kennel and Cabinate* V1, part studio **Groove2**
(the parts the *study* document's **Kennel Cabinet** assembly uses), then redesigned (v2):
the v1 dowel tracks broke out and the desk bounced.

| | |
|---|---|
| Status | v1 = as built (Onshape rebuild, in git history). v2 = new build from scratch, designed, not yet cut |
| Process | Shaper Origin (panels, plate pockets, relief grooves); track plates laser-cut by SendCutSend |
| Material | ¾″ white-ash plywood (**thickness unverified**: measure the sheet); 0.190″ 6061-T6 aluminium plates |
| Hardware | 4 × ⅜″ steel dowel pins, 2 folding shelf brackets, 32 × #6 82° flat-head screws |
| Key dims | 15 W × 21 D × 32 H in; kennel opening 13.5 × 12 in; shelf at 12 in; desk surface at 22.7 in |

## How the lid works
Each side rail is an L: a 15″ × ¾″ bar along the top's end grain plus a 1.5″ wide drop leg at
the front. The leg carries two pins that run in tracks on the **outside** face of each side panel:
two horizontal tracks (the lid slides 13.5″ aft), then a vertical drop slot ¾″ in from the aft
edge (both pins drop 9.3″ and the lid hangs beside the cabinet as a lower **desk**).
Parameter `desk` = 0 shows it stowed, 1 shows desk mode.

The ¾″ drop-slot edge distance is not free: the lid only clears the aft panel on the way down
when `pin_x + groove_edge = fill_w` (0.75 + 0.75 = 1.5″). In desk mode the top's inner edge sits
exactly flush with the aft face.

## Why v1 broke and bounced
- In desk mode the whole lid is a cantilever held by a couple of two dowels **1.5″ apart**.
  The lid alone is ~2.6 kg at ~7″; with ~150 N of forearms and laptop at ~10″ the moment is
  ~43 N·m, ~21 N·m per side, so each dowel pushes **~560 N** sideways.
- The upper dowel pushes towards the aft edge, on the ply between the drop groove and the edge:
  **14 mm wide and only 9.5 mm deep** (half the panel). Shear-out area ~2 × 14 × 9.5 ≈ 270 mm²;
  at ~2 MPa plywood rolling shear that is **~540 N**: about the load. That matches the break.
- Bounce: a ⅜″ dowel in a routed ⅜″ groove has ~0.3–0.5 mm play per dowel. Over a 38 mm couple
  that is **~10 mm of free play at a 20″ desk edge**, before any ply flex.

## v2 design
- **Aluminium track plates.** An L-shaped 0.190″ 6061 plate let in flush on each side panel
  (band across the top 5″, leg down the aft edge), slots cut in the metal. The pins bear only on
  aluminium; a relief groove (pin + 1/16″ wide, ¼″ deeper) behind each slot keeps them off the
  ply. 16 countersunk #6 screws per plate, the edge rows into the front/aft panel end grain.
  The ¾″ web behind the drop slot is ~108 MPa worst case without the brackets (SF ≈ 2.2).
- **Pins 3″ apart** (was 1.5″): half the force per pin (~280 N). The rail leg grows to 5.25″.
- **Steel pins**, ⅜″ hardened dowel pins pressed through the rail leg into the relief groove.
- **Desk brackets.** Two folding shelf brackets on the aft panel carry the desk in desk mode,
  so the pins only locate it: that removes the bounce. Modelled as 10 × 8″ flats (placeholders).

Both plates are the same flat part: the passenger one is the outside one flipped over.

### Unverified (measure before cutting / ordering)
| Value | Model | Why it matters |
|---|---|---|
| Ply thickness `t` | 0.75″ nominal | every joint; screw edge distances |
| Plate thickness `plate_t` | 0.1875″ in the model; SendCutSend stock is **0.190″** | set `plate_t` to 0.190 so the pocket depth matches |
| Pin diameter / length | ⅜″ × 1-1/8″ | slot is pin + 0.15 mm; buy the pins, measure, then set `pin_d` and the length |
| Bracket arm / height | 10″ / 8″ | bracket top must sit at the desk underside (21.94″) |
| #6 countersink | model 0.28″; SendCutSend 0.307″ | see the open issue below |

### Open issue: aft-edge screws
The 5 screws in the strip behind the drop slot (`XA`) sit in 0.56″ of metal. With SendCutSend's
#6 countersink (0.307″) that leaves only **0.126″** each side, to the plate edge and to the slot,
and their guidelines warn against countersinks that close to edges. Switch those 5 to #4
(0.255″) or move them before ordering.

## Parts
**Make**
| Part | Qty | From |
|---|---|---|
| Front, Aft | 2 | ¾″ ash ply |
| Outside side, Passenger side (plate pocket + relief grooves) | 2 | ¾″ ash ply |
| Shelf, Top, Top filler | 3 | ¾″ ash ply |
| Side rails (L, 5.25″ leg, pin holes 3″ apart) | 2 | ¾″ ash ply |
| Track plate (`sendcutsend/vn002-track-plate.dxf`, order qty 2) | 2 | SendCutSend 6061-T6 0.190″, 16 × #6 82° countersinks, black anodize |

**Buy**
| Item | Qty | Spec |
|---|---|---|
| Dowel pins | 4 | ⅜″ hardened steel, ~1-1/8″ (nearest stocked length; adjust the model) |
| Folding shelf brackets | 2 | ~10″ arm; fit-critical height, see above |
| Flat-head screws | 32 | #6 × ? 82°, black oxide; length to suit ¾″ ply |
| Bracket and rail screws | — | not modelled |

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
   Black-oxide screws. Pins bare steel, lightly waxed; paste wax on the rails' inner faces.
5. Fit the plates after the finish has cured.

## Files
- `kennel-cabinet.json`: source of truth (SolidCraft script, parameters in inches). `./build.sh` regenerates the rest.
- Bodies: `Front`, `Aft`, `PassengerSide`, `OutsideSide`, `Shelf`, `Top`, `TopFiller`,
  `PlateOutside`, `PlatePassenger`, `RailOutside`, `RailPassenger`,
  `Pin{Outside,Passenger}{Upper,Lower}`, `Bracket1`, `Bracket2`.
- `sendcutsend/plate_dxf.py` writes `sendcutsend/vn002-track-plate.dxf` (true arcs and circles;
  holes at SendCutSend's #6 countersink pilot, 0.164″). It mirrors the plate parameters in the
  script by hand: change both together.
- `out/desk-iso.png`: desk mode.

## Checks
- v1 against the Onshape BOM (660 kg/m³): front/aft 4943.0 g (Onshape 4943.0), shelf 2135.4
  (2135.4), top 2299.6 (2299.6), filler 255.5 (255.5), outside panel 3737.6 (3740.2), passenger
  side 2423.5 (2426.1), rail 126.1 (125.3; its 0.1″ edge rounds are left out).
- v2 volumes against a hand grid: outside panel 329.772 in³ (expected 329.761), passenger side
  208.272 (208.261), plates 14.560 each (16 holes, 53 faces), rails 13.344 (13.344).
- v2 desk mode: top x 7.5–21″ (flush with the aft face), underside 21.937″ on the bracket tops at
  21.938″, lower pin at the slot end (18.19″).
- Plate DXF: 1 outline, 1 slot cutout, 16 holes; net area × 0.1875″ − countersinks = 14.56 in³,
  the model's plate volume.

## Log
- 2026-11-08: v1 rebuilt from Onshape (public API feature list + drawings). As built, the
  groove walls broke out and the desk bounces.
- 2026-11-08: v2 designed for a new build: aluminium track plates, pins at 3″ pitch, desk
  brackets; finish chosen (dark grey hardwax oil, poly kennel, black anodized plates).
  Not yet ordered or cut.
