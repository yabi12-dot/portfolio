
import os
import glob

html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Replace the \xc2\x9d character we found in the hex dump
    # And also any \xc2\x80 \xc2\x94 etc if they exist
    # But specifically \xc2\x9d which was causing the "A?" look
    cleaned_data = data.replace(b'\xc2\x9d', b'')
    
    # Also replace any sequence like b'-  ' with b'- '
    cleaned_data = cleaned_data.replace(b'-  ', b'- ')
    
    if cleaned_data != data:
        with open(filepath, 'wb') as f:
            f.write(cleaned_data)
        print(f"Cleaned binary artifacts from {filepath}")
