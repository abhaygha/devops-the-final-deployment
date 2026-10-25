#!/usr/bin/env python3
"""Generate editable scene tracking CSV; preserves existing CSV unless --force."""
import csv,json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=root/'docs/shotlist.csv'
if out.exists() and '--force' not in sys.argv:
 print(f'Exists: {out} (pass --force to overwrite)');raise SystemExit(0)
data=json.loads((root/'scenes/manifest.json').read_text())
with out.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['scene_id','scene_title','start_seconds','duration_seconds','status','clip_path','voice_path','cost_aed','notes'])
 for s in data['scenes']:w.writerow([s['id'],s['title'],s['start_seconds'],s['duration_seconds'],'planned','','',0,''])
print(out)
