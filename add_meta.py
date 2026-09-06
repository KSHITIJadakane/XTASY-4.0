import glob
import re

meta_tags = """
  <meta property="og:title" content="XTASY 4.0 — Quest Room | Official Experience" />
  <meta property="og:description" content="Step inside the ultimate XTASY 4.0 escape room. Test your limits, follow the rules of survival, and hold the card. The game begins now." />
  <meta property="og:image" content="https://xtasy-zeta.vercel.app/assets/IMG_9183.png" />
  <meta property="og:url" content="https://xtasy-zeta.vercel.app/" />
  <meta property="og:type" content="website" />
  
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="XTASY 4.0 — Quest Room | Official Experience" />
  <meta name="twitter:description" content="Step inside the ultimate XTASY 4.0 escape room. Test your limits, follow the rules of survival, and hold the card. The game begins now." />
  <meta name="twitter:image" content="https://xtasy-zeta.vercel.app/assets/IMG_9183.png" />
"""

def update_meta():
    for filename in glob.glob('*.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'og:title' not in content:
            # Replace the first occurrence of </head> with meta_tags + </head>
            content = content.replace('</head>', meta_tags + '\n</head>', 1)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"Already updated {filename}")

update_meta()
