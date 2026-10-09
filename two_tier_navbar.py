import re

with open("index.html", "r") as f:
    content = f.read()

# 1. We replace the ENTIRE desktop navbar block with the two-tier setup.
target_pattern = r'<div class="hidden md:flex gap-5 md:gap-8 items-center flex-nowrap whitespace-nowrap flex-shrink-0 overflow-x-auto scrollbar-hide w-full justify-end px-2">.*?</nav>'

two_tier_html = """<div class="hidden md:flex gap-6 items-center flex-nowrap whitespace-nowrap justify-end w-full pl-6">
                <button onclick="navigate('home')" id="nav-home" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Home</button>
                <button onclick="navigate('process')" id="nav-process" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Our Process</button>
                <button onclick="navigate('blog')" id="nav-blog" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Blog</button>
                <button onclick="navigate('contact')" id="nav-contact" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Contact</button>
                
                <div class="w-px h-5 bg-brand-lightgray mx-1"></div>

                <button onclick="navigate('calculator')" id="nav-calculator" class="nav-link text-sm font-medium text-[#d4af37] hover:text-brand-black transition-colors flex items-center gap-1.5">
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg> Calculator
                </button>
                
                <button onclick="navigate('inquiry')" id="nav-inquiry" class="nav-link text-sm font-bold hover:text-brand-gray transition-colors flex items-center gap-1.5">
                    Inquiry List <span id="inquiry-badge" class="bg-brand-black text-white text-[10px] rounded-full w-5 h-5 flex items-center justify-center hidden shadow-sm">0</span>
                </button>
                
                <a href="#" onclick="openCatalogueModal(event)" class="text-sm font-bold bg-brand-black text-white px-6 py-2.5 rounded-full hover:opacity-80 transition-opacity ml-2 shadow-sm">
                    Catalogue
                </a>

                <button onclick="toggleDarkMode()" class="text-brand-gray hover:text-brand-black transition-colors p-2 rounded-full border border-brand-lightgray ml-1 bg-brand-offwhite" aria-label="Toggle Dark Mode">
                    <svg id="moon-icon" class="w-4 h-4 block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                    <svg id="sun-icon" class="w-4 h-4 hidden" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                </button>
            </div>
        </div>

        <!-- Secondary Product Categories Navbar -->
        <div class="hidden md:flex justify-center gap-12 bg-brand-offwhite border-t border-brand-lightgray py-3 shadow-sm relative z-40">
            <button onclick="navigate('200')" id="nav-200" class="nav-link text-xs font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors">Cabinet Handles</button>
            <button onclick="navigate('300')" id="nav-300" class="nav-link text-xs font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors">Cabinet Profiles</button>
            <button onclick="navigate('400')" id="nav-400" class="nav-link text-xs font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors">Counsil Handles</button>
            <button onclick="navigate('450')" id="nav-450" class="nav-link text-xs font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors">Sliding Counsils</button>
            <button onclick="navigate('500')" id="nav-500" class="nav-link text-xs font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors">Cabinet Knobs</button>
        </div>

        <!-- Mobile Menu Drawer Backdrop -->"""

content = re.sub(target_pattern, two_tier_html, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Two-tier navbar implemented.")
