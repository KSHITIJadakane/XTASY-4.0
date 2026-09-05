import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('.cctv-scanlines { .cctv-scanlines {', '.cctv-scanlines {')
content = content.replace('z-index: 50;0;', 'z-index: 50;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS syntax errors fixed!")
