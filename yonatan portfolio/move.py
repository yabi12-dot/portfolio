import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reorder buttons
content = content.replace(
'''      <button class="filter-btn active" data-filter="all" id="filter-all">All</button>
      <button class="filter-btn" data-filter="morning-gondar" id="filter-morning">Morning in Gondar</button>
      <button class="filter-btn" data-filter="rural-rhythms" id="filter-rural">Rural Rhythms</button>
      <button class="filter-btn" data-filter="faces-untold" id="filter-faces">Faces Untold</button>
      <button class="filter-btn" data-filter="kuskuam-church" id="filter-kuskuam">Kuskuam Church</button>''',
'''      <button class="filter-btn active" data-filter="all" id="filter-all">All</button>
      <button class="filter-btn" data-filter="kuskuam-church" id="filter-kuskuam">Kuskuam Church</button>
      <button class="filter-btn" data-filter="morning-gondar" id="filter-morning">Morning in Gondar</button>
      <button class="filter-btn" data-filter="rural-rhythms" id="filter-rural">Rural Rhythms</button>
      <button class="filter-btn" data-filter="faces-untold" id="filter-faces">Faces Untold</button>'''
)

# 2. Extract Kuskuam Church section
kuskuam_pattern = r'(  <!-- SERIES: KUSKUAM CHURCH -->\n  <section class="work-series" id="kuskuam-church" data-series="kuskuam-church">.*?</section>\n)'
match = re.search(kuskuam_pattern, content, re.DOTALL)
if match:
    kuskuam_section = match.group(1)
    # Remove from original position
    content = content.replace(kuskuam_section + '\n', '')
    content = content.replace(kuskuam_section, '')

    # Insert before Morning in Gondar
    morning_gondar_marker = '  <!-- SERIES: Morning in Gondar -->'
    content = content.replace(morning_gondar_marker, kuskuam_section + '\n' + morning_gondar_marker)

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(content)
