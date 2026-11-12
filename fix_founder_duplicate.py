import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Fix the original split-screen Founder block (remove grayscale, fix image source)
old_img_tag = r'<img src="assets/founder\.jpg" class="w-full h-full object-cover grayscale opacity-90 transition-transform duration-1000 hover:scale-105" alt="Sanjay Patel" onerror="this\.src=\'assets/blog1_header\.jpg\'">'
new_img_tag = '<img src="assets/sanjay_patel.jpg" class="w-full h-full object-cover transition-transform duration-1000 hover:scale-105" alt="Sanjay Patel">'
content = re.sub(old_img_tag, new_img_tag, content)

# 2. Delete the new duplicate Founder section I just added
new_founder_section = r'<!-- Founder Section -->[\s\S]*?<!-- SEO Optimized Content Block -->'
content = re.sub(new_founder_section, '<!-- SEO Optimized Content Block -->', content)

with open("index.html", "w") as f:
    f.write(content)

print("Duplicates fixed, image updated.")
