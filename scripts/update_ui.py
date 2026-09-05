import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update fx-scroll and countdown UI in HTML
fx_vig = '<div class="fx-vig"></div>'
fx_vig_new = '''<div class="fx-vig"></div>
  <div class="fx-scroll" id="fx-scroll"></div>'''
html = html.replace(fx_vig, fx_vig_new)

scroll_cue = '''          <div class="scroll-cue" onclick="goTo('welcome')">
            <span class="sc-lbl">SCROLL</span>
            <div class="sc-mouse"><div class="sc-dot"></div></div>
          </div>
        </div>'''
scroll_cue_new = scroll_cue + '''
        
        <div id="countdown"><span class="cd-lbl">T-MINUS</span><span class="cd-clock">04:59:59</span></div>'''
html = html.replace(scroll_cue, scroll_cue_new)

# 2. Update Rules Grid symbols and data-cursors
rules_grid = '''        <div class="rules-grid">
          <div class="rc"><div class="r-num">1</div><div class="r-title">6 games.</div><div class="r-desc">Each harder. Each deadlier.</div></div>
          <div class="rc"><div class="r-num">2</div><div class="r-title">No second chances</div><div class="r-desc">One move. One shot.</div></div>
          <div class="rc"><div class="r-num">3</div><div class="r-title">Trust no one</div><div class="r-desc">Allies can betray you</div></div>
          <div class="rc"><div class="r-num">4</div><div class="r-title">Time is running.</div><div class="r-desc">Decide fast — or die.</div></div>
        </div>'''
rules_grid_new = '''        <div class="rules-grid">
          <div class="rc" data-cursor="square"><div class="r-num">○</div><div class="r-title">6 games.</div><div class="r-desc">Each harder. Each deadlier.</div></div>
          <div class="rc" data-cursor="square"><div class="r-num">△</div><div class="r-title">No second chances</div><div class="r-desc">One move. One shot.</div></div>
          <div class="rc" data-cursor="square"><div class="r-num">□</div><div class="r-title">Trust no one</div><div class="r-desc">Allies can betray you</div></div>
          <div class="rc" data-cursor="square"><div class="r-num">○</div><div class="r-title">Time is running.</div><div class="r-desc">Decide fast — or die.</div></div>
        </div>'''
html = html.replace(rules_grid, rules_grid_new)

# 3. Update Modal HTML
modal = '''  <div id="modal" onclick="if(event.target===this)closeModal()">
    <div class="mbox">
      <div class="m-syms">&#9675; &#9651; &#9633;</div>
      <h3 class="m-h">YOU ARE INVITED</h3>
      <p class="m-p">Will you risk everything for the prize?<br/>Player 456 is waiting.</p>
      <div class="m-ins">
        <input type="text" class="m-inp" placeholder="ENTER PLAYER NAME"/>
        <input type="email" class="m-inp" placeholder="CONTACT FREQUENCY (EMAIL)"/>
      </div>
      <button class="btn-conf" onclick="confirmEntry()">CONFIRM REGISTRATION</button><br/>
      <button class="btn-walk" onclick="closeModal()">WALK AWAY</button>
    </div>
  </div>'''
modal_new = '''  <div id="modal" onclick="if(event.target===this)closeModal()">
    <div class="mbox" data-cursor="default">
      <div class="m-top">
        <div class="m-syms">&#9675; &#9651; &#9633;</div>
        <div class="m-h">CONSENT FORM</div>
      </div>
      <p class="m-p">I acknowledge that the games are highly dangerous.<br/>I play of my own free will. No quitting.</p>
      <div class="m-ins">
        <input type="text" class="m-inp" placeholder="ENTER PLAYER ALIAS"/>
        <input type="email" class="m-inp" placeholder="CONTACT EMAIL"/>
      </div>
      <div class="m-actions">
        <button class="btn-walk" data-cursor="triangle" onclick="closeModal()">WALK AWAY</button>
        <button class="btn-conf" data-cursor="triangle" onclick="confirmEntry()">
          <div class="thumbprint"></div>
          <span class="btn-conf-lbl">AGREE</span>
        </button>
      </div>
    </div>
  </div>'''
