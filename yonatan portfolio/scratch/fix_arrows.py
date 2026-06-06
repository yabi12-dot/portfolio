
import os
import glob

# Fix mangled arrows project-wide
html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Mangled arrow UTF-8
    mangled_arrow = 'Ã¢â€ â€™'.encode('utf-8')
    # Target arrow (right arrow)
    target_arrow = '&rarr;'.encode('utf-8')
    
    if mangled_arrow in data:
        new_data = data.replace(mangled_arrow, target_arrow)
        with open(filepath, 'wb') as f:
            f.write(new_data)
        print(f"Fixed arrows in {filepath}")
