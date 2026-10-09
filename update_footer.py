import re

with open("index.html", "r") as f:
    content = f.read()

target = """<h4 class="font-bold text-brand-black mb-4">Resources</h4>
                <ul class="space-y-3 text-sm text-brand-gray">
                    <li><a href="#" onclick="openCatalogueModal(event)" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg> Digital Catalogue</a></li>
                </ul>"""

replacement = """<h4 class="font-bold text-brand-black mb-4">Resources</h4>
                <ul class="space-y-3 text-sm text-brand-gray">
                    <li><a href="#" onclick="navigate('blog')" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg> Architecture Blog</a></li>
                    <li><a href="#" onclick="openCatalogueModal(event)" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg> Digital Catalogue</a></li>
                    <li><a href="#" onclick="navigate('legal')" class="hover:text-[#f59e0b] font-medium transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg> Wholesale Terms</a></li>
                </ul>"""

content = content.replace(target, replacement)

with open("index.html", "w") as f:
    f.write(content)

print("Footer updated with explicit legal links.")