html = html.replace(modal, modal_new)

# Add data-cursor="triangle" to buttons/links
html = html.replace('class="btn-cta"', 'class="btn-cta" data-cursor="triangle"')
html = html.replace('class="btn-accept"', 'class="btn-accept" data-cursor="triangle"')
html = html.replace('class="btn-replay"', 'class="btn-replay" data-cursor="triangle"')

# Update CSS for Cursor
css_cursor_old = '''    /* Cursor */
    .cdot{position:fixed;top:0;left:0;width:8px;height:8px;background:var(--pink);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);box-shadow:0 0 12px var(--pink),0 0 24px var(--pink);opacity:0;transition:width .2s,height .2s,background .2s,opacity .3s}
    .cring{position:fixed;top:0;left:0;width:32px;height:32px;border:1.5px solid rgba(255,0,127,.6);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);opacity:0;transition:width .3s var(--ease-s),height .3s var(--ease-s),border-color .3s,opacity .3s}
    body.m-on .cdot,body.m-on .cring{opacity:1}
    .cdot.hov{width:14px;height:14px;background:var(--cyan);box-shadow:0 0 18px var(--cyan)}
    .cring.hov{width:48px;height:48px;border-color:var(--cyan)}'''

css_cursor_new = '''    /* Cursor */
    .cdot{position:fixed;top:0;left:0;width:8px;height:8px;background:var(--pink);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);box-shadow:0 0 12px var(--pink),0 0 24px var(--pink);opacity:0;transition:width .2s,height .2s,background .2s,opacity .3s,border-radius .2s,border .2s,transform .2s,filter .2s}
    .cring{position:fixed;top:0;left:0;width:32px;height:32px;border:1.5px solid rgba(255,0,127,.6);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);opacity:0;transition:width .3s var(--ease-s),height .3s var(--ease-s),border-color .3s,opacity .3s,background .3s,border-radius .3s,border .3s,clip-path .3s}
    body.m-on .cdot,body.m-on .cring{opacity:1}
    /* Circle */
    .cdot.hov{width:14px;height:14px;background:var(--cyan);box-shadow:0 0 18px var(--cyan)}
    .cring.hov{width:48px;height:48px;border-color:var(--cyan)}
    /* Triangle (Danger/Action) */
    .cdot.hov-triangle{width:0;height:0;background:transparent;border-left:7px solid transparent;border-right:7px solid transparent;border-bottom:12px solid var(--pink);border-radius:0;box-shadow:none;filter:drop-shadow(0 0 8px var(--pink));transform:translate(-50%,calc(-50% - 2px))}
    .cring.hov-triangle{width:46px;height:46px;border-radius:0;clip-path:polygon(50% 0%, 0% 100%, 100% 100%);background:rgba(255,0,127,.12);border:none}
    /* Square (Info) */
    .cdot.hov-square{width:12px;height:12px;border-radius:2px;background:var(--cyan);box-shadow:0 0 12px var(--cyan)}
    .cring.hov-square{width:42px;height:42px;border-radius:4px;border-color:var(--cyan)}'''
html = html.replace(css_cursor_old, css_cursor_new)

# Update Atmosphere CSS
css_atmos_old = '''    /* Atmosphere */
    .fx-grain{position:fixed;inset:0;pointer-events:none;z-index:900;opacity:.032;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
    .fx-vig{position:fixed;inset:0;pointer-events:none;z-index:12;background:radial-gradient(ellipse at center,transparent 58%,rgba(0,0,0,.75) 100%)}'''

