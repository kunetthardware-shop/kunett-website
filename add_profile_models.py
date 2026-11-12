import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern to replace the Architectural Profiles product list
old_profiles = """${renderProductSlider([
                            products.find(p => p.code === '301'),
                            products.find(p => p.code === '303'),
                            products.find(p => p.code === '306'),
                            products.find(p => p.code === '312')
                        ].filter(Boolean))}"""

new_profiles = """${renderProductSlider([
                            products.find(p => p.code === '301'),
                            products.find(p => p.code === '303'),
                            products.find(p => p.code === '306'),
                            products.find(p => p.code === '308'),
                            products.find(p => p.code === '310'),
                            products.find(p => p.code === '312'),
                            products.find(p => p.code === '315'),
                            products.find(p => p.code === '318')
                        ].filter(Boolean))}"""

content = content.replace(old_profiles, new_profiles)

with open("index.html", "w") as f:
    f.write(content)

print("Added more models to Architectural Profiles.")
