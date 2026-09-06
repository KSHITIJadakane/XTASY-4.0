import re
import os

files = ['index.html', 'events.html', 'automystica.html', 'hackthehardware.html', 'triguna.html', 'visionexpo.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    content = open(fn, 'r', encoding='utf-8').read()
    style_blocks = re.findall(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    print(f"=== {fn} ({len(style_blocks)} style blocks) ===")
    for idx, block in enumerate(style_blocks):
        # strip strings and comments
        cleaned = re.sub(r'/\*.*?\*/', '', block, flags=re.DOTALL)
        cleaned = re.sub(r'"(?:\\.|[^"\\])*"', '', cleaned)
        cleaned = re.sub(r"'(?:\\.|[^'\\])*'", '', cleaned)
        
        balance = 0
        errors = []
        for line_no, line in enumerate(cleaned.split('\n'), 1):
            for ch in line:
                if ch == '{':
                    balance += 1
                elif ch == '}':
                    balance -= 1
                    if balance < 0:
                        errors.append(f"Block {idx+1} Extra '}}' at relative line {line_no}")
                        balance = 0
        if balance > 0:
            errors.append(f"Block {idx+1} Missing {balance} '}}' (unclosed blocks)")
            
        if errors:
            for err in errors:
                print("  [ERROR]", err)
        else:
            print(f"  [OK] Block {idx+1} perfectly balanced.")
