#!/usr/bin/env python3
"""Optional FFmpeg concat for already-rendered compatible MP4 clips.

Usage: python scripts/assemble_movie.py clips.txt video/final/movie.mp4
clips.txt contains one absolute or relative video path per line. Clips must
have compatible codecs, resolution, frame rate and audio layout. For complex
mixing and transitions, use a non-linear editor instead.
"""
import subprocess,sys,tempfile
from pathlib import Path
if len(sys.argv)!=3:raise SystemExit('Usage: assemble_movie.py clips.txt output.mp4')
files=[Path(s.strip()).resolve() for s in Path(sys.argv[1]).read_text().splitlines() if s.strip()]
if not files or any(not p.is_file() for p in files):raise SystemExit('Missing clips')
out=Path(sys.argv[2]).resolve();out.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory() as d:
 listing=Path(d)/'concat.txt'
 listing.write_text(''.join("file '"+str(p).replace("'","'\\''")+"'\n" for p in files))
 subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(out)],check=True)
print(out)