css_atmos_new = '''    /* Atmosphere */
    .fx-grain{position:fixed;inset:0;pointer-events:none;z-index:900;opacity:.032;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
    .fx-vig{position:fixed;inset:0;pointer-events:none;z-index:12;background:radial-gradient(ellipse at center,transparent 58%,rgba(0,0,0,.75) 100%)}
    .fx-scroll{position:fixed;inset:0;pointer-events:none;z-index:11;background:radial-gradient(ellipse at center,transparent 58%,rgba(3,122,75,0.04) 100%);transition:background 0.5s}
    .fx-scroll.danger{background:radial-gradient(ellipse at center,transparent 50%,rgba(186,19,77,0.2) 100%)}
    body.glitch main{animation:glitch-scroll 0.3s cubic-bezier(.25,.46,.45,.94) both 2}
    @keyframes glitch-scroll{0%{transform:translate(0)}20%{transform:translate(-3px,1px)}40%{transform:translate(-1px,-3px)}60%{transform:translate(3px,1px)}80%{transform:translate(1px,-1px)}100%{transform:translate(0)}}'''
html = html.replace(css_atmos_old, css_atmos_new)

# Add Countdown Timer CSS below Atmosphere
countdown_css = '''
    /* Countdown Timer */
    #countdown{position:fixed;bottom:26px;left:26px;z-index:100;font-family:'Space Mono',monospace;font-size:16px;font-weight:700;color:var(--pink);text-shadow:0 0 12px rgba(255,0,127,.6);letter-spacing:.15em;display:flex;align-items:center;gap:12px;opacity:0;transform:translateY(10px);transition:all .8s var(--ease) 1.5s}
    body.settled #countdown{opacity:1;transform:translateY(0)}
    .cd-lbl{font-size:9px;color:var(--t70);letter-spacing:.25em}
    .cd-clock{background:rgba(8,8,8,.72);border:1px solid rgba(255,0,127,.2);padding:6px 12px;border-radius:4px;backdrop-filter:blur(12px)}'''
html = html.replace('/* Cursor */', countdown_css + '\n\n    /* Cursor */')

# Update Modal CSS
css_modal_old = '''    /* Modal */
    #modal{position:fixed;inset:0;background:rgba(0,0,0,.9);backdrop-filter:blur(18px);z-index:1000;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s var(--ease-s)}
    #modal.open{opacity:1;pointer-events:auto}
    .mbox{width:min(92vw,440px);background:#0c0c0c;border:1px solid var(--pink);box-shadow:0 0 52px rgba(255,0,127,.48);border-radius:12px;padding:36px 28px;text-align:center;transform:scale(.88);transition:transform .4s var(--ease)}
    #modal.open .mbox{transform:scale(1)}
    .m-syms{font-size:30px;margin-bottom:12px;color:var(--pink);text-shadow:0 0 22px rgba(255,0,127,.75)}
    .m-h{font-family:'Space Grotesk',sans-serif;font-size:22px;font-weight:800;color:#fff;letter-spacing:.1em;margin-bottom:8px}
    .m-p{font-family:'Inter',sans-serif;font-size:13.5px;color:var(--t70);margin-bottom:24px;line-height:1.52}
    .m-ins{display:flex;flex-direction:column;gap:12px;margin-bottom:20px}
    .m-inp{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.2);border-radius:6px;padding:12px 16px;color:#fff;font-family:'Space Grotesk',sans-serif;font-size:12.5px;text-transform:uppercase;outline:none;width:100%;transition:border-color .25s,box-shadow .25s}
    .m-inp:focus{border-color:var(--pink);box-shadow:0 0 0 1px var(--pink),0 0 16px rgba(255,0,127,.32)}
    .btn-conf{width:100%;padding:12px;font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:700;letter-spacing:.05em;color:#fff;background:var(--pink);border:none;border-radius:9999px;cursor:pointer;box-shadow:0 0 22px rgba(255,0,127,.52);transition:all .3s}
    .btn-conf:hover{background:#ff1a8c;box-shadow:0 0 40px rgba(255,0,127,.9)}
    .btn-walk{background:none;border:none;color:rgba(255,255,255,.38);font-size:11.5px;margin-top:12px;cursor:pointer;text-decoration:underline;transition:color .25s}
    .btn-walk:hover{color:rgba(255,255,255,.68)}'''

