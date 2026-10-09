import re

with open("index.html", "r") as f:
    content = f.read()

# Add scrollbar-hide CSS
css_target = ".product-img { transition: transform 0.4s ease; mix-blend-mode: multiply; }"
css_replacement = """
        .scrollbar-hide::-webkit-scrollbar { display: none; }
        .scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
        .product-img { transition: transform 0.4s ease; mix-blend-mode: multiply; }"""
if ".scrollbar-hide" not in content:
    content = content.replace(css_target, css_replacement)

# Update nav container
nav_target = '<div class="hidden md:flex gap-5 md:gap-8 items-center flex-nowrap whitespace-nowrap flex-shrink-0">'
nav_replacement = '<div class="hidden md:flex gap-5 md:gap-8 items-center flex-nowrap whitespace-nowrap flex-shrink-0 overflow-x-auto scrollbar-hide w-full justify-end px-2">'
if "scrollbar-hide w-full" not in content:
    content = content.replace(nav_target, nav_replacement)

with open("index.html", "w") as f:
    f.write(content)

print("Navbar overflow fixed.")
