with open("index.html", "r") as f:
    content = f.read()

# 1. Update Homepage SEO Paragraph
target1 = "Our solid, aerospace-grade aluminium handles are meticulously crafted to endure daily wear while elevating modern interior spaces. Whether you are outfitting a luxury residential project, a modular kitchen, or sourcing bulk custom hardware for commercial architecture, KUNETT delivers precision, ergonomic design, and striking aesthetic finishes."
replacement1 = "Our solid, aerospace-grade aluminium handles are meticulously crafted to endure daily wear while elevating modern interior spaces. Whether you are outfitting a luxury residential project, a modular kitchen, or sourcing bulk custom hardware for commercial architecture, KUNETT delivers precision, ergonomic design, and striking aesthetic finishes. For more insights on architectural hardware, read our <a href=\"#\" onclick=\"navigate('blog')\" class=\"text-brand-black hover:underline font-bold\">Design & Architecture Blog</a> or learn about the industrial properties of <a href=\"https://en.wikipedia.org/wiki/Aluminium_alloy\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"text-brand-black hover:underline font-bold\">Aerospace-Grade Aluminium Alloys</a> used in our manufacturing process."

content = content.replace(target1, replacement1)

# 2. Update Process Page
target2 = "Our manufacturing floor utilizes state-of-the-art VMC (Vertical Machining Centers) to shape every aluminium profile with absolute precision. Once milled, every piece goes through a meticulous buffing process to ensure a flawless, smooth texture before coloring.</p>"
replacement2 = """Our manufacturing floor utilizes state-of-the-art <a href="https://en.wikipedia.org/wiki/Milling_(machining)#Computer_numerical_control" target="_blank" rel="noopener noreferrer" class="text-[#f59e0b] hover:underline font-bold">VMC (Vertical Machining Centers)</a> to shape every aluminium profile with absolute precision. Once milled, every piece goes through a meticulous buffing process to ensure a flawless, smooth texture before coloring.</p>
                                <p class="text-brand-gray leading-relaxed mb-6">Discover exactly why precision-milled aluminium is replacing steel in luxury homes by reading our <a href="#" onclick="navigate('blog-post', 'aluminium-vs-steel-handles-for-new-home')" class="text-[#f59e0b] hover:underline font-bold">Aluminium vs Steel Design Guide</a>.</p>"""

content = content.replace(target2, replacement2)

# 3. Update Footer Local SEO
target3 = "Gujarat, India"
replacement3 = "<a href=\"https://maps.app.goo.gl/EMsseMvKHpNqxPVh9\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"hover:text-[#f59e0b] transition-colors font-bold\">Rajkot, Gujarat, India</a>"

content = content.replace(target3, replacement3)

with open("index.html", "w") as f:
    f.write(content)

print("Site-wide SEO links injected successfully.")
