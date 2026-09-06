import glob
import re

for fn in sorted(glob.glob('*.html')):
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"=== {fn} ===")
    tags = re.findall(r'<meta (?:property|name)=["\'][^"\']+["\'][^>]+>', content)
    for t in tags:
        if any(k in t for k in ['image', 'title', 'url', 'type']):
            print(" ", t)
