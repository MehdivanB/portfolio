#!/usr/bin/env python3
"""
Check that all image files referenced from HTML and CSS exist in the repo.

Usage: python3 scripts/check_images.py
Exits with code 0 when all referenced files exist, non-zero otherwise.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

html_files = list(ROOT.glob('*.html'))
css_files = [ROOT / 'style.css'] if (ROOT / 'style.css').exists() else []

refs = set()

src_re = re.compile(r'src\s*=\s*"([^"]+)"')
url_re = re.compile(r'url\(\s*["']?([^"')]+)["']?\s*\)')

def collect_from_file(path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    for m in src_re.finditer(text):
        refs.add(m.group(1))
    for m in url_re.finditer(text):
        refs.add(m.group(1))

for f in html_files:
    collect_from_file(f)
for f in css_files:
    collect_from_file(f)

# Normalize and check
missing = []
for r in sorted(refs):
    # Ignore absolute URLs
    if r.startswith('http://') or r.startswith('https://') or r.startswith('data:'):
        continue
    # Strip query/hash
    r_clean = r.split('?', 1)[0].split('#', 1)[0]
    # Normalize relative paths
    p = (ROOT / r_clean).resolve() if not r_clean.startswith('/') else (Path(r_clean).resolve())
    if not p.exists():
        missing.append((r, p))

if missing:
    print('Missing referenced assets:')
    for r, p in missing:
        print(f' - {r} -> expected at {p}')
    sys.exit(2)
else:
    print('All referenced image/assets exist.')
    sys.exit(0)
