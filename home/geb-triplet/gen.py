#!/usr/bin/env -S uv run -q --with fonttools python
"""Writes geb-triplet.json: Hofstadter's GEB trip-let (book cover of Godel, Escher, Bach).

Each letter's font outline is flattened to a polygon and stretched to fill an S x S square, extruded along
its own axis, and the three prisms are intersected, so the block's shadows along X, Y and Z are the letters.
Two trip-lets, like the cover: GEB (G seen from +X, E from -Y, B from +Z) and EGB beside it.
(Text glyphs are drawn as polygons because the kernel fails intersecting stretched spline glyph faces.)
Run: ./gen.py && ./build.sh
"""
import json
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

S = 50.0         # cube size, mm: each shadow letter fills S x S
SEG = 0.8        # max chord length when flattening curves, mm (in font units scaled to S)
FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
GAP = 1.5 * S    # centre spacing of the two trip-lets along X

font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()

def contours(ch):
    """Glyph outline as closed polylines (font units), quadratic curves sampled finely."""
    pen = RecordingPen(); gs[cmap[ord(ch)]].draw(pen)
    out, cur = [], []
    for op, pts in pen.value:
        if op == "moveTo": cur = [pts[0]]
        elif op == "lineTo": cur.append(pts[0])
        elif op == "qCurveTo":  # TrueType: implied on-curve points between consecutive off-curve ones
            p0 = cur[-1]; offs = list(pts[:-1]); end = pts[-1]
            for i, c in enumerate(offs):
                e = end if i == len(offs) - 1 else ((c[0] + offs[i+1][0]) / 2, (c[1] + offs[i+1][1]) / 2)
                for k in range(1, 25):
                    t = k / 24
                    cur.append(((1-t)**2*p0[0] + 2*(1-t)*t*c[0] + t*t*e[0], (1-t)**2*p0[1] + 2*(1-t)*t*c[1] + t*t*e[1]))
                p0 = e
        elif op in ("closePath", "endPath"): out.append(cur); cur = []
    return out

def letter_polys(ch):
    dense = contours(ch)
    allp = [p for c in dense for p in c]
    x0 = min(p[0] for p in allp); x1 = max(p[0] for p in allp)
    y0 = min(p[1] for p in allp); y1 = max(p[1] for p in allp)
    sx = S / (x1 - x0); sy = S / (y1 - y0)
    polys = []
    for c in dense:
        q = [((x - x0) * sx - S/2, (y - y0) * sy - S/2) for x, y in c]
        # thin to SEG chord, keeping corners: drop a point if it's close to the previous kept one and nearly collinear
        kept = [q[0]]
        for i in range(1, len(q)):
            a, b = kept[-1], q[i]
            nxt = q[(i + 1) % len(q)]
            d = ((b[0]-a[0])**2 + (b[1]-a[1])**2) ** .5
            if d < 0.05: continue
            cross = abs((b[0]-a[0])*(nxt[1]-a[1]) - (b[1]-a[1])*(nxt[0]-a[0]))
            dn = ((nxt[0]-a[0])**2 + (nxt[1]-a[1])**2) ** .5
            if dn < SEG and dn > 0 and cross / dn < 0.02: continue   # within 0.02 mm of the chord
            kept.append(b)
        if ((kept[0][0]-kept[-1][0])**2 + (kept[0][1]-kept[-1][1])**2) ** .5 < 0.05: kept.pop()
        polys.append([[round(x, 3), round(y, 3)] for x, y in kept])
    return polys

PLANES = {  # sketch x/y -> world, chosen so each shadow reads correctly from outside
    "side":  {"origin": [0, 0, 0], "x_dir": [0, 1, 0], "y_dir": [0, 0, 1]},   # seen from +X
    "front": {"origin": [0, 0, 0], "x_dir": [1, 0, 0], "y_dir": [0, 0, 1]},   # seen from -Y
    "top":   "XY",                                                             # seen from +Z
}

def letter(ch, plane, name, dx):
    pl = PLANES[plane]
    if dx:
        pl = dict(pl) if isinstance(pl, dict) else {"origin": [0, 0, 0], "x_dir": [1, 0, 0], "y_dir": [0, 1, 0]}
        pl["origin"] = [dx, 0, 0]
    cmds = [{"command": "sketch.create", "params": {"plane": pl, "name": name + "Sketch"}}]
    for poly in letter_polys(ch):
        cmds.append({"command": "sketch.line", "params": {"points": poly, "closed": True, "infer": False}})
    cmds += [{"command": "sketch.finish", "params": {}},
             {"command": "solid.extrude", "params": {"distance": 2 * S, "direction": "symmetric",
                                                      "name": name, "body_name": name}}]
    return cmds

def triplet(a, b, name, dx):
    n1, n2, n3 = f"{name}_{a}", f"{name}_{b}", f"{name}_B"
    return (letter(a, "side", n1, dx) + letter(b, "front", n2, dx) + letter("B", "top", n3, dx) + [
        {"command": "solid.combine", "params": {"target": n1, "tools": [n2], "operation": "intersect", "name": name + "_x1"}},
        {"command": "solid.combine", "params": {"target": n1, "tools": [n3], "operation": "intersect", "name": name + "_x2"}},
        {"command": "body.rename", "params": {"body": n1, "name": name}}])

cmds = triplet("G", "E", "GEB", 0) + triplet("E", "G", "EGB", GAP)
cmds += [
{"command": "material.assign", "params": {"bodies": ["GEB", "EGB"], "material": "PLA"}}]
json.dump({"commands": cmds}, open("geb-triplet.json", "w"), indent=1)
print(sum(len(c["params"]["points"]) for c in cmds if c["command"] == "sketch.line"), "polygon points")
