// Scroll reveal effect with staggered animation
function revealOnScroll() {
    const reveals = document.querySelectorAll(".reveal");

    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 100;

        if (elementTop < windowHeight - elementVisible) {
            setTimeout(() => {
                reveals[i].classList.add("active");
            }, i * 150); // stagger effect
        }
    }
}

window.addEventListener("scroll", revealOnScroll);
document.addEventListener("DOMContentLoaded", revealOnScroll);

// Change navbar style on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = '#f1f1f1';
        navbar.style.boxShadow = '0px 4px 8px rgba(0,0,0,0.1)';
    } else {
        navbar.style.backgroundColor = '#fff';
        navbar.style.boxShadow = 'none';
    }
});

// Dark mode toggle button
document.addEventListener("DOMContentLoaded", function() {
    const toggle = document.createElement('button');
    toggle.textContent = "🌙";
    toggle.style.border = 'none';
    toggle.style.background = 'transparent';
    toggle.style.fontSize = '1.2rem';
    toggle.style.cursor = 'pointer';
    toggle.style.marginLeft = '10px';

    document.querySelector('.navbar-nav').appendChild(toggle);

    toggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        toggle.textContent = document.body.classList.contains('dark-mode') ? "☀️" : "🌙";
    });
});
// Equalize card heights to the tallest card on the page
function equalizeCardHeights() {
  const cards = Array.from(document.querySelectorAll('.course-card'));
  if (!cards.length) return;

  // reset first so we measure natural height
  cards.forEach(c => { c.style.minHeight = 'auto'; });

  // measure
  let max = 0;
  cards.forEach(c => {
    const h = c.getBoundingClientRect().height;
    if (h > max) max = h;
  });

  // set all to max
  cards.forEach(c => { c.style.minHeight = `${Math.ceil(max)}px`; });
}

// Debounce resize for performance
let resizeTimer = null;
function onResize() {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(equalizeCardHeights, 120);
}

// Re-run when images load (so late-loading images don't break heights)
function watchImages() {
  const imgs = document.querySelectorAll('.course-card img');
  imgs.forEach(img => {
    if (img.complete) return;
    img.addEventListener('load', equalizeCardHeights, { once: true });
    img.addEventListener('error', equalizeCardHeights, { once: true });
  });
}

// Observe DOM changes (e.g., when courses change dynamically)
const observer = new MutationObserver(() => {
  equalizeCardHeights();
  watchImages();
});

document.addEventListener('DOMContentLoaded', () => {
  equalizeCardHeights();
  watchImages();
  window.addEventListener('resize', onResize);

  const grid = document.querySelector('.courses-grid') || document.body;
  observer.observe(grid, { childList: true, subtree: true });
});

// As a final safety, run again after full load
window.addEventListener('load', equalizeCardHeights);
