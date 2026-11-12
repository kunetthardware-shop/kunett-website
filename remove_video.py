import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern to remove the video block
video_pattern = r'<video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-multiply">\s*<source src="assets/Code_204_Compressed\.mp4" type="video/mp4">\s*</video>'

content = re.sub(video_pattern, '', content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Video removed.")
