#!/usr/bin/env python3
"""Validate scene manifest and total target runtime."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'scenes/manifest.json').read_text())
expected=0
for scene in data['scenes']:
 assert scene['start_seconds']==expected, f"Gap/overlap: {scene['id']}"
 assert scene['duration_seconds']>0
 assert (root/'scenes'/scene['id']/'README.md').exists()
 expected+=scene['duration_seconds']
assert expected==data['runtime_seconds']==1500
print(f"OK: {len(data['scenes'])} scenes, {expected//60} minutes, {data['fps']} fps")
