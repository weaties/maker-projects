# VN-001 · Sprinter phone sun hood + vent duct

A sun hood for the phone on the Quad Lock mount on the 2017 Sprinter dash (between the instrument
pod and the centre document compartment), plus a removable duct that takes air from the nearby
vent and blows it across the back of the phone. The phone overheats in the sun.

| | |
|---|---|
| Status | v0 modelled, all fit dims UNVERIFIED (placeholders) |
| Process | 3D print (Bambu X2D) |
| Material | ASA (dash sun: >80 °C, UV) |
| Fasteners / hardware | M3 × 16 screw + nut (clamp pinch); 5/8 in ID silicone hose, length to suit |
| Key dims | hood 120 × 80 × 205 mm, 92 g; scoop 60 × 50 × 58 mm, 24 g (at placeholder values) |

## Concept
Phone: iPhone 16 Pro Max in a Quad Lock case, portrait. The Quad Lock head is a wireless-charging
puck on a ball-joint arm; the base is screwed to the centre console to the right of the holder.

1. **Hood** (one print), clamped to the ball-joint arm just behind the puck, so it moves with the phone:
   - **Roof** with short side cheeks. The phone goes on at 45° and twists to lock, so the roof sits
     outside the circle the phone's corners sweep (`r_tw`), and the cheeks only reach down as far
     as that circle allows. That's why the sides are short.
   - **Plenum** behind the phone: back plate + side rims + floor, open at the top. Air comes in
     through the hose spigot in the floor, flows up across the back of the phone and leaves around
     the phone edges and up through the roof slot. A floor notch takes the charging cable.
   - **Clamp ring** around the arm, split, with an M3 pinch screw. It is a closed ring, so it goes
     on with the puck off the arm (check that the puck's centre screw releases it).
2. **Vent scoop** (one print): a box over the top of the left centre-stack vent, held by two tabs
   that slide between louvres and hook behind one. Hose spigot on top. The rest of the vent still
   blows on the driver.
3. **Hose** between the two spigots: flexible, so the ball joint still adjusts. Unplug it in winter.

## Parameters to measure
Edit the `expression` of each in `sprinter-phone-hood.json`, then `./build.sh --fast`. Everything
else (roof height, cheeks, clamp, spigots) follows. Placeholder values are marked UNVERIFIED in the
script's comments.

| Parameter | Placeholder | Measure |
|---|---|---|
| `ph_w`, `ph_h` | 83, 168 | phone in its case, width and height |
| `ph_t` | 12 | back of case to screen |
| `ph_dz` | 0 | phone centre above the puck centre (0 if the adaptor is centred) |
| `puck_t` | 18 | puck face to the back of the puck where the arm starts |
| `arm_d` | 16 | arm diameter just behind the puck |
| `clamp_l` | 12 | keep shorter than the bare arm between puck and ball joint |
| `vent_w` | 55 | vent opening width inside the bezel |
| `louvre_set` | 8 | bezel face back to the front edge of the louvres |
| `louvre_depth` | 10 | louvre blade depth, front to back |
| `louvre_gap` | 6 | clear gap between two louvres |
| `tab_z` | 6 | top edge of the opening down to the centre of the gap the tabs go into |
| `hose_id` | 15.9 | the hose you buy |
| `inlet_x` | −(ph_w/2 − 14) | where the hose enters the plenum floor (−X = your right, toward the vent) |

Design choices you can change: `visor_d` (roof reach in front of the screen), `roof_w`,
`scoop_h` (how much of the vent is captured), `twist_clr`, `wall`.

Model axes: origin on the puck axis at the puck face; +Y toward the driver, +Z up, +X to the driver's left (the vent is at −X).

## Requirements
- Fits (all to be measured; calipers for vent and mount):
  - [x] Photos (2026-11-08, night, no scale; kept out of git): puck sits on a ball-joint arm on the
        right edge of the instrument hood. The vent is the left centre-stack vent below and right of
        it: tall rectangle, about 9 horizontal louvres, a centre adjuster tab, and the shut-off
        thumbwheel below. Air would have to go up and left to the phone.
  - [ ] Photo of the mount base with the phone off (top/side), and one with the phone on
  - [ ] Quad Lock mount model; base L × W; screw spacing and size; dash-to-puck-face height
  - [ ] Phone + case + adaptor: H × W × T; portrait / landscape / rotates; wireless charging?
  - [ ] Vent: which one; centre offset to mount centre (x, y, z); opening size; louvre thickness,
        gap and set-back; swivels?
  - [ ] Dash surface shape/slope under the mount
  - [ ] Sun direction: windshield (above) or side window
- Must not block the instrument cluster or the road view.
- Environment: vehicle dash in direct sun, high heat, UV.
- Plan: fit-test print of the vent clip + mount footprint before the full part.

## Files
- `sprinter-phone-hood.json`: source of truth (SolidCraft script). `./build.sh` regenerates everything else.
- `out/snap-iso.png`, `out/snap-rear.png`, `out/snap-driver-side.png`: views.

## Log
- 2026-11-08: part created; concept agreed; waiting for measurements.
- 2026-11-08: v0 modelled with placeholder dims (Hood 86 228 mm³, VentScoop 22 714 mm³; both match
  hand calculations). Checked it rebuilds cleanly with other phone/arm/vent sizes. Next: measure,
  then fit-test print of the clamp ring and the scoop tabs.
