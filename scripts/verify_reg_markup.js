const fs = require('fs');

const files = {
  'automystica.html': { 
    title: 'AUTOMYSTICA // REGISTRATION', 
    form: '1FAIpQLSf1jQc9NrUwIkwGFuUulKUlHb3NIkXBmLC0Oqe7co6WqbLDyA', 
    btnText: 'ENTER AUTOMYSTICA' 
  },
  'hackthehardware.html': { 
    title: 'HACK THE HARDWARE // REGISTRATION', 
    form: '1FAIpQLSetSTwoYBZw0WRXJmBzVfwiX3_OCBlArhGx6hU8wAzAA5cizg', 
    btnText: 'ENTER THE ARENA' 
  },
  'triguna.html': { 
    title: 'TRIGUNA // REGISTRATION', 
    form: '1FAIpQLSeacWAr5sfv1_or_a2kdFzgk4-BvvFjW1KuyhlfMGLYJgDFuA', 
    btnText: 'PITCH YOUR IMPACT' 
  },
  'visionexpo.html': { 
    title: 'VISION EXPO // REGISTRATION', 
    form: '1FAIpQLScj41ycwJXNK7PgPASwvW1SVw7FqlmrqMtZR49m8blxksdQ7w', 
    btnText: 'SUBMIT YOUR VISION' 
  }
};

let allOk = true;

Object.entries(files).forEach(([file, expected]) => {
  const content = fs.readFileSync(file, 'utf8');
  const checks = [
    ['Preconnect to docs.google.com present', content.includes('href="https://docs.google.com"')],
    ['Preconnect to forms.gle present', content.includes('href="https://forms.gle"')],
    ['CTA button has direct form link with target="_blank"', content.includes(`href="https://docs.google.com/forms/d/e/${expected.form}/viewform"`) && content.includes('target="_blank"')],
    ['CTA button has correct text', content.includes(`>${expected.btnText}</a>`)],
    ['openRegModal fallback function present', content.includes('function openRegModal')],
    ['closeRegModal function present', content.includes('function closeRegModal')],
    ['.ed-cta has inline-flex and text-decoration:none', content.includes('.ed-cta { display: inline-flex; align-items: center; justify-content: center; text-decoration: none;')]
  ];
  
  console.log(`=== Checking ${file} ===`);
  checks.forEach(([desc, passed]) => {
    console.log(passed ? '  [PASS]' : '  [FAIL]', desc);
    if (!passed) allOk = false;
  });
});

if (allOk) {
  console.log('\nALL 4 EVENT REGISTRATION BUTTONS & PRECONNECTS FULLY VERIFIED FOR FAST OPENING!');
} else {
  console.error('\nVerification failed!');
  process.exit(1);
}
