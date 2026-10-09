import re

with open("index.html", "r") as f:
    content = f.read()

# Desktop Nav target
desktop_target = """<button onclick="navigate('blog')" id="nav-blog" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors pb-1">Blog</button>"""
desktop_replace = """<button onclick="navigate('blog')" id="nav-blog" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors pb-1">Blog</button>
                <button onclick="navigate('calculator')" id="nav-calculator" class="nav-link text-sm font-medium text-[#d4af37] hover:text-brand-gray transition-colors pb-1 flex items-center gap-1">
                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg> Calculator
                </button>
                <button onclick="toggleDarkMode()" class="text-brand-gray hover:text-brand-black transition-colors p-1.5 rounded-full border border-brand-lightgray ml-2" aria-label="Toggle Dark Mode">
                    <svg id="moon-icon" class="w-4 h-4 block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                    <svg id="sun-icon" class="w-4 h-4 hidden" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                </button>"""

if "navigate('calculator')" not in content:
    content = content.replace(desktop_target, desktop_replace)

# Mobile Nav target
mobile_target = """<button onclick="closeMobileMenu(); navigate('blog')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Blog</button>"""
mobile_replace = """<button onclick="closeMobileMenu(); navigate('blog')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Blog</button>
                <button onclick="closeMobileMenu(); navigate('calculator')" class="text-left py-3 border-b border-brand-lightgray/50 text-[#d4af37] flex items-center justify-between">
                    Project Calculator <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg>
                </button>
                <button onclick="toggleDarkMode(); closeMobileMenu()" class="text-left py-3 border-b border-brand-lightgray/50 flex items-center justify-between hover:text-brand-gray">
                    <span id="mobile-dark-text">Toggle Dark Mode</span>
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                </button>"""

if "Project Calculator" not in content:
    content = content.replace(mobile_target, mobile_replace)

with open("index.html", "w") as f:
    f.write(content)

print("Navbar fixed.")
