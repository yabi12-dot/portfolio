import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the "Faces Untold" filter button
content = re.sub(r'\s*<button class="filter-btn" data-filter="faces-untold" id="filter-faces">Faces Untold</button>', '', content)

# 2. Remove the "Faces Untold" section
faces_pattern = r'  <!-- SERIES: FACES UNTOLD -->\n  <section class="work-series" id="faces-untold".*?</section>\n'
content = re.sub(faces_pattern, '', content, flags=re.DOTALL)

# 3. Update meta description to remove Faces Untold
content = content.replace(', Faces Untold', '')

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(content)
