with open("index.html", "r") as f:
    content = f.read()

# Remove the broken dark mode override that turns black backgrounds into gold
content = content.replace("html.dark .bg-brand-black { background-color: #d4af37 !important; color: #000000 !important; }", "")

# Ensure the calculator box explicitly stays dark with high-contrast text
# (Just in case, we'll give it a solid dark style)
content = content.replace('<div class="bg-brand-black text-white p-8 rounded-2xl flex flex-col justify-center">',
                          '<div class="bg-[#111111] text-white p-8 rounded-2xl flex flex-col justify-center border border-[#333333]">')

with open("index.html", "w") as f:
    f.write(content)

print("Calculator colors fixed.")
