#!/usr/bin/env python3
"""
Run a small set of repository-specific checks:
- Verify required anchor ids exist in index.html
- Run the image reference checker

Usage: python3 scripts/check_site.py
"""
import sys
from pathlib import Path
from html.parser import HTMLParser
import subprocess

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'

required_ids = ['home', 'portfolio', 'about', 'contact', 'year', 'show-more-btn', 'more-projects']

class IDCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == 'id' and v:
                self.ids.add(v)

if not INDEX.exists():
    print('index.html not found in repo root')
    sys.exit(3)

collector = IDCollector()
collector.feed(INDEX.read_text(encoding='utf-8', errors='ignore'))

missing = [i for i in required_ids if i not in collector.ids]
if missing:
    print('Missing required ids in index.html:')
    for m in missing:
        print(' -', m)

# Run image check script
print('\nRunning image reference checks...')
res = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'check_images.py')])

if res.returncode != 0 or missing:
    print('\nSite checks failed.')
    sys.exit(4)

print('\nAll site checks passed.')
sys.exit(0)
