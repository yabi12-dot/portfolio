import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the "Rural Rhythms" filter button
content = re.sub(r'\s*<button class="filter-btn" data-filter="rural-rhythms" id="filter-rural">Rural Rhythms</button>', '', content)

# 2. Remove the "Rural Rhythms" section
rural_pattern = r'  <!-- SERIES: RURAL RHYTHMS -->\n  <section class="work-series" id="rural-rhythms".*?</section>\n'
content = re.sub(rural_pattern, '', content, flags=re.DOTALL)

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(content)
