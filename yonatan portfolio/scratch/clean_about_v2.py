
import os
import re

filepath = 'about.html'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Specifically target the pattern " -  " or any variation with the mangled dash
# We'll replace it with a single space as per "delete" instruction
# or a simple hyphen if it feels better.
# But let's try to just remove the double space.

# First, replace the hyphen and any sequence of spaces/junk with a hyphen and one space
content = re.sub(r'-\s+', '- ', content)

# Also fix the title specifically
content = content.replace('<title>About - Yonatan Nigussie</title>', '<title>About Yonatan Nigussie</title>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated about.html")