css_modal_new = '''    /* Modal - Consent Form */
    #modal{position:fixed;inset:0;background:rgba(0,0,0,.85);backdrop-filter:blur(12px);z-index:1000;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s var(--ease-s)}
    #modal.open{opacity:1;pointer-events:auto}
    .mbox{width:min(92vw,440px);background:#f4f4f0;box-shadow:0 24px 64px rgba(0,0,0,.8);border-radius:2px;padding:48px 36px;text-align:left;transform:scale(.94) translateY(20px);transition:transform .5s var(--ease);position:relative;overflow:hidden}
    .mbox::before{content:'';position:absolute;inset:0;background:url('data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="100" height="100"%3E%3Cfilter id="noise"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noise)" opacity="0.08"/%3E%3C/svg%3E');pointer-events:none;mix-blend-mode:multiply}
    #modal.open .mbox{transform:scale(1) translateY(0)}
    .m-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px;border-bottom:2px solid #222;padding-bottom:16px}
    .m-syms{font-family:'Space Grotesk',sans-serif;font-size:18px;color:#000;letter-spacing:.2em;font-weight:700}
    .m-h{font-family:'Space Mono',monospace;font-size:16px;font-weight:700;color:#000;letter-spacing:.05em;text-transform:uppercase}
    .m-p{font-family:'Space Mono',monospace;font-size:12.5px;color:#333;margin-bottom:28px;line-height:1.6}
    .m-ins{display:flex;flex-direction:column;gap:16px;margin-bottom:32px}
    .m-inp{background:transparent;border:none;border-bottom:1px dashed #666;padding:8px 0;color:#000;font-family:'Space Mono',monospace;font-size:14px;outline:none;width:100%;transition:border-color .25s}
    .m-inp:focus{border-color:#ba134d}
    .m-inp::placeholder{color:#999}
    
    .m-actions{display:flex;align-items:center;justify-content:space-between;margin-top:20px;position:relative;z-index:2}
    .btn-conf{position:relative;width:90px;height:100px;background:none;border:1px dashed #ccc;border-radius:4px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:all .3s;overflow:hidden;margin-left:auto}
    .btn-conf-lbl{font-family:'Space Mono',monospace;font-size:10px;color:#666;margin-top:auto;margin-bottom:8px}
    .thumbprint{position:absolute;top:10px;left:18px;width:55px;height:70px;opacity:0;transform:scale(1.2);transition:all .3s cubic-bezier(.35,0,.25,1);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 120' fill='none' stroke='%23ba134d' stroke-width='4' stroke-linecap='round'%3E%3Cpath d='M40,20 Q50,15 60,20'/%3E%3Cpath d='M35,30 Q50,20 65,30'/%3E%3Cpath d='M30,40 Q50,25 70,40'/%3E%3Cpath d='M25,50 Q50,30 75,50'/%3E%3Cpath d='M28,60 Q50,35 72,60'/%3E%3Cpath d='M32,70 Q50,45 68,70'/%3E%3Cpath d='M38,80 Q50,55 62,80'/%3E%3Cpath d='M45,90 Q50,70 55,90'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:center;mix-blend-mode:multiply}
    .btn-conf:hover{border-color:#ba134d;background:rgba(186,19,77,.04)}
    .btn-conf:hover .thumbprint{opacity:0.85;transform:scale(1)}
    
    .btn-walk{background:none;border:none;color:#555;font-family:'Space Mono',monospace;font-size:13px;cursor:pointer;text-decoration:underline;text-underline-offset:4px;transition:color .25s}
    .btn-walk:hover{color:#ba134d}'''
html = html.replace(css_modal_old, css_modal_new)


