import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('Ã¢â‚¬â€ ', '&mdash;')
    content = content.replace('Ã¢â‚¬â€œ', '&ndash;')
    content = content.replace('Ã‚Â·', '&middot;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
