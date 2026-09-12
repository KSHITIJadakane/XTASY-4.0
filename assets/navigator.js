/**
 * XTASY 4.0 — Seamless Unbroken Audio & SPA Page Navigator
 * Keeps audio playing continuously across Home -> Events -> Event Pages -> Registration
 */
(function() {
  'use strict';

  // 1. Audio Memory & Continuity
  var snd = document.getElementById('snd');
  if (snd) {
    try {
      // Clear any accidental mute flag from previous sessions so audio always autoplays
      sessionStorage.removeItem('xtasy_audio_muted');
      window.userMuted = false;

      var savedTime = sessionStorage.getItem('xtasy_audio_time');
      if (savedTime && !isNaN(savedTime)) {
        var t = parseFloat(savedTime);
        if (t > 0 && (!snd.duration || t < snd.duration)) {
          snd.currentTime = t;
        }
      }
    } catch(e) {}

    // Continuously persist current playback timestamp
    snd.addEventListener('timeupdate', function() {
      try {
        if (!snd.paused && snd.currentTime > 0) {
          sessionStorage.setItem('xtasy_audio_time', snd.currentTime);
        }
      } catch(e) {}
    });

    // Auto-trigger audio playback immediately on load
    snd.volume = 0.5;
    var playPromise = snd.play();
    if (playPromise !== undefined) {
      playPromise.then(function() {
        if (typeof window.updateSoundUI === 'function') {
          window.updateSoundUI(true);
        }
      }).catch(function(e) {
        // If mobile browser blocks unprompted autoplay, start on very first interaction
        var touchEvents = ['pointerdown', 'touchstart', 'mousedown', 'click', 'scroll', 'keydown'];
        function onFirstTouch() {
          if (snd.paused && !window.userMuted) {
            snd.volume = 0.5;
            snd.play().then(function() {
              if (typeof window.updateSoundUI === 'function') {
                window.updateSoundUI(true);
              }
            }).catch(function() {});
          }
          touchEvents.forEach(function(evt) {
            window.removeEventListener(evt, onFirstTouch, true);
            document.removeEventListener(evt, onFirstTouch, true);
          });
        }
        touchEvents.forEach(function(evt) {
          window.addEventListener(evt, onFirstTouch, { capture: true, passive: true });
          document.addEventListener(evt, onFirstTouch, { capture: true, passive: true });
        });
      });
    }
  }

  // 2. Internal Page Detection
  var internalPages = [
    'index.html',
    'events.html',
    'automystica.html',
    'hackthehardware.html',
    'triguna.html',
    'visionexpo.html'
  ];

  function getCleanFileName(url) {
    if (!url) return '';
    var clean = url.split('?')[0].split('#')[0];
    var file = clean.split('/').pop();
    if (!file || file === '') return 'index.html';
    return file;
  }

  function isInternalUrl(url) {
    if (!url) return false;
    if (url.startsWith('mailto:') || url.startsWith('tel:') || url.startsWith('javascript:')) return false;
    if (url.indexOf('forms.gle') !== -1 || url.indexOf('docs.google.com') !== -1 || url.indexOf('instagram.com') !== -1) return false;
    var file = getCleanFileName(url);
    return internalPages.indexOf(file) !== -1;
  }

  var isNavigating = false;
  var cachedPages = {};

  // 3. Seamless Transition Function
  window.xtasyNavigate = function(url, pushState) {
    if (pushState === undefined) pushState = true;
    if (isNavigating) return;

    if (!isInternalUrl(url)) {
      window.location.href = url;
      return;
    }

    var targetFile = getCleanFileName(url);
    var currentFile = getCleanFileName(window.location.pathname);

    // If target is events.html (event concluded), reroute directly to index.html#thankyou
    if (targetFile === 'events.html') {
      window.xtasyNavigate('index.html#thankyou', pushState);
      return;
    }

    // If navigating to the same file with a hash, smooth scroll to element
    if (targetFile === currentFile && url.indexOf('#') !== -1) {
      var hash = url.split('#')[1];
      var el = document.getElementById(hash);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
        if (pushState) history.pushState({ url: url }, document.title, url);
        return;
      }
    }

    isNavigating = true;

    // Fade out main content
    var main = document.querySelector('main');
    if (main) {
      main.style.transition = 'opacity 0.15s cubic-bezier(0.16, 1, 0.3, 1), transform 0.15s cubic-bezier(0.16, 1, 0.3, 1)';
      main.style.opacity = '0';
      main.style.transform = 'translateY(8px)';
    }

    function applyNewPage(html, destinationUrl) {
      try {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        // 1. Update Title
        if (doc.title) {
          document.title = doc.title;
        }

        // 2. Update Page-Specific CSS
        var newStyles = Array.from(doc.querySelectorAll('style')).map(function(s) { return s.textContent; }).join('\n');
        var dynamicStyleEl = document.getElementById('xtasy-dynamic-styles');
        if (!dynamicStyleEl) {
          dynamicStyleEl = document.createElement('style');
          dynamicStyleEl.id = 'xtasy-dynamic-styles';
          document.head.appendChild(dynamicStyleEl);
        }
        dynamicStyleEl.textContent = newStyles;

        // 3. Update Header (keeps nav links in correct active state)
        var newHdr = doc.getElementById('hdr');
        var curHdr = document.getElementById('hdr');
        if (newHdr && curHdr) {
          curHdr.innerHTML = newHdr.innerHTML;
        }

        // 4. Update Mobile Nav Overlay
        var newMobileNav = doc.getElementById('mobileNav');
        var curMobileNav = document.getElementById('mobileNav');
        if (newMobileNav && curMobileNav) {
          curMobileNav.innerHTML = newMobileNav.innerHTML;
        }

        // 5. Update Main Content
        var newMain = doc.querySelector('main');
        if (main && newMain) {
          main.innerHTML = newMain.innerHTML;
          main.className = newMain.className;
        }

        // 6. Update Event Registration Modal if present
        var newRegModal = doc.getElementById('reg-modal');
        var curRegModal = document.getElementById('reg-modal');
        if (newRegModal) {
          if (curRegModal) {
            curRegModal.outerHTML = newRegModal.outerHTML;
          } else {
            document.body.insertAdjacentHTML('beforeend', newRegModal.outerHTML);
          }
        } else if (curRegModal) {
          curRegModal.remove();
        }

        // 7. Update Contact Modal
        var newContactModal = doc.getElementById('contact-modal');
        var curContactModal = document.getElementById('contact-modal');
        if (newContactModal && curContactModal) {
          curContactModal.innerHTML = newContactModal.innerHTML;
        }

        // 8. Update Body classes & Loader state
        var destFile = getCleanFileName(destinationUrl);
        if (destFile === 'index.html') {
          // If returning to index, make sure hero is settled and loader is dismissed
          document.body.classList.remove('loader-active');
          document.body.classList.add('intro-active', 'lit', 'settled');
          var loader = document.getElementById('xtasy-loader');
          if (loader) loader.style.display = 'none';
        } else {
          document.body.classList.remove('loader-active');
          document.body.classList.add('settled');
        }

        // 9. Update History
        if (pushState) {
          window.history.pushState({ url: destinationUrl }, doc.title, destinationUrl);
        }

        // 10. Scroll position
        if (destinationUrl.indexOf('#') !== -1) {
          var targetId = destinationUrl.split('#')[1];
          var targetNode = document.getElementById(targetId);
          if (targetNode) targetNode.scrollIntoView({ behavior: 'smooth' });
          else window.scrollTo(0, 0);
        } else {
          window.scrollTo(0, 0);
        }

        // 11. Re-initialize interactive components
        reinitializePage(destFile);

        // 12. Fade main content back in
        if (main) {
          setTimeout(function() {
            main.style.opacity = '1';
            main.style.transform = 'translateY(0)';
          }, 30);
        }
      } catch(err) {
        console.error('Error applying page content:', err);
        window.location.href = destinationUrl;
      } finally {
        isNavigating = false;
      }
    }

    // Check cache first for instant feel
    if (cachedPages[targetFile]) {
      applyNewPage(cachedPages[targetFile], url);
      return;
    }

    fetch(url)
      .then(function(res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.text();
      })
      .then(function(html) {
        cachedPages[targetFile] = html;
        applyNewPage(html, url);
      })
      .catch(function(err) {
        console.warn('Navigation fetch failed, falling back to full page load:', err);
        window.location.href = url;
        isNavigating = false;
      });
  };

  // 4. Component Re-initialization after page swap
  function reinitializePage(pageFile) {
    // Synchronize audio UI button state
    var currentSnd = document.getElementById('snd');
    if (currentSnd && typeof window.updateSoundUI === 'function') {
      window.updateSoundUI(!currentSnd.paused);
    }

    // Attach cursor shapes on new links and buttons
    if (typeof window.attachCursorEvents === 'function') {
      window.attachCursorEvents();
    }

    // Scroll reveal observer on .sec
    var secs = document.querySelectorAll('.sec');
    if (secs.length && 'IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function(entries) {
        entries.forEach(function(en) {
          if (!en.isIntersecting) return;
          en.target.classList.add('iv');
        });
      }, { threshold: 0.18, rootMargin: '0px 0px -10% 0px' });
      secs.forEach(function(s) { obs.observe(s); });
    }

    // Close any open mobile navigation
    var mobileNav = document.getElementById('mobileNav');
    if (mobileNav) {
      mobileNav.classList.remove('active', 'open');
    }
    var menuBtn = document.querySelector('.mobile-menu-btn');
    if (menuBtn) {
      menuBtn.classList.remove('active', 'open');
    }
  }

  // 5. Global Link & Button Click Interception (Capture Phase)
  document.addEventListener('click', function(e) {
    // 1. Check anchor elements
    var a = e.target.closest('a');
    if (a) {
      var href = a.getAttribute('href');
      if (href && isInternalUrl(href) && a.target !== '_blank' && !e.metaKey && !e.ctrlKey) {
        e.preventDefault();
        e.stopPropagation();
        window.xtasyNavigate(href);
        return;
      }
    }

    // 2. Check elements with inline window.location.href
    var clickEl = e.target.closest('[onclick]');
    if (clickEl) {
      var onclickAttr = clickEl.getAttribute('onclick');
      if (onclickAttr && onclickAttr.indexOf('window.location.href') !== -1) {
        var match = onclickAttr.match(/window\.location\.href\s*=\s*['"]([^'"]+)['"]/);
        if (match && match[1] && isInternalUrl(match[1])) {
          e.preventDefault();
          e.stopPropagation();
          window.xtasyNavigate(match[1]);
          return;
        }
      }
    }
  }, true);

  // 6. Browser Back & Forward History Listener
  window.addEventListener('popstate', function(e) {
    var targetUrl = window.location.pathname.split('/').pop() || 'index.html';
    if (window.location.hash) {
      targetUrl += window.location.hash;
    }
    window.xtasyNavigate(targetUrl, false);
  });

  // 7. Make modal and audio handlers globally accessible across all views
  window.openContactModal = window.openContactModal || function() {
    var m = document.getElementById('contact-modal');
    if (m) m.classList.add('open');
  };

  window.closeContactModal = window.closeContactModal || function() {
    var m = document.getElementById('contact-modal');
    if (m) m.classList.remove('open');
  };

  window.toggleToolbar = window.toggleToolbar || function(e) {
    if (e) e.stopPropagation();
    var tb = document.getElementById('xtasy-toolbar');
    if (tb) tb.classList.toggle('active');
  };

  // Close toolbar when clicking outside
  document.addEventListener('click', function(e) {
    var tb = document.getElementById('xtasy-toolbar');
    if (tb && tb.classList.contains('active') && !e.target.closest('#xtasy-toolbar') && !e.target.closest('.logo')) {
      tb.classList.remove('active');
    }
  });

})();
