#!/usr/bin/env bash
# Rebuild everything for this part from pi5-case.json (the source of truth).
#   ./build.sh            design + CAD exports + print files + images + drawings
#   ./build.sh --fast     skip the path-traced render
set -euo pipefail
cd "$(dirname "$0")"
find_hub() { local d="$PWD"; while [[ "$d" != / ]]; do [[ -f "$d/.maker-hub" ]] && { echo "$d"; return; }; d="$(dirname "$d")"; done
  echo "build.sh: no .maker-hub above $PWD; clone this repo into <hub>/projects/ or set MAKER_HUB" >&2; return 1; }
HUB="${MAKER_HUB:-$(find_hub)}"; SC="$HUB/tools/bin/solidcraft-cli"
NAME=pi5-case
mkdir -p out print

echo "== model"
"$SC" run "$NAME.json" --save "$NAME.sc" --out "$NAME.step" --quiet
"$SC" eval "$NAME.sc" --json-out out/measure.json
python3 - <<'PY'
import json; d=json.load(open("out/measure.json"))
for b in d["bodies"]:
    print(f'  {b["name"]:6} {b["volume_mm3"]:10.1f} mm3  {b.get("mass_g",0):6.1f} g  faces={b["faces"]}  closed={b["closed"]}')
PY

echo "== print files (print/)"
"$SC" run print.json --in "$NAME.sc" --quiet

echo "== images (out/)"
"$SC" snapshot "$NAME.sc" --out out/snap-base-iso.png --width 1200 --height 780 --no-grid --no-axes \
  --camera '{"target":[0,0,12],"yaw":-0.6,"pitch":0.6,"distance":150}' --body 'Lid:opacity=0' >/dev/null
"$SC" snapshot "$NAME.sc" --out out/snap-rear-xray.png --width 1400 --height 900 --no-grid --no-axes \
  --camera '{"target":[0,0,14],"yaw":2.5,"pitch":0.55,"distance":160}' --body 'Lid:opacity=0.25' >/dev/null
"$SC" snapshot "$NAME.sc" --out out/snap-section.png --width 1400 --height 900 --no-grid --no-axes \
  --camera '{"target":[0,0,14],"yaw":2.85,"pitch":0.3,"distance":150}' \
  --section '{"plane":{"origin":[0,24.5,0],"normal":[0,1,0]}}' >/dev/null
if [[ "${1:-}" != "--fast" ]]; then
  "$SC" render "$NAME.sc" --out out/render-hero.png --width 1600 --height 1000 --progressive --samples 128 --overwrite --timeout 400 >/dev/null
fi

echo "== drawings (out/drawing-*.svg|pdf|png)"
uv run -q "$HUB/tools/drawing/drawing.py" drawing.json
