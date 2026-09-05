import os
import take_snap

test_html = """<!DOCTYPE html>
<html>
<body style="margin:0;background:#000">
  <iframe id="ifr" src="../index.html" style="width:1440px;height:900px;border:none;"></iframe>
  <script>
    var ifr = document.getElementById('ifr');
    ifr.onload = function() {
      setTimeout(function() {
        var doc = ifr.contentDocument || ifr.contentWindow.document;
        var el = doc.getElementById('welcome');
        if (el) el.scrollIntoView();
      }, 400);
    };
  </script>
</body>
</html>"""

os.makedirs('scratch_frames', exist_ok=True)
with open('scratch_frames/test_scroll_runner.html', 'w') as f:
    f.write(test_html)

take_snap.take_snapshot('scratch_frames/test_scroll_runner.html', 'scratch_frames/welcome_scrolled.png', delay_s=2.5, width=1440, height=900)
print('Welcome scrolled snapshot taken')
