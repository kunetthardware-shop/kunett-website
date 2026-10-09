with open("index.html", "r") as f:
    content = f.read()

# Add the video fix to the dark mode CSS
target = "html.dark img.mix-blend-multiply { mix-blend-mode: normal !important; }"
replacement = """html.dark img.mix-blend-multiply { mix-blend-mode: normal !important; }
        html.dark video.mix-blend-multiply { mix-blend-mode: screen !important; opacity: 0.4 !important; filter: grayscale(100%); }
        /* Alternative: just normal mode, but screen looks cooler for dark mode */
        html.dark header video { mix-blend-mode: normal !important; opacity: 0.3 !important; }"""

if "html.dark header video" not in content:
    content = content.replace(target, replacement)

with open("index.html", "w") as f:
    f.write(content)

print("Video dark mode fixed.")
