/* main.js  Shared JavaScript for all pages */

// ── NAV SCROLL BEHAVIOUR ──────────────────────────────────────────────────────
const nav = document.getElementById('main-nav');
if (nav) {
 window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
 }, { passive: true });
}

// ── HAMBURGER MENU ────────────────────────────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
if (hamburger && navLinks) {
 hamburger.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  hamburger.setAttribute('aria-expanded', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
 });
 // Close on link click
 navLinks.querySelectorAll('.nav__link').forEach(link => {
  link.addEventListener('click', () => {
   navLinks.classList.remove('open');
   hamburger.setAttribute('aria-expanded', 'false');
   document.body.style.overflow = '';
  });
 });
}

// ── HERO IMAGE LOAD ANIMATION ─────────────────────────────────────────────────
const heroSection = document.getElementById('hero');
if (heroSection) {
 const heroImg = heroSection.querySelector('.hero__img');
 const activate = () => heroSection.classList.add('loaded');
 if (heroImg) {
  if (heroImg.complete) activate();
  else heroImg.addEventListener('load', activate);
 }
}

// ── SCROLL FADE-IN ────────────────────────────────────────────────────────────
const fadeEls = document.querySelectorAll('.fade-in');
if (fadeEls.length && 'IntersectionObserver' in window) {
 const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
   if (entry.isIntersecting) {
    setTimeout(() => entry.target.classList.add('visible'), i * 80);
    observer.unobserve(entry.target);
   }
  });
 }, { threshold: 0.12 });
 fadeEls.forEach(el => observer.observe(el));
} else {
 fadeEls.forEach(el => el.classList.add('visible'));
}

// ── ABOUT PAGE: ACCORDION Q&A ─────────────────────────────────────────────────
const qaItems = document.querySelectorAll('.qa-item');
qaItems.forEach(item => {
 const question = item.querySelector('.qa-question');
 const answer = item.querySelector('.qa-answer');
 if (!question || !answer) return;

 // Collapse all except first by default
 if (!item.classList.contains('open')) {
  answer.style.maxHeight = '0';
  answer.style.overflow = 'hidden';
  answer.style.transition = 'max-height 0.4s ease';
 } else {
  answer.style.maxHeight = answer.scrollHeight + 'px';
 }

 question.addEventListener('click', () => {
  const isOpen = item.classList.toggle('open');
  answer.style.maxHeight = isOpen ? answer.scrollHeight + 'px' : '0';
 });
});
// Open first by default
if (qaItems.length) {
 const first = qaItems[0];
 first.classList.add('open');
 const firstAnswer = first.querySelector('.qa-answer');
 if (firstAnswer) firstAnswer.style.maxHeight = firstAnswer.scrollHeight + 'px';
}
