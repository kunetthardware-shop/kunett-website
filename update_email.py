import re

with open("index.html", "r") as f:
    content = f.read()

# Case-insensitive replacement of the old gmail address
content = re.sub(r'kunetthardware@gmail\.com', 'support@kunetthardware.com', content, flags=re.IGNORECASE)

with open("index.html", "w") as f:
    f.write(content)

print("Email updated.")
