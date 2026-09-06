import glob
import re
import os

html_files = sorted(glob.glob('*.html'))
print('Found HTML files:', html_files)

all_issues = {}

for hf in html_files:
    issues = []
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Check local assets (src and url())
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    css_urls = re.findall(r'url\(["\']?([^"\'\)\s]+)["\']?\)', content)
    for s in set(srcs + css_urls):
        if not s.startswith('http') and not s.startswith('data:') and not s.startswith('#') and not s.startswith('%23'):
            clean_s = s.split('?')[0].split('#')[0]
            if not os.path.exists(clean_s):
                issues.append(f'MISSING ASSET: {clean_s}')

    # 2. Check IDs referenced in goTo
    gotos = re.findall(r'goTo\(["\']([^"\']+)["\']\)', content)
    for target in set(gotos):
        if f'id="{target}"' not in content:
            issues.append(f'BROKEN goTo: target id="{target}" not present in {hf}')

    # 3. Header elements
    if 'id="sound-btn"' not in content:
        issues.append('MISSING desktop sound toggle: id="sound-btn"')
    if 'id="sound-btn-mobile"' not in content:
        issues.append('MISSING mobile sound toggle: id="sound-btn-mobile"')
    if 'id="mobileNav"' not in content:
        issues.append('MISSING mobile nav overlay: id="mobileNav"')
    if 'id="contact-modal"' not in content:
        issues.append('MISSING contact modal: id="contact-modal"')
    if 'class="hdr-right"' not in content:
        issues.append('MISSING class="hdr-right" wrapper in header')
    
    # 4. Check duplicate IDs
    all_ids = re.findall(r'id=["\']([^"\']+)["\']', content)
    id_counts = {}
    for i in all_ids:
        id_counts[i] = id_counts.get(i, 0) + 1
    for i, count in id_counts.items():
        # filter out svg gradient/filter IDs if any
        if count > 1:
            issues.append(f'DUPLICATE ID: id="{i}" appears {count} times')

    # 5. Check mobile menu CSS vs JS
    css_has_open = '.mobile-nav-overlay.open' in content and '.mobile-menu-btn.open' in content
    css_has_active = '.mobile-nav-overlay.active' in content and '.mobile-menu-btn.active' in content
    if not (css_has_open or css_has_active):
        issues.append('MOBILE MENU CSS: Missing both .open and .active rules')
    
    all_issues[hf] = issues

total_issues = 0
for hf, issues in all_issues.items():
    print(f"\n==================== {hf} ====================")
    if not issues:
        print("  [PASS] ALL CHECKS PASSED (No issues found)")
    else:
        for iss in issues:
            print(f"  [FAIL] {iss}")
            total_issues += 1

print(f"\nTOTAL ISSUES DETECTED: {total_issues}")