# Update JS
js_cursor_old = '''    /* ── 3. CURSOR + 3D CARD TILT ── */
    window.addEventListener('mousemove',function(e){
      document.body.classList.add('m-on');mx=e.clientX;my=e.clientY;
      dot.style.left=mx+'px';dot.style.top=my+'px';
      var cs=document.getElementById('cstage'),tc=document.getElementById('tcard');
      if(cs&&tc){var r=cs.getBoundingClientRect();
        if(my>=r.top&&my<=r.bottom&&mx>=r.left&&mx<=r.right){
          var px=(mx-r.left)/r.width-.5,py=(my-r.top)/r.height-.5;
          tc.style.transform='rotateY('+(px*36)+'deg) rotateX('+(-py*36)+'deg) translateY(-18px) scale(1.05)'
        }
      }
    });
    (function loop(){rx+=(mx-rx)*.15;ry+=(my-ry)*.15;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(loop)})();
    document.querySelectorAll('a,button,.card-m,.ci').forEach(function(el){
      el.addEventListener('mouseenter',function(){dot.classList.add('hov');ring.classList.add('hov')});
      el.addEventListener('mouseleave',function(){dot.classList.remove('hov');ring.classList.remove('hov')});
    });'''

js_cursor_new = '''    /* ── 3. CURSOR + 3D CARD TILT ── */
    window.addEventListener('mousemove',function(e){
      document.body.classList.add('m-on');mx=e.clientX;my=e.clientY;
      dot.style.left=mx+'px';dot.style.top=my+'px';
      var cs=document.getElementById('cstage'),tc=document.getElementById('tcard');
      if(cs&&tc){var r=cs.getBoundingClientRect();
        if(my>=r.top&&my<=r.bottom&&mx>=r.left&&mx<=r.right){
          var px=(mx-r.left)/r.width-.5,py=(my-r.top)/r.height-.5;
          tc.style.transform='rotateY('+(px*36)+'deg) rotateX('+(-py*36)+'deg) translateY(-18px) scale(1.05)'
        }
      }
    });
    (function loop(){rx+=(mx-rx)*.15;ry+=(my-ry)*.15;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(loop)})();
    
    function attachCursorEvents(){
      document.querySelectorAll('a,button,.card-m,.ci,.rc').forEach(function(el){
        el.addEventListener('mouseenter',function(){
          var shape = el.getAttribute('data-cursor') || 'circle';
          if(shape==='triangle'){dot.classList.add('hov-triangle');ring.classList.add('hov-triangle');}
          else if(shape==='square'){dot.classList.add('hov-square');ring.classList.add('hov-square');}
          else{dot.classList.add('hov');ring.classList.add('hov');}
        });
        el.addEventListener('mouseleave',function(){
          dot.classList.remove('hov','hov-triangle','hov-square');
          ring.classList.remove('hov','hov-triangle','hov-square');
        });
      });
    }
    attachCursorEvents();

    /* Red Light Green Light Scroll */
    var lastScrollY = window.scrollY, scrollTimeout;
    window.addEventListener('scroll', function() {
      var currentScrollY = window.scrollY;
      var velocity = Math.abs(currentScrollY - lastScrollY);
      var fx = document.getElementById('fx-scroll');
      lastScrollY = currentScrollY;
      
      if(velocity > 35 && document.body.classList.contains('settled')) {
        fx.classList.add('danger');
        document.body.classList.add('glitch');
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function(){
          fx.classList.remove('danger');
          document.body.classList.remove('glitch');
        }, 300);
      }
    });

    /* Countdown Timer logic */
    var cdClock = document.querySelector('.cd-clock');
    var timeLeft = 4 * 3600 + 59 * 60 + 59; // 04:59:59
    setInterval(function(){
      timeLeft--;
      if(timeLeft<0) timeLeft=0;
      var h = Math.floor(timeLeft / 3600);
      var m = Math.floor((timeLeft % 3600) / 60);
      var s = timeLeft % 60;
      if(cdClock) cdClock.innerText = (h<10?'0'+h:h)+':'+(m<10?'0'+m:m)+':'+(s<10?'0'+s:s);
    }, 1000);'''
html = html.replace(js_cursor_old, js_cursor_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
