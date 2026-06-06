
import os
import glob

# Project-wide cleanup of the em-dash character as requested
for root, dirs, files in os.walk('.'):
  for filename in files:
    if filename.endswith(('.html', '.js', '.css', '.md', '.py')):
      filepath = os.path.join(root, filename)
      try:
        with open(filepath, 'rb') as f:
          data = f.read()
        
        # Replace the UTF-8 em-dash (e2 80 94) with a space or nothing
        # The user said "delete", so we'll remove it.
        # If it's between words, we should probably ensure there's at least one space.
        
        # Literal em-dash
        em_dash_utf8 = ' '.encode('utf-8')
        
        if em_dash_utf8 in data:
          # Replace em-dash with a single space to avoid running words together
          new_data = data.replace(em_dash_utf8, b' ')
          
          # Clean up any resulting double spaces
          new_data = new_data.replace(b' ', b' ')
          
          with open(filepath, 'wb') as f:
            f.write(new_data)
          print(f"Removed em-dashes from {filepath}")
      except Exception as e:
        print(f"Could not process {filepath}: {e}")
