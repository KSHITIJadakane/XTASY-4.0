import glob
import re

files_info = {
    'index.html': {
        'url': 'https://xtasy-4-0.vercel.app/',
        'title': 'XTASY 4.0 — Quest Room | Department of Industrial IoT',
        'desc': 'XTASY 4.0 — The ultimate high-stakes tech arena & quest room experience, presented by the Department of Industrial IoT (IIoT). Test your limits, outsmart the challenge, and hold the card. The game begins now!'
    },
    'events.html': {
        'url': 'https://xtasy-4-0.vercel.app/events.html',
        'title': 'XTASY 4.0 — All Events & Arena Games | Dept. of IIoT',
        'desc': 'XTASY 4.0 — Explore all high-stakes arena events, presented by the Department of Industrial IoT (IIoT): Automystica, Hack The Hardware, Triguna, and Vision Expo. Adapt and conquer!'
    },
    'automystica.html': {
        'url': 'https://xtasy-4-0.vercel.app/automystica.html',
        'title': 'AUTOMYSTICA — XTASY 4.0 | Dept. of Industrial IoT',
        'desc': 'XTASY 4.0 presents AUTOMYSTICA by the Department of Industrial IoT (IIoT). Master IoT circuits, adapt to unexpected twists, and engineer an automated system that survives.'
    },
    'hackthehardware.html': {
        'url': 'https://xtasy-4-0.vercel.app/hackthehardware.html',
        'title': 'HACK THE HARDWARE — XTASY 4.0 | Dept. of Industrial IoT',
        'desc': 'XTASY 4.0 presents HACK THE HARDWARE by the Department of Industrial IoT (IIoT). Debug faulty circuits, crack encrypted breadboards, and rewire logic under extreme pressure.'
    },
    'triguna.html': {
        'url': 'https://xtasy-4-0.vercel.app/triguna.html',
        'title': 'TRIGUNA — XTASY 4.0 | Dept. of Industrial IoT',
        'desc': 'XTASY 4.0 presents TRIGUNA by the Department of Industrial IoT (IIoT). Three intense rounds of coding, logic, and rapid problem-solving. Only the sharpest minds survive.'
    },
    'visionexpo.html': {
        'url': 'https://xtasy-4-0.vercel.app/visionexpo.html',
        'title': 'VISION EXPO — XTASY 4.0 | Dept. of Industrial IoT',
        'desc': 'XTASY 4.0 presents VISION EXPO by the Department of Industrial IoT (IIoT). Showcase breakthrough engineering prototypes, hardware innovations, and futuristic tech to industry judges.'
    }
}

image_url = 'https://xtasy-4-0.vercel.app/assets/xtasy_logo.jpg'

for fn, info in files_info.items():
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <title> and top <meta name="description"> if present
    content = re.sub(r'<title>.*?</title>', f"<title>{info['title']}</title>", content)
    content = re.sub(r'<meta name="description" content=".*?"\s*/?>', f'<meta name="description" content="{info["desc"]}"/>', content)

    # 2. Re-create clean meta tags block
    meta_block = f"""  <!-- Favicon & Touch Icon -->
  <link rel="icon" type="image/jpeg" href="assets/xtasy_logo.jpg" />
  <link rel="apple-touch-icon" href="assets/xtasy_logo.jpg" />

  <!-- Open Graph / Facebook / WhatsApp -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="XTASY 4.0" />
  <meta property="og:url" content="{info['url']}" />
  <meta property="og:title" content="{info['title']}" />
  <meta property="og:description" content="{info['desc']}" />
  <meta property="og:image" content="{image_url}" />
  <meta property="og:image:secure_url" content="{image_url}" />
  <meta property="og:image:type" content="image/jpeg" />
  <meta property="og:image:width" content="1024" />
  <meta property="og:image:height" content="1024" />
  <meta property="og:image:alt" content="XTASY 4.0 Official Logo" />

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="{info['url']}" />
  <meta name="twitter:title" content="{info['title']}" />
  <meta name="twitter:description" content="{info['desc']}" />
  <meta name="twitter:image" content="{image_url}" />"""

    # Remove existing OG & Twitter tags & link icons right before </head>
    content = re.sub(r'<!--\s*(?:Favicon|Open Graph|Twitter)[^>]*-->', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\s*<link rel="(?:icon|apple-touch-icon)"[^>]+>', '', content)
    content = re.sub(r'\s*<meta property="og:[^"]+"[^>]+>', '', content)
    content = re.sub(r'\s*<meta name="twitter:[^"]+"[^>]+>', '', content)

    # Insert meta block right before </head>
    content = content.replace('</head>', f'\n{meta_block}\n</head>')

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fn}: title & catchy description applied.")

print("All files updated successfully.")
