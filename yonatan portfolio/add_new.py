import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add button
button_target = '      <button class="filter-btn" data-filter="faces-untold" id="filter-faces">Faces Untold</button>'
button_replacement = button_target + '\n      <button class="filter-btn" data-filter="new-documentary" id="filter-new">New Documentary</button>'
content = content.replace(button_target, button_replacement)

# Add section
section_html = """
  <!-- SERIES: NEW DOCUMENTARY -->
  <section class="work-series" id="new-documentary" data-series="new-documentary">
    <div class="work-series__header">
      <div class="work-series__header-text">
        <span class="section-label">Documentary</span>
        <h2 class="work-series__title">New Documentary</h2>
        <p class="work-series__desc">Description coming soon...</p>
      </div>
      <div class="work-series__header-meta">
        <div class="meta-item"><span class="meta-label">Location</span><span class="meta-value">TBD</span></div>
        <div class="meta-item"><span class="meta-label">Year</span><span class="meta-value">2024</span></div>
        <div class="meta-item"><span class="meta-label">Frames</span><span class="meta-value">8 Photographs</span></div>
      </div>
    </div>
    <div class="photo-grid photo-grid--masonry" id="grid-new">
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="a.jpg" alt="Documentary image A" /><div class="photo-item__overlay"><p>Image A</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="b.jpg" alt="Documentary image B" /><div class="photo-item__overlay"><p>Image B</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="c.jpg" alt="Documentary image C" /><div class="photo-item__overlay"><p>Image C</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="d.jpg" alt="Documentary image D" /><div class="photo-item__overlay"><p>Image D</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="e.jpg" alt="Documentary image E" /><div class="photo-item__overlay"><p>Image E</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="f.jpg" alt="Documentary image F" /><div class="photo-item__overlay"><p>Image F</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="g.jpg" alt="Documentary image G" /><div class="photo-item__overlay"><p>Image G</p></div></div></div>
      <div class="photo-item" data-series="new-documentary"><div class="photo-item__wrap"><img src="h.jpg" alt="Documentary image H" /><div class="photo-item__overlay"><p>Image H</p></div></div></div>
    </div>
  </section>
"""

content = content.replace('  <!-- LIGHTBOX -->', section_html + '\n  <!-- LIGHTBOX -->')

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(content)
