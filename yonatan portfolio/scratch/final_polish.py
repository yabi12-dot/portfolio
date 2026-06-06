
import os
import glob
import re

# Final cleanup of double spaces in all HTML files
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace any double spaces with a single space
    # but be careful not to mess up HTML indentation (which we'll assume is at start of lines)
    
    # Use a regex that only matches double spaces within text, not at the start of lines
    # This is tricky, but we can do a simpler version:
    # Replace double space with single space if it's NOT at the beginning of a line.
    
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        # Keep leading whitespace
        match = re.match(r'^(\s*)', line)
        indent = match.group(1) if match else ''
        rest = line[len(indent):]
        # Replace multiple spaces with one in the rest of the line
        rest = re.sub(r' +', ' ', rest)
        new_lines.append(indent + rest)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned extra spaces in {filepath}")
