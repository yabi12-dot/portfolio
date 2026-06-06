/* contact.js  Form handling */
const form = document.getElementById('contact-form');
const formSuccess = document.getElementById('form-success');

if (form) {
 form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name')?.value.trim();
  const email = document.getElementById('email')?.value.trim();
  const message = document.getElementById('message')?.value.trim();

  if (!name || !email || !message) {
   // Simple validation highlight
   [document.getElementById('name'), document.getElementById('email'), document.getElementById('message')].forEach(field => {
    if (field && !field.value.trim()) {
     field.style.borderColor = '#C1673A';
     field.addEventListener('input', () => { field.style.borderColor = ''; }, { once: true });
    }
   });
   return;
  }

  // Simulate submission
  const submitBtn = document.getElementById('contact-submit');
  if (submitBtn) {
   submitBtn.textContent = 'Sending...';
   submitBtn.disabled = true;
  }

  setTimeout(() => {
   form.hidden = true;
   if (formSuccess) formSuccess.hidden = false;
  }, 1200);
 });
}
