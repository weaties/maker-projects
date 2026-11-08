# VN-002 · Van kennel cabinet with sliding desk top

A ¾″ ash-ply cabinet in the van: a dog kennel at the bottom (open on the passenger side), a
shelf above it, and a lid that slides out sideways and drops to become a desk. Rebuilt in
SolidCraft from the Onshape model *Van Kennel and Cabinate* V1, part studio **Groove2**
(the parts the *study* document's **Kennel Cabinet** assembly uses), so it can be improved:
the dowel tracks broke out and the desk bounces.

| | |
|---|---|
| Status | v1 = as built (Onshape rebuild). v2 = fix the tracks + stiffen the desk (in progress) |
| Process | Shaper Origin (panels, tracks), hand tools |
| Material | ¾″ white-ash plywood (Onshape: 0.75 in nominal, **thickness unverified**) |
| Fasteners / hardware | 4 × ⅜″ hardwood dowels in the rail legs |
| Key dims | 15 W × 21 D × 32 H in; kennel opening 13.5 × 12 in; shelf at 12 in |

## How the lid works (read off the grooves)
Each side rail is an L: a 15″ × ¾″ bar along the top's end grain plus a 1.5 × 3.75″ drop leg
at the front. The leg carries two ⅜″ dowels 1.5″ apart vertically that run in ⅜″-wide, ⅜″-deep
grooves routed into the **outside** face of each side panel:

- two horizontal tracks across the panel (1.5″ and 3″ below the top surface): the lid slides
  13.5″ towards the aft side;
- a drop groove ¾″ in from the aft edge, ~10.8″ long: at the end of the slide both dowels drop
  down it and the lid hangs beside the cabinet as a lower **desk**, cantilevered off the dowels;
- a short connector between the tracks 1.5″ before the drop groove (in the Onshape model; its
  purpose is unconfirmed).

Simplified here: the Onshape junction at the top of the drop groove also has a small quarter
arc; it is left out (groove volume 5.98 in³ here vs 5.75 in³ in Onshape).

## Why it broke and why it bounces (v1 numbers)
- In desk mode the whole lid is a cantilever held by a couple of two dowels **1.5″ apart**.
  The lid alone is ~2.6 kg at ~7″; with ~150 N of forearms and laptop at ~10″ the moment is
  ~43 N·m, ~21 N·m per side, so each dowel pushes **~560 N** sideways.
- The upper dowel pushes towards the aft edge. The wall it bears on is the ply between the
  drop groove and the edge: **0.56″ (14 mm) wide and only ⅜″ (9.5 mm) deep**, since the groove
  is half the panel thickness. Its shear-out area is ~2 × 14 × 9.5 ≈ 270 mm²; at ~2 MPa
  plywood rolling shear that is **~540 N**: about the load. That matches the break.
- Bounce: a ⅜″ dowel in a routed ⅜″ groove has ~0.3–0.5 mm play per dowel. Over a 38 mm
  couple arm that is ~0.02 rad, **~10 mm of free play at a 20″ desk edge**, before any ply flex.

## Files
- `kennel-cabinet.json`: source of truth (SolidCraft script, parameters in inches). `./build.sh` regenerates the rest.
- Bodies: `Front`, `Aft`, `PassengerSide`, `OutsideSide`, `Shelf`, `Top`, `TopFiller`,
  `RailOutside`, `RailPassenger`, `Pin{Outside,Passenger}{Upper,Lower}`.

Check against the Onshape BOM (mass at 660 kg/m³): front/aft 4943.0 g (Onshape 4943.0),
shelf 2135.4 (2135.4), top 2299.6 (2299.6), top filler 255.5 (255.5), outside panel 3737.6
(3740.2), passenger side 2423.5 (2426.1), side rail 126.1 (125.3; its 0.1″ edge rounds are
left out). Onshape modelled 2 dowels; both rails need 2 each, so this has 4.

## Log
- 2026-11-08: v1 rebuilt from Onshape (public API feature list + drawings). As built, the
  groove walls broke out and the desk bounces.
