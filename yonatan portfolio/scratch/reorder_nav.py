
import os
import glob
import re

# New navigation order
new_nav_links = """
      <li><a href="index.html" class="nav__link">Home</a></li>
      <li><a href="about.html" class="nav__link">About</a></li>
      <li><a href="journal.html" class="nav__link">Journal</a></li>
      <li><a href="work.html" class="nav__link">Work</a></li>
      <li><a href="contact.html" class="nav__link nav__link--cta">Contact</a></li>
"""

# Footer links reorder
new_footer_links = """
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="journal.html">Journal</a>
        <a href="work.html">Work</a>
        <a href="contact.html">Contact</a>
"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reorder Nav Links
    # We use a broad regex to find the nav__links list and replace its interior
    content = re.sub(
        r'(<ul class="nav__links"[^>]*>).*?(</ul>)',
        lambda m: f"{m.group(1)}{new_nav_links}{m.group(2)}",
        content,
        flags=re.DOTALL
    )
    
    # Update active class based on filename
    basename = os.path.basename(filepath)
    content = content.replace('class="nav__link">', 'class="nav__link">') # Reset
    content = re.sub(r'class="nav__link active"', 'class="nav__link"', content)
    
    if basename == 'index.html':
        content = content.replace('href="index.html" class="nav__link"', 'href="index.html" class="nav__link active"')
    else:
        content = content.replace(f'href="{basename}" class="nav__link"', f'href="{basename}" class="nav__link active"')

    # Reorder Footer Links
    content = re.sub(
        r'(<nav class="footer__nav"[^>]*>).*?(</nav>)',
        lambda m: f"{m.group(1)}{new_footer_links}{m.group(2)}",
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Reordered navigation in {filepath}")
