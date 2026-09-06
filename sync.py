import re, glob

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Extract from </main> to the end
after_main = re.search(r'(</main>.*)', idx, re.DOTALL).group(1)
# Extract CSS from <style> in index.html
styles = re.search(r'(<style>.*?</style>)', idx, re.DOTALL).group(1)

for f in glob.glob('*.html'):
    if f == 'index.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace after </main>
    content = re.sub(r'</main>.*', after_main, content, count=1, flags=re.DOTALL)
    # Replace styles
    content = re.sub(r'<style>.*?</style>', styles, content, count=1, flags=re.DOTALL)
    
    # ensure the watermark is there (after fx-scroll)
    if 'dept-watermark' not in content:
        content = content.replace('<div class="fx-scroll" id="fx-scroll"></div>', '<div class="fx-scroll" id="fx-scroll"></div>\n  <div class="dept-watermark">DEPARTMENT OF INDUSTRIAL IOT</div>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
