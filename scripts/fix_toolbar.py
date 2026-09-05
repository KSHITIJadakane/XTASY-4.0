import os
import re

def fix_toolbar(filename):
    filepath = os.path.join(r"c:\Users\rajur\OneDrive\Desktop\xtasy", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the global toggle function in the script block if it's not already there
    toggle_script = """
    <script>
      function toggleToolbar(e) {
        if(e) e.stopPropagation();
        const toolbar = document.getElementById('xtasy-toolbar');
        if(toolbar) toolbar.classList.toggle('active');
      }
    </script>
    """
    
    if "function toggleToolbar" not in content:
        content = content.replace("</main>", toggle_script + "</main>")

    # Replace the inline onclick for the logo
    # The logo might have onclick="goTo('hero')"
    content = re.sub(r'<div class="logo"[^>]*>', '<div class="logo" onclick="toggleToolbar(event)" style="cursor:pointer; z-index:1001; position:relative;">', content)

    # Let's ensure the JS that was added in DOMContentLoaded doesn't conflict
    # We can just remove the old eventListener part. 
    # Actually, the old script has:
    # logo.removeAttribute('onclick');
    # logo.addEventListener('click', ...
    # Let's just remove that old block by replacing it with nothing.
    bad_js = """const logo = document.querySelector('.logo');
        if (logo) {
          // Remove potential existing onclick attribute behaviors
          logo.removeAttribute('onclick');
          logo.style.cursor = 'pointer';
          
          logo.addEventListener('click', (e) => {
            e.stopPropagation();
            toolbar.classList.toggle('active');
          });
        }"""
    
    content = content.replace(bad_js, "")
    
    # Also update the click outside logic to reference the toggle function
    # Wait, the click outside logic was:
    # if (!toolbar.contains(e.target) && (!logo || !logo.contains(e.target))) {
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for page in ['automystica.html', 'hackthehardware.html', 'visionexpo.html', 'triguna.html']:
    fix_toolbar(page)

