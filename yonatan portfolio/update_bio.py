import glob
import re

# 1. Fix about.html bio
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_bio_1 = r'Yonatan Nigussie is a passionate street and documentary photographer who began photography at a young age, first using his phone to capture real life as he saw it.*?people, daily moments, and sometimes nature.'
replacement_bio_1 = 'I am a passionate street and documentary photographer who began photography at a young age, first using my phone to capture real life as I saw it - people, daily moments, and sometimes nature.'
content = re.sub(target_bio_1, replacement_bio_1, content, flags=re.DOTALL)

target_bio_2 = r'What truly draws him is its honesty. He is deeply connected to the culture, the people, and the way faith and everyday life are lived.*?it is what drives him to document real, unstaged moments.'
replacement_bio_2 = 'What truly draws me is its honesty. I am deeply connected to the culture, the people, and the way faith and everyday life are lived - it is what drives me to document real, unstaged moments.'
content = re.sub(target_bio_2, replacement_bio_2, content, flags=re.DOTALL)

target_bio_3 = r'Nigussie has always been more interested in truth than in perfection, and this interest has deepened over time. He is currently a Film and TV Production student at the University of Gondar, and studying cinema has shaped the way he sees photography, especially in storytelling, light, and composition.'
replacement_bio_3 = 'I have always been more interested in truth than in perfection, and this interest has deepened over time. I am currently a Film and TV Production student at the University of Gondar, and studying cinema has shaped the way I see photography, especially in storytelling, light, and composition.'
content = re.sub(target_bio_3, replacement_bio_3, content, flags=re.DOTALL)

target_bio_4 = r'His most significant project to date was participation in the <em>Everyday Elsewhere</em> exchange between Addis Ababa and Weimar, Germany.*?work that was exhibited internationally and published in print and digital media.'
replacement_bio_4 = 'My most significant project to date was participation in the <em>Everyday Elsewhere</em> exchange between Addis Ababa and Weimar, Germany - work that was exhibited internationally and published in print and digital media.'
content = re.sub(target_bio_4, replacement_bio_4, content, flags=re.DOTALL)

content = content.replace('In His Own Words', 'In My Own Words')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Fix mojibake everywhere
html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('Ã¢â‚¬â€ ', '-')
    html = html.replace('Ã‚Â·', '·')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
