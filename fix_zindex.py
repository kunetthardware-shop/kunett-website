import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r'<div id="catalogue-modal" class="drawer-overlay fixed inset-0 z-\[60\] bg-black/60 flex justify-center items-center p-4">'
replacement = '<div id="catalogue-modal" class="drawer-overlay fixed inset-0 z-[9999] bg-black/60 flex justify-center items-center p-4">'
content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Z-index fixed.")
