import re

with open("index.html", "r") as f:
    content = f.read()

# I will use regex to remove the dummy blogs from the array
# Dummy 1: 'trends-in-aluminium-hardware-2026'
content = re.sub(r'\{\s*slug:\s*\'trends-in-aluminium-hardware-2026\'.*?image:\s*\'assets/blog_kitchen\.jpg\'\s*\},', '', content, flags=re.DOTALL)

# Dummy 2: 'how-to-choose-cabinet-handles'
content = re.sub(r'\{\s*slug:\s*\'how-to-choose-cabinet-handles\'.*?image:\s*\'assets/blog_wardrobe\.jpg\'\s*\}', '', content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Cleaned dummy blogs.")
