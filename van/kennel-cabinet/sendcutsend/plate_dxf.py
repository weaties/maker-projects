"""Clean cut DXF for the VN-002 track plate and its curve insert (both plates are the same flat part;
one is flipped). The hang curve cuts an insert loose from the plate; it is screwed down on its own.
Mirrors the plate features in kennel-cabinet.json; dims in inches, written in mm.
Run: uv run --with ezdxf --with shapely sendcutsend/plate_dxf.py sendcutsend/vn002-track-plate.dxf"""
import math, sys, ezdxf
from shapely.geometry import Point, LineString, box
from shapely.ops import unary_union

IN = 25.4
W, H, t = 15, 32, 0.75
pin_z, pitch, band_m, drop_front, edge, drop = 1.5, 3, 1.25, 1.25, 0.75, 9.3125
hang_drop, r = 0, 0.25           # hang pivot at the top of the drop slot
slot_w = 0.375 + 0.15 / IN
scr_d = 0.164          # SendCutSend #6 82 deg countersink: draw the pilot (minor) diameter
RES = 256

z1, z2 = H - pin_z, H - pin_z - pitch            # track centre lines
x0, xe = -W / 2 + 0.75, W / 2 - edge             # track start, drop slot line
zb = z2 - drop                                   # drop slot bottom (lower pin at the lowest desk)
zc = H - pin_z - hang_drop                       # hang pivot: upper pin here
za = zc - pitch                                  # hang curve starts here (lower pin)
zb0 = H - pin_z - pitch - band_m                 # band bottom
ztop = H - t
xd0 = W / 2 - edge - drop_front                  # drop leg front edge
zbot = zb - 1                                    # plate bottom


def round_convex(poly, cx, cz, sx, sz):
    """Round a convex corner at (cx, cz); (sx, sz) points into the material."""
    sq = box(min(cx, cx + sx * r), min(cz, cz + sz * r), max(cx, cx + sx * r), max(cz, cz + sz * r))
    return poly.difference(sq).union(Point(cx + sx * r, cz + sz * r).buffer(r, RES).intersection(sq))


def round_concave(poly, cx, cz, sx, sz):
    """Fill a concave corner at (cx, cz); (sx, sz) points into the empty quadrant."""
    sq = box(min(cx, cx + sx * r), min(cz, cz + sz * r), max(cx, cx + sx * r), max(cz, cz + sz * r))
    return poly.union(sq.difference(Point(cx + sx * r, cz + sz * r).buffer(r, RES)))


o = unary_union([box(-W / 2, zb0, W / 2, ztop), box(xd0, zbot, W / 2, zb0 + 0.01)])
o = round_concave(o, xd0, zb0, -1, -1)           # leg meets band
o = round_convex(o, xd0, zbot, 1, 1)             # leg bottom front

arc = LineString([(xe + pitch * math.cos(a), zc + pitch * math.sin(a))
                  for a in [math.radians(-90 - 90 * i / 512) for i in range(513)]])
# drop slot runs out through the top edge so the lid drops in from above
sl = unary_union([LineString(p).buffer(slot_w / 2, RES) for p in (((x0, z1), (xe, z1)), ((x0, z2), (xe, z2)), ((xe, H), (xe, zb)))]
                 + [arc.buffer(slot_w / 2, RES)])

zm, zl, zs = H - pin_z - pitch / 2, H - pin_z - pitch - band_m / 2 - 0.125, (z1 + slot_w / 2 + ztop) / 2
xa, xdh = W / 2 - (edge - slot_w / 2) / 2, W / 2 - edge - drop_front / 2 - 0.125
holes = [(x, zm) for x in (-W / 2 + t / 2, -3.5, 0, 3.5, xa)]
holes += [(x, zl) for x in (-W / 2 + t / 2, -3.5, 0, 3.5, xa)]
holes += [(x, zs) for x in (-3.5, 0, 3.5, xa)]                     # top strip (open at the aft end)
holes += [(xe - 0.75, zc - 0.75), (xe - 1.5, zc - 1.5)]              # curve insert
holes += [(x, z) for z in (23.875, 21.5, 19.125, zb + 0.0625) for x in (xdh, xa)]  # leg
hole_u = unary_union([Point(p).buffer(scr_d / 2, RES) for p in holes])
assert hole_u.intersection(sl).area == 0 and o.contains(hole_u)
net = o.difference(sl).difference(hole_u)
body = o.difference(sl)                          # outline with the slots (the drop slot opens through the top edge)
parts = sorted(getattr(body, "geoms", [body]), key=lambda g: -g.area)
assert len(parts) == 2, f"expected the plate and one curve insert, got {len(parts)} pieces"
print("pieces: plate %.4f in2, insert %.4f in2 (bounds %s)" % (parts[0].area, parts[1].area, [round(v, 3) for v in parts[1].bounds]))
print(f"holes {len(holes)}  outline {o.area:.4f} in2  slots {o.intersection(sl).area:.4f} in2  net {net.area:.4f} in2  bounds {o.bounds}")

doc = ezdxf.new("R2010"); doc.header["$INSUNITS"] = 4; m = doc.modelspace()
ox, oz = -W / 2, zbot                            # DXF origin at the plate's lower front corner
f = lambda x, z: ((x - ox) * IN, (z - oz) * IN)
for ring in [r_ for g in parts for r_ in (g.exterior, *g.interiors)]:
    m.add_lwpolyline([f(*p) for p in ring.simplify(1e-5).coords], close=True)
for p in holes:
    m.add_circle(f(*p), scr_d / 2 * IN)
if len(sys.argv) > 1:
    doc.saveas(sys.argv[1])
