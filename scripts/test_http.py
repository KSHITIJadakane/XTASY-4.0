import urllib.request
import re

pages = ['index.html', 'events.html', 'automystica.html', 'hackthehardware.html', 'triguna.html', 'visionexpo.html']
all_assets = set()

for p in pages:
    url = f'http://localhost:8080/{p}'
    resp = urllib.request.urlopen(url)
    html = resp.read().decode('utf-8')
    assert resp.status == 200, f'Failed {url}'
    srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
    for s in srcs:
        if not s.startswith('http') and not s.startswith('data:'):
            all_assets.add(s)

print(f'Successfully loaded all {len(pages)} pages over HTTP 200!')
print(f'Checking {len(all_assets)} unique assets over HTTP...')
for a in sorted(all_assets):
    a_url = f'http://localhost:8080/{a}'
    resp = urllib.request.urlopen(a_url)
    print(f'  {resp.status} OK: {a}')

print('\nALL HTML PAGES AND REFERENCED ASSETS RETURN HTTP 200 OK OVER LOCAL SERVER!')
