"""Clean cut DXF for the VN-002 track plate (both plates are the same flat part; one is flipped).
Mirrors the plate features in kennel-cabinet.json; dims in inches, written in mm.
Run: uv run --with ezdxf --with shapely sendcutsend/plate_dxf.py sendcutsend/vn002-track-plate.dxf"""
import sys, ezdxf
from shapely.geometry import Point, LineString, box
from shapely.ops import unary_union
IN = 25.4
W, H, t = 15, 32, 0.75
pin_z, pitch, band_m, drop_front, edge, drop, r = 1.5, 3, 1.25, 1.25, 0.75, 9.3125, 0.25
slot_w = 0.375 + 0.15 / IN
scr_d = 0.164   # SendCutSend #6 82deg countersink: draw the minor dia
zb0 = H - pin_z - pitch - band_m            # band bottom 26.25
ztop = H - t                                # 31.25
xd0 = W/2 - edge - drop_front               # drop leg front 5.5
zbot = zb0 - (drop + 1 - band_m)            # 17.1875
# outline: band + drop leg, R0.25 at the inner corner (concave) and the drop leg's bottom-front corner (convex)
band = box(-W/2, zb0, W/2, ztop); leg = box(xd0, zbot, W/2, zb0 + 0.01)
o = unary_union([band, leg])
# convex corner: round by erode/dilate only that corner -> do explicitly
corner_sq = box(xd0, zbot, xd0 + r, zbot + r); corner_round = Point(xd0 + r, zbot + r).buffer(r, 256)
o = o.difference(corner_sq).union(corner_round.intersection(corner_sq))
concave = box(xd0 - r, zb0 - r, xd0, zb0).difference(Point(xd0 - r, zb0 - r).buffer(r, 256))
o = o.union(concave)
# slots: upper/lower track, drop slot
x0, xe = -W/2 + 0.75, W/2 - edge
z1, z2 = H - pin_z, H - pin_z - pitch
zs = z2 - drop
sl = unary_union([LineString(p).buffer(slot_w/2, 256) for p in (((x0, z1), (xe, z1)), ((x0, z2), (xe, z2)), ((xe, z1), (xe, zs)))])
zm, zl = H - pin_z - pitch/2, H - pin_z - pitch - band_m/2 - 0.125
xa, xdh = W/2 - (edge - slot_w/2)/2, W/2 - edge - drop_front/2 - 0.125
holes = [(x, z) for z in (zm, zl) for x in (-W/2 + t/2, -3.5, 0, 3.5, xa)]
for k in (1, 2, 3):
    zz = zb0 - k*(drop - band_m)/3.4; holes += [(xdh, zz), (xa, zz)]
net = o.difference(sl).difference(unary_union([Point(p).buffer(scr_d/2, 256) for p in holes]))
print(f"holes {len(holes)}  outline {o.area:.4f} in2  net {net.area:.4f} in2  x{net.bounds}")
# write: origin at the plate's bottom-left (front edge, band... min corner), mm
ox, oz = -W/2, zbot
doc = ezdxf.new("R2010"); doc.header["$INSUNITS"] = 4; m = doc.modelspace()
f = lambda x, z: ((x - ox) * IN, (z - oz) * IN)
for ring in [o.exterior, *[s.exterior for s in getattr(sl, "geoms", [sl])]]:
    m.add_lwpolyline([f(*p) for p in ring.coords], close=True)
for p in holes:
    m.add_circle(f(*p), scr_d/2 * IN)
doc.saveas(sys.argv[1])
