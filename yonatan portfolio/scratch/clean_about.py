
import os

filepath = 'about.html'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # The user specifically wants to "delete" this string.
    # We'll replace it and its variants with a simple hyphen for clean look.
    # It seems there are trailing hidden characters in some cases.
    
    # Replace the specific mangled string
    content = content.replace('Ã¢â‚¬â€', '-')
    # Also replace the &mdash; we might have introduced
    content = content.replace('&mdash;', '-')
    
    # Clean up any resulting double hyphens or weird space patterns
    import re
    content = re.sub(r'-[ \t\r\n\xa0Â]+', '- ', content)
    content = re.sub(r' +', ' ', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {filepath}")
