import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML structure
old_html = '''<div class="rr-dy">
            <div class="rr-dy-t">DY</div>
            <div class="rr-toplay">TO PLAY?</div>
            <button class="btn-cta" data-cursor="triangle" style="margin-top:6px" onclick="openModal()">Play Game</button>
          </div>'''
new_html = '''<div class="rr-dy">
            <div class="rr-dy-t">DY</div>
            <div class="rr-dy-extras">
              <div class="rr-toplay">TO PLAY?</div>
              <button class="btn-cta" data-cursor="triangle" style="margin-top:6px" onclick="openModal()">Play Game</button>
            </div>
          </div>'''
content = content.replace(old_html, new_html)

# 2. Update CSS for rr-dy to have position:relative and remove gap:12px
content = content.replace(
    ".rr-dy{display:flex;flex-direction:column;align-items:flex-start;gap:12px;opacity:0;transform:translateX(42px);transition:all .92s var(--ease) .3s}",
    ".rr-dy{display:flex;flex-direction:column;align-items:flex-start;opacity:0;transform:translateX(42px);transition:all .92s var(--ease) .3s;position:relative}"
)

# 3. Add CSS for .rr-dy-extras after .rr-dy-t
content = content.replace(
    ".rr-toplay{",
    ".rr-dy-extras{position:absolute;top:100%;left:0;margin-top:12px;display:flex;flex-direction:column;gap:12px;width:max-content}\n    .rr-toplay{"
)

# 4. Add CSS for mobile
content = content.replace(
    ".rr-dy{align-items:center;text-align:center}",
    ".rr-dy{align-items:center;text-align:center}\n      .rr-dy-extras{position:static;margin-top:16px;align-items:center}"
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Alignment fixed!")
