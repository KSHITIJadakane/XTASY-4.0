import os
import re

filepath = r"c:\Users\rajur\OneDrive\Desktop\xtasy\make_pages.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole injected block in make_pages.py

old_block = '''      <script>
      document.addEventListener('DOMContentLoaded', () => {
        // Quick Access Toolbar Setup
        const toolbar = document.createElement('div');
        toolbar.id = 'xtasy-toolbar';
        toolbar.innerHTML = 
          <div class="xt-item" onclick="window.history.back()">
            <span class="xt-icon">←</span> Back
          </div>
          <div class="xt-item" onclick="window.location.href='index.html'">
            <span class="xt-icon">⌂</span> Home
          </div>
          <div class="xt-item" style="opacity: 0.5; cursor: not-allowed;">
            <span class="xt-icon">⊞</span> Dashboard (Soon)
          </div>
        ;
        document.body.appendChild(toolbar);

        const logo = document.querySelector('.logo');
        if (logo) {
          // Remove potential existing onclick attribute behaviors
          logo.removeAttribute('onclick');
          logo.style.cursor = 'pointer';
          
          logo.addEventListener('click', (e) => {
            e.stopPropagation();
            toolbar.classList.toggle('active');
          });
        }

        // Close toolbar when clicking outside
        document.addEventListener('click', (e) => {
          if (!toolbar.contains(e.target) && (!logo || !logo.contains(e.target))) {
            toolbar.classList.remove('active');
          }
        });
      });
    </script>'''

new_block = '''      <script>
      (function() {
        // Quick Access Toolbar Setup
        const toolbar = document.createElement('div');
        toolbar.id = 'xtasy-toolbar';
        toolbar.innerHTML = 
          <div class="xt-item" onclick="window.history.back()">
            <span class="xt-icon">←</span> Back
          </div>
          <div class="xt-item" onclick="window.location.href='index.html'">
            <span class="xt-icon">⌂</span> Home
          </div>
          <div class="xt-item" style="opacity: 0.5; cursor: not-allowed;">
            <span class="xt-icon">⊞</span> Dashboard (Soon)
          </div>
        ;
        document.body.appendChild(toolbar);

        const logo = document.querySelector('.logo');
        if (logo) {
          logo.style.cursor = 'pointer';
          // We will use inline onclick to call toggleToolbar so we don't depend on load timing
          logo.setAttribute('onclick', 'toggleToolbar(event)');
        }

        // Close toolbar when clicking outside
        document.addEventListener('click', (e) => {
          if (toolbar && !toolbar.contains(e.target) && (!logo || !logo.contains(e.target))) {
            toolbar.classList.remove('active');
          }
        });
      })();

      function toggleToolbar(e) {
        if(e) e.stopPropagation();
        const toolbar = document.getElementById('xtasy-toolbar');
        if(toolbar) toolbar.classList.toggle('active');
      }
      </script>'''

content = content.replace(old_block, new_block)

# Remove the extra <script> block for toggleToolbar since we integrated it above
extra_toggle = '''
    <script>
      function toggleToolbar(e) {
        if(e) e.stopPropagation();
        const toolbar = document.getElementById('xtasy-toolbar');
        if(toolbar) toolbar.classList.toggle('active');
      }
    </script>'''
content = content.replace(extra_toggle, "")

# We don't need to rewrite the regex for <div class="logo"... in python because we dynamically do logo.setAttribute in JS
# But let's remove any hardcoded toggleToolbar if we did it via regex earlier. 
# Wait, make_pages.py reads from events.html or similar, which might still have <div class="logo" onclick="goTo('hero')">

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

