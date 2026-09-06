import glob

def update_meta_urls():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        if 'https://xtasy-zeta.vercel.app/assets/IMG_9183.png' in content:
            content = content.replace('https://xtasy-zeta.vercel.app/assets/IMG_9183.png', 'https://xtasy-4-0.vercel.app/assets/IMG_9183.png')
            changed = True
        
        if 'https://xtasy-zeta.vercel.app/' in content:
            content = content.replace('https://xtasy-zeta.vercel.app/', 'https://xtasy-4-0.vercel.app/')
            changed = True
            
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

update_meta_urls()
