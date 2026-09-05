import os

filepath = r"c:\Users\rajur\OneDrive\Desktop\xtasy\make_pages.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing backticks in make_pages.py
old_str = """        toolbar.innerHTML = 
          <div class="xt-item" onclick="window.history.back()">"""
new_str = """        toolbar.innerHTML = 
          <div class="xt-item" onclick="window.history.back()">"""
content = content.replace(old_str, new_str)

old_str_end = """          </div>
        ;"""
new_str_end = """          </div>
        ;"""
content = content.replace(old_str_end, new_str_end)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

