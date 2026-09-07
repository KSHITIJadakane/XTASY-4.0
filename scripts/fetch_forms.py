import urllib.request
import re

urls = {
    'TRIGUNA': 'https://forms.gle/GZoGhr7K9MT3817n7',
    'AUTOMYSTICA': 'https://forms.gle/R9LFzpG6GCGGthmg7',
    'HACK_THE_HARDWARE': 'https://forms.gle/ogJAjE5PofFKNwup7',
    'VISIONEXPO': 'https://forms.gle/Ebnnth5RKrSLTuk57'
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Form action
        action = re.search(r'action="(https://docs\.google\.com/forms/[^"]+/formResponse)"', html)
        if action:
            print(f"{name} Action URL: {action.group(1)}")
            
        # Find all field names (like entry.123456) and their context
        # In Google Forms, the questions are usually stored in a massive JS array at the end of the file.
        # Let's extract FB_PUBLIC_LOAD_DATA_
        data_match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.*?\]);\n', html, re.DOTALL)
        if data_match:
            print(f"{name} Data found.")
            # We will just print the first 200 chars to verify we can parse it
        else:
            print(f"{name} Data NOT found.")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

