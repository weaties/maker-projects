# HM-001 · GEB trip-let

The object on the cover of Hofstadter's *Gödel, Escher, Bach*: a block carved so its shadows along the
three axes spell G, E and B. Two of them, as on the cover: **GEB** (G seen from +X, E from the front,
B from above) and **EGB** (E and G swapped). A desk piece; shine a light along an axis to see each letter.

| | |
|---|---|
| Status | designed, sliced; not printed |
| Process | 3D print (Bambu Lab X2D, 0.4 nozzle) |
| Material | PLA (anything; a light colour shows the shadows best) |
| Fasteners / hardware | none |
| Key dims | 50 mm cube each (`S` in `gen.py`) |

## How it's made
Each letter outline (Arial Rounded MT Bold, close to the cover's lettering) is flattened to a polygon,
stretched to fill an S × S square, then extruded through the cube along its own axis. The three prisms are
intersected. The trip-let trick only works if every row and column of each letter meets the other two. These
bold letters do: the front, top and side snapshots show complete letters (`out/snap-front.png`,
`snap-top.png`; `snap-right.png` shows both blocks' side letters overlaid).

`gen.py` writes `geb-triplet.json`. Change `S`, the font or the letters there, then run `./gen.py && ./build.sh`.
The letters are polygons, not `sketch.text`: SolidCraft 0.30.1 fails (`boolean Intersect: no result`) when
intersecting text glyphs that `solid.scale` has stretched non-uniformly. If that gets fixed, the script could
use `sketch.text` directly and keep `S` as a live parameter.

| Body | Volume | Mass (PLA solid) | Bbox |
|---|---|---|---|
| GEB | 27 266 mm³ | 33.8 g | 50 × 50 × 50, centred on the origin |
| EGB | 25 878 mm³ | 32.1 g | 50 × 50 × 50, centre at X = 75 |

## Printing
Print as modelled, B face down, with tree supports (the counters of the G and the gaps of the E need them).
`slice.json`: PLA, 0.2 mm, 3 walls, 15 % infill, tree(auto) supports. About 1 h 28 min and 29 g each on the X2D.
Pull the supports out of the inner pockets carefully; the thin E arms are the weak spot.

## Files
- `gen.py`: generator (font → polygons → script). `geb-triplet.json`: the generated SolidCraft script.
- `print.json` → `print/geb.3mf`, `print/egb.3mf` (+ STL); `slice.json` → Bambu print jobs.

## Log
- 2026-11-09: v1 designed and sliced (S = 50 mm).
