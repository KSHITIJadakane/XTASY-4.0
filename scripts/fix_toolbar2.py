import os

def fix_toolbar_error(filename):
    filepath = os.path.join(r"c:\Users\rajur\OneDrive\Desktop\xtasy", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Re-declare logo
    fix_str = """
        const logo = document.querySelector('.logo');
        // Close toolbar when clicking outside
        document.addEventListener('click', (e) => {
    """
    
    content = content.replace("// Close toolbar when clicking outside\n        document.addEventListener('click', (e) => {", fix_str)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for page in ['automystica.html', 'hackthehardware.html', 'visionexpo.html', 'triguna.html']:
    fix_toolbar_error(page)

