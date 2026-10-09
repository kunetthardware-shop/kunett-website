import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update the Mobile Menu HTML
old_menu_pattern = r'<div id="mobile-menu" class="md:hidden absolute top-full left-0 w-full bg-white border-b border-brand-lightgray shadow-2xl transition-all duration-300 transform -translate-y-full opacity-0 pointer-events-none -z-10">.*?</div>\n        </div>'

new_menu_html = """
        <!-- Mobile Menu Drawer Backdrop -->
        <div id="mobile-backdrop" onclick="closeMobileMenu()" class="md:hidden fixed inset-0 bg-black/60 z-[90] transition-opacity duration-300 opacity-0 pointer-events-none"></div>

        <!-- Mobile Menu Drawer (Slide from Right) -->
        <div id="mobile-menu" class="md:hidden fixed top-0 right-0 w-[85vw] max-w-sm h-full bg-white shadow-2xl transition-transform duration-300 transform translate-x-full z-[100] flex flex-col">
            
            <div class="p-6 border-b border-brand-lightgray flex justify-between items-center bg-brand-offwhite">
                <span class="font-serif text-2xl text-brand-black font-bold">Menu</span>
                <button onclick="closeMobileMenu()" class="p-2 text-brand-black hover:text-brand-gray transition-colors bg-white rounded-full shadow-sm border border-brand-lightgray">
                    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>

            <div class="flex flex-col p-6 gap-2 text-base font-bold text-brand-black overflow-y-auto flex-grow pb-24">
                <button onclick="closeMobileMenu(); navigate('home')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Home</button>
                <button onclick="closeMobileMenu(); navigate('process')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Our Process</button>
                <button onclick="closeMobileMenu(); navigate('blog')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Blog</button>
                <button onclick="closeMobileMenu(); navigate('calculator')" class="text-left py-3 border-b border-brand-lightgray/50 text-[#d4af37] flex items-center justify-between">
                    Project Calculator <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg>
                </button>
                <button onclick="toggleDarkMode(); closeMobileMenu()" class="text-left py-3 border-b border-brand-lightgray/50 flex items-center justify-between hover:text-brand-gray">
                    <span id="mobile-dark-text">Toggle Dark Mode</span>
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                </button>
                <button onclick="closeMobileMenu(); navigate('200')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Handles</button>
                <button onclick="closeMobileMenu(); navigate('300')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Profiles</button>
                <button onclick="closeMobileMenu(); navigate('400')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Counsil Handles</button>
                <button onclick="closeMobileMenu(); navigate('450')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Sliding Counsils</button>
                <button onclick="closeMobileMenu(); navigate('500')" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Knobs</button>
                <button onclick="closeMobileMenu(); navigate('contact')" class="text-left py-3 border-b border-brand-lightgray/50 text-[#f59e0b]">Contact Us</button>
                <button onclick="closeMobileMenu(); navigate('inquiry')" class="text-left py-3 border-b border-brand-lightgray/50">My Inquiry List</button>
                <a href="#" onclick="closeMobileMenu(); openCatalogueModal(event)" class="mt-8 text-center text-sm bg-brand-black text-white px-5 py-4 rounded-full shadow-lg">Download Catalogue</a>
            </div>
        </div>"""

content = re.sub(old_menu_pattern, new_menu_html, content, flags=re.DOTALL)

# 2. Update the Mobile Menu JS Logic
old_js_pattern = r'// --- Mobile Menu Logic ---.*?function addToInquiry\(\)'

new_js = """// --- Mobile Menu Logic ---
        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            const backdrop = document.getElementById('mobile-backdrop');
            
            if (menu.classList.contains('translate-x-full')) {
                menu.classList.remove('translate-x-full');
                if(backdrop) backdrop.classList.remove('opacity-0', 'pointer-events-none');
                document.body.style.overflow = 'hidden'; // prevent scrolling
            } else {
                closeMobileMenu();
            }
        }

        function closeMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            const backdrop = document.getElementById('mobile-backdrop');
            
            if (menu && !menu.classList.contains('translate-x-full')) {
                menu.classList.add('translate-x-full');
                if(backdrop) backdrop.classList.add('opacity-0', 'pointer-events-none');
                document.body.style.overflow = ''; // restore scrolling
            }
        }

        function addToInquiry()"""

content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Slide drawer menu integrated.")
