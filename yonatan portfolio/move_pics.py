import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the "New Documentary" filter button
content = content.replace('\n      <button class="filter-btn" data-filter="new-documentary" id="filter-new">New Documentary</button>', '')

# 2. Remove the "New Documentary" section
new_doc_pattern = r'  <!-- SERIES: NEW DOCUMENTARY -->\n  <section class="work-series" id="new-documentary".*?</section>\n'
content = re.sub(new_doc_pattern, '', content, flags=re.DOTALL)

# 3. Replace the contents of grid-morning
new_grid_content = '''    <div class="photo-grid photo-grid--masonry" id="grid-morning">
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="a.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="b.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="c.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="d.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="e.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="f.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="g.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
      <div class="photo-item" data-series="morning-gondar"><div class="photo-item__wrap"><img src="h.jpg" alt="Morning in Gondar" /><div class="photo-item__overlay"><p>Morning in Gondar</p></div></div></div>
    </div>'''

grid_pattern = r'    <div class="photo-grid photo-grid--masonry" id="grid-morning">.*?    </div>'
content = re.sub(grid_pattern, new_grid_content, content, flags=re.DOTALL)

# 4. Update frame count for Morning in Gondar
content = content.replace('<div class="meta-item"><span class="meta-label">Frames</span><span class="meta-value">12 Photographs</span></div>', '<div class="meta-item"><span class="meta-label">Frames</span><span class="meta-value">8 Photographs</span></div>')

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(content)
