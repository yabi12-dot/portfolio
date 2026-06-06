/* work.js  Lightbox and series filter */

document.addEventListener('DOMContentLoaded', () => {
  // ── SERIES FILTER ─────────────────────────────────────────────────────────────
  const filterBtns = document.querySelectorAll('.filter-btn');
  const workSeries = document.querySelectorAll('.work-series');
  const comingSoon = document.querySelector('.coming-soon-message');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;
      
      // Update active button state
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Toggle project sections
      workSeries.forEach(section => {
        const series = section.dataset.series;
        if (filter === 'all' || series === filter) {
          section.style.display = 'block';
          section.classList.remove('hidden');
        } else {
          section.style.display = 'none';
          section.classList.add('hidden');
        }
      });

      // Toggle coming soon message
      if (comingSoon) {
        comingSoon.style.display = (filter === 'all') ? 'block' : 'none';
      }
    });
  });

  // ── LIGHTBOX ──────────────────────────────────────────────────────────────────
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxClose = document.getElementById('lightbox-close');
  const lightboxPrev = document.getElementById('lightbox-prev');
  const lightboxNext = document.getElementById('lightbox-next');

  let currentIndex = 0;
  let currentImages = [];

  const photoItems = document.querySelectorAll('.photo-item');

  photoItems.forEach((item) => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      if (!img) return;

      const seriesAttr = item.dataset.series;
      const seriesPhotos = Array.from(
        seriesAttr 
          ? document.querySelectorAll(`.photo-item[data-series="${seriesAttr}"]`)
          : photoItems
      );

      currentImages = seriesPhotos.map(el => ({
        src: el.querySelector('img')?.src || '',
        alt: el.querySelector('img')?.alt || '',
        caption: el.querySelector('.photo-item__overlay p')?.textContent || ''
      }));

      currentIndex = currentImages.findIndex(i => i.src === img.src);
      openLightbox();
    });
  });

  function openLightbox() {
    const current = currentImages[currentIndex];
    if (!current || !lightbox) return;
    
    lightboxImg.src = current.src;
    lightboxImg.alt = current.alt;
    lightboxCaption.textContent = current.caption;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  if (lightboxPrev) {
    lightboxPrev.addEventListener('click', (e) => {
      e.stopPropagation();
      currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
      openLightbox();
    });
  }
  if (lightboxNext) {
    lightboxNext.addEventListener('click', (e) => {
      e.stopPropagation();
      currentIndex = (currentIndex + 1) % currentImages.length;
      openLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!lightbox || !lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') {
      currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
      openLightbox();
    }
    if (e.key === 'ArrowRight') {
      currentIndex = (currentIndex + 1) % currentImages.length;
      openLightbox();
    }
  });
});
