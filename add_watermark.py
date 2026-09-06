import glob

for f in glob.glob('*.html'):
    if f == 'index.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '<div class="dept-watermark">' not in content:
        content = content.replace('<div class="fx-scroll" id="fx-scroll"></div>', '<div class="fx-scroll" id="fx-scroll"></div>\n  <div class="dept-watermark">DEPARTMENT OF INDUSTRIAL IOT</div>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated', f)
    else:
        print('Already present in', f)
