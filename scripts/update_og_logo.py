import glob
import re

files_info = {
    'index.html': {
        'url': 'https://xtasy-4-0.vercel.app/',
        'title': 'XTASY 4.0 — Quest Room | Official Experience',
        'desc': 'Step inside the ultimate XTASY 4.0 escape room. Test your limits, follow the rules of survival, and hold the card. The game begins now.'
    },
    'events.html': {
        'url': 'https://xtasy-4-0.vercel.app/events.html',
        'title': 'XTASY 4.0 — All Events & Arena Games',
        'desc': 'Explore all XTASY 4.0 events: Automystica, Hack The Hardware, Triguna, and Vision Expo. Compete, adapt, and claim victory.'
    },
    'automystica.html': {
        'url': 'https://xtasy-4-0.vercel.app/automystica.html',
        'title': 'AUTOMYSTICA — XTASY 4.0 | Build. Adapt. Survive.',
        'desc': 'Master the elements of IoT, optimize your nodes, and build a system that outlasts the rest. The frontline of the Industrial IoT revolution starts here.'
    },
    'hackthehardware.html': {
        'url': 'https://xtasy-4-0.vercel.app/hackthehardware.html',
        'title': 'HACK THE HARDWARE — XTASY 4.0 | Circuit Combat',
        'desc': 'Debug faulty circuits, crack encrypted breadboards, and rewire logic under extreme pressure in XTASY 4.0.'
    },
    'triguna.html': {
        'url': 'https://xtasy-4-0.vercel.app/triguna.html',
        'title': 'TRIGUNA — XTASY 4.0 | The Triple Domain Trial',
        'desc': 'Three rounds of coding, logic, and rapid problem-solving. Only the sharpest minds survive all three tiers of Triguna.'
    },
    'visionexpo.html': {
        'url': 'https://xtasy-4-0.vercel.app/visionexpo.html',
        'title': 'VISION EXPO — XTASY 4.0 | Project Exhibition',
        'desc': 'Showcase breakthrough engineering projects, hardware prototypes, and futuristic tech innovations to industry judges.'
    }
}

image_url = 'https://xtasy-4-0.vercel.app/assets/xtasy_logo.jpg'

for fn, info in files_info.items():
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta tags block
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

    # Remove existing OG & Twitter tags
    content = re.sub(r'<!--\s*(?:Favicon|Open Graph|Twitter)[^>]*-->', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\s*<link rel="(?:icon|apple-touch-icon)"[^>]+>', '', content)
    content = re.sub(r'\s*<meta property="og:[^"]+"[^>]+>', '', content)
    content = re.sub(r'\s*<meta name="twitter:[^"]+"[^>]+>', '', content)

    # Insert meta block right before </head>
    content = content.replace('</head>', f'\n{meta_block}\n</head>')

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fn} with new OG image: {image_url}")

print("All files updated successfully.")
