import glob

def update_meta_urls():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        if 'IMG_9183.png' in content and 'og:image' in content:
            content = content.replace('IMG_9183.png', 'xtasy_logo.jpg')
            changed = True
            
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

if __name__ == '__main__':
    update_meta_urls()
