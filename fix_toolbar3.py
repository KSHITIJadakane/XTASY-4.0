import os
import re

def run_immediately(filename):
    filepath = os.path.join(r"c:\Users\rajur\OneDrive\Desktop\xtasy", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace:
    # document.addEventListener('DOMContentLoaded', () => {
    # with:
    # (function() {
    
    # And the matching }); with })();
    
    content = content.replace("document.addEventListener('DOMContentLoaded', () => {", "(function() {")
    
    # The matching closing bracket is right before </script>
    # There are two </script> tags in the main block now (one for toolbar append, one for toggleToolbar)
    # The first script block is:
    #     });
    #   </script>
    
    content = content.replace("});\n    </script>", "})();\n    </script>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for page in ['automystica.html', 'hackthehardware.html', 'visionexpo.html', 'triguna.html']:
    run_immediately(page)

