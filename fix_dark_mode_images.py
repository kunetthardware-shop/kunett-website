import re

with open("index.html", "r") as f:
    content = f.read()

# We need to enhance the dark mode CSS block
target_css = """/* Dark Mode Overrides */"""
replacement_css = """/* Dark Mode Overrides */
        html.dark body { background-color: #0a0a0a !important; color: #ffffff !important; }
        html.dark .bg-brand-offwhite { background-color: #141414 !important; }
        html.dark .bg-white { background-color: #0a0a0a !important; border-color: #2a2a2a !important; }
        html.dark .text-brand-black { color: #ffffff !important; }
        html.dark .text-brand-gray { color: #a0a0a0 !important; }
        html.dark .border-brand-lightgray { border-color: #2a2a2a !important; }
        html.dark .bg-brand-black { background-color: #d4af37 !important; color: #000000 !important; }
        
        /* FIX FOR IMAGES IN DARK MODE: 
           Remove multiply (which makes them vanish) and give them a clean white card background 
           so the handles are perfectly visible. */
        html.dark .product-img { mix-blend-mode: normal !important; }
        html.dark img.mix-blend-multiply { mix-blend-mode: normal !important; }
        
        /* Product Grid Containers */
        html.dark .bg-brand-offwhite.aspect-square { background-color: #ffffff !important; padding: 10px !important; }
        html.dark .bg-brand-offwhite.aspect-square img { filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1)); }
        
        /* Product Detail Page Container */
        html.dark .bg-brand-offwhite.rounded-3xl.min-h-\[50vh\] { background-color: #ffffff !important; }
        
        /* Finish Studio Mask/Overlay fix */
        html.dark #studio-color-overlay { mix-blend-mode: normal !important; opacity: 0.8 !important; }
        html.dark #studio-handle-img { filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5)) !important; }
"""

# Let's completely replace the old dark mode overrides
old_block_pattern = r'/\* Dark Mode Overrides \*/.*?(?=</style>)'
content = re.sub(old_block_pattern, replacement_css, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Dark Mode images fixed.")
