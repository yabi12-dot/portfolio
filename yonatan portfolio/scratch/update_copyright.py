
import glob

# Update copyright year to 2026 in all HTML files
html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace 2024 with 2026 in the footer copyright line
    new_content = content.replace('&copy; 2024 Yonatan Nigussie', '&copy; 2026 Yonatan Nigussie')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated copyright year in {filepath}")
