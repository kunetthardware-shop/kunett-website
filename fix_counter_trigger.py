import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r"mainContent\.style\.transform = 'translateY\(0\)';"
replacement = "mainContent.style.transform = 'translateY(0)';\n                if (page === 'home' && typeof initCounters === 'function') initCounters();"

content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Trigger added.")
