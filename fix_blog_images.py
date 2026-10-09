import re

with open("index.html", "r") as f:
    content = f.read()

# I will find the blog objects. 
# Blog 1: aluminium-vs-steel-handles-for-new-home (currently assets/blog_wardrobe.jpg)
# Blog 2: how-to-choose-aluminium-handle-for-wardrobe (currently assets/blog_kitchen.jpg)
# Blog 3: aluminium-profile-handles-modern-modular-furniture (currently assets/blog_wardrobe.jpg)

# Let's replace the image for the first blog (Aluminium vs Steel) to blog_kitchen
content = re.sub(
    r"(slug: 'aluminium-vs-steel-handles-for-new-home'.*?image: 'assets/)blog_wardrobe\.jpg(')",
    r"\1blog_kitchen.jpg\2",
    content,
    flags=re.DOTALL
)

# Let's replace the image for the second blog (Wardrobe) to blog_wardrobe
content = re.sub(
    r"(slug: 'how-to-choose-aluminium-handle-for-wardrobe'.*?image: 'assets/)blog_kitchen\.jpg(')",
    r"\1blog_wardrobe.jpg\2",
    content,
    flags=re.DOTALL
)

# Let's replace the image for the third blog (Profile handles) to blog_profile
content = re.sub(
    r"(slug: 'aluminium-profile-handles-modern-modular-furniture'.*?image: 'assets/)blog_wardrobe\.jpg(')",
    r"\1blog_profile.jpg\2",
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)

print("Blog images updated.")
