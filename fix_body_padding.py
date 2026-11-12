import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r'<body class="bg-brand-offwhite text-brand-black font-sans antialiased overflow-x-hidden pt-20 selection:bg-brand-black selection:text-white">'
replacement = '<body class="bg-brand-offwhite text-brand-black font-sans antialiased overflow-x-hidden selection:bg-brand-black selection:text-white">'

content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Body padding removed.")
