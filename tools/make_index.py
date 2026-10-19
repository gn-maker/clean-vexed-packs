"""Write index.json, the list of packs that Baffled's Get Packs reads.

Run from the repository root after changing packs/: python3 tools/make_index.py
"""
import glob, hashlib, json, os, re
from urllib.parse import quote

BASE = 'https://raw.githubusercontent.com/gn-maker/clean-vexed-packs/main/'
CREDITS = ('From Vexed by James A. McCombe and the Vexed Development Team, as released in Vexed for Windows by '
           'John G. Zvonar. Licensed under the GNU GPL, version 2: github.com/gn-maker/clean-vexed-packs')


def natural(name):
    """Variety 2 before Variety 10."""
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', name)]


packs = []
for path in sorted(glob.glob('packs/*.ini'), key=natural):
    data = open(path, 'rb').read()
    text = data.decode('utf-8')
    author = re.search(r'^Author=(.*)$', text, re.M)
    packs.append({
        'name': os.path.basename(path)[:-4],
        'author': author.group(1).strip() if author else None,
        # A level starts at each board= line, as Baffled's parser counts them.
        'levels': len(re.findall(r'^board=', text, re.M | re.I)),
        'size': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
        'url': BASE + quote(path),
    })

with open('index.json', 'w') as f:
    json.dump({'credits': CREDITS, 'packs': packs}, f, indent=2, ensure_ascii=False)
    f.write('\n')
print(f'{len(packs)} packs, {sum(p["levels"] for p in packs)} levels')
