import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern to find the header inside page === 'home'
header_pattern = r'(<header class="relative w-full h-\[90vh\] md:h-\[80vh\] bg-brand-offwhite flex items-center justify-center overflow-hidden">)\s*(<div class="relative z-10 text-center px-4 flex flex-col items-center">)'

# Replacement with video
replacement = r'''\1
                        <video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-multiply">
                            <source src="assets/Code_204_Compressed.mp4" type="video/mp4">
                        </video>
                        \2'''

content = re.sub(header_pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Video added back.")
