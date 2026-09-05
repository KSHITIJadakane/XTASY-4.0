import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up bad injection
bad_section = '<section class="sec" id="ready" style="position: relative; overflow: hidden;">\n  <div class="cctv-scanlines"></div>\n  <div class="cctv-ui">\n    <div class="cctv-rec"><span class="rec-dot"></span> REC</div>\n    <div class="cctv-time">CAM 04 - 1999/10/29 23:45:00</div>\n  </div>'
if bad_section in content:
    content = content.replace(bad_section, '<section class="sec" id="ready">')

# 1b. Fallback cleanup just in case
content = content.replace('<section class="sec" id="ready" style="position: relative; overflow: hidden;">', '<section class="sec" id="ready">')
content = re.sub(r'^\s*<div class="cctv-scanlines"></div>\n\s*<div class="cctv-ui">\n\s*<div class="cctv-rec"><span class="rec-dot"></span> REC</div>\n\s*<div class="cctv-time">CAM 04 - 1999/10/29 23:45:00</div>\n\s*</div>\n', '', content, flags=re.MULTILINE)

# 2. Correct injection into .rr-mask
# The current mask looks like: <div class="rr-mask"><img src="assets/frontman_mask_hd.jpg" alt="Frontman Mask" class="frontman-feed"/></div>
new_mask = '''<div class="rr-mask">
  <div class="cctv-glitch-container">
    <img src="assets/frontman_mask_hd.jpg" alt="Frontman Mask" class="frontman-feed"/>
    <div class="cctv-scanlines"></div>
    <div class="cctv-ui">
      <div class="cctv-rec"><span class="rec-dot"></span> REC</div>
      <div class="cctv-time">CAM 04 - 1999/10/29 23:45:00</div>
    </div>
  </div>
</div>'''

# We need to replace the rr-mask div. Let's use a regex to be safe.
pattern = r'<div class="rr-mask">\s*<img src="assets/frontman_mask_hd\.jpg" alt="Frontman Mask"(?: class="frontman-feed")?/>\s*</div>'
content = re.sub(pattern, new_mask, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("CCTV Glitch fixed successfully!")
