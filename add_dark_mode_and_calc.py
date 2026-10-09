import re

with open("index.html", "r") as f:
    content = f.read()

# 1. ADD DARK MODE STYLES
dark_mode_css = """
        /* Dark Mode Overrides */
        html.dark body { background-color: #0a0a0a !important; color: #ffffff !important; }
        html.dark .bg-brand-offwhite { background-color: #141414 !important; }
        html.dark .bg-white { background-color: #0a0a0a !important; border-color: #2a2a2a !important; }
        html.dark .text-brand-black { color: #ffffff !important; }
        html.dark .text-brand-gray { color: #a0a0a0 !important; }
        html.dark .border-brand-lightgray { border-color: #2a2a2a !important; }
        html.dark .bg-brand-black { background-color: #d4af37 !important; color: #000000 !important; }
        html.dark .hover\:text-brand-black:hover { color: #d4af37 !important; }
        html.dark .hover\:border-brand-black:hover { border-color: #d4af37 !important; }
        html.dark .active { border-color: #d4af37 !important; color: #d4af37 !important; }
        html.dark img.mix-blend-multiply { mix-blend-mode: normal !important; filter: drop-shadow(0px 10px 20px rgba(255,255,255,0.05)); }
        html.dark .shadow-sm, html.dark .shadow-md, html.dark .shadow-2xl, html.dark .shadow-lg { box-shadow: 0 4px 30px rgba(0,0,0,0.5) !important; }
"""
if "html.dark body" not in content:
    content = content.replace("</style>", dark_mode_css + "\n    </style>")

# 2. ADD DARK MODE TOGGLE TO NAVBAR & CALCULATOR LINK
desktop_nav_target = """<a href="#" id="nav-blog" onclick="navigate('blog')" class="nav-link text-sm font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors py-2">Blog</a>"""
desktop_nav_replace = desktop_nav_target + """
                <a href="#" id="nav-calculator" onclick="navigate('calculator')" class="nav-link text-sm font-bold uppercase tracking-widest text-brand-gray hover:text-brand-black transition-colors py-2">Calculator</a>
                <button onclick="toggleDarkMode()" class="text-brand-gray hover:text-brand-black transition-colors p-2 rounded-full border border-brand-lightgray ml-2" aria-label="Toggle Dark Mode">
                    <svg id="moon-icon" class="w-4 h-4 block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                    <svg id="sun-icon" class="w-4 h-4 hidden" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                </button>"""
if "navigate('calculator')" not in content:
    content = content.replace(desktop_nav_target, desktop_nav_replace)

mobile_nav_target = """<a href="#" id="mobile-nav-blog" onclick="navigate('blog'); toggleMobileMenu()" class="nav-link text-xl font-serif text-brand-black py-2">Blog</a>"""
mobile_nav_replace = mobile_nav_target + """
                <a href="#" id="mobile-nav-calculator" onclick="navigate('calculator'); toggleMobileMenu()" class="nav-link text-xl font-serif text-brand-black py-2">Calculator</a>
                <button onclick="toggleDarkMode(); toggleMobileMenu()" class="flex items-center gap-4 text-xl font-serif text-brand-black py-2 mt-4 border-t border-brand-lightgray pt-6">
                    <span id="mobile-dark-text">Dark Mode</span>
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"></path></svg>
                </button>"""
if "mobile-nav-calculator" not in content:
    content = content.replace(mobile_nav_target, mobile_nav_replace)

# 3. ADD JS FOR DARK MODE AND CALCULATOR ROUTE
js_target = "} else if (page === 'legal') {"
js_replace = """} else if (page === 'calculator') {
                let html = `
                    <div class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-b border-brand-lightgray">
                        <div class="max-w-4xl mx-auto text-center">
                            <h1 class="font-serif text-4xl md:text-5xl text-brand-black mb-6 leading-tight">B2B Project Calculator</h1>
                            <p class="text-brand-gray text-base md:text-xl leading-relaxed max-w-2xl mx-auto">Instantly estimate hardware requirements and weight savings for your upcoming interior projects.</p>
                        </div>
                    </div>
                    <section class="py-12 md:py-20 px-4 md:px-6 max-w-4xl mx-auto min-h-[50vh]">
                        <div class="bg-white border border-brand-lightgray rounded-3xl p-8 md:p-12 shadow-sm">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
                                <div>
                                    <h3 class="font-serif text-2xl font-bold mb-6 text-brand-black">Project Details</h3>
                                    <div class="space-y-6">
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Number of Modular Kitchens</label>
                                            <input type="number" id="calc-kitchens" value="5" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Number of Wardrobes</label>
                                            <input type="number" id="calc-wardrobes" value="10" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Average Drawers/Cabinets per unit</label>
                                            <input type="number" id="calc-drawers" value="8" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-brand-black text-white p-8 rounded-2xl flex flex-col justify-center">
                                    <h3 class="font-serif text-2xl font-bold mb-8 text-brand-offwhite">Estimated Hardware</h3>
                                    
                                    <div class="space-y-6">
                                        <div>
                                            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Total Handles Needed</p>
                                            <p class="text-3xl font-serif text-[#d4af37]" id="res-handles">120</p>
                                        </div>
                                        <div>
                                            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Est. Aluminium Profile Length</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-profiles">360 meters</p>
                                        </div>
                                        <div class="pt-6 border-t border-gray-700">
                                            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Weight Savings vs Steel</p>
                                            <p class="text-2xl font-serif text-[#25D366] flex items-center gap-2" id="res-weight">
                                                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
                                                68 kg lighter
                                            </p>
                                            <p class="text-[10px] text-gray-500 mt-2">Aluminium puts significantly less stress on hinges, increasing furniture lifespan.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `;
                mainContent.innerHTML = html;
                setTimeout(calculateROI, 100);
            } else if (page === 'legal') {"""
if "} else if (page === 'calculator') {" not in content:
    content = content.replace(js_target, js_replace)

js_helpers = """
        function toggleDarkMode() {
            document.documentElement.classList.toggle('dark');
            const isDark = document.documentElement.classList.contains('dark');
            const moon = document.getElementById('moon-icon');
            const sun = document.getElementById('sun-icon');
            if (moon) moon.classList.toggle('hidden', isDark);
            if (sun) sun.classList.toggle('hidden', !isDark);
            
            const mobText = document.getElementById('mobile-dark-text');
            if (mobText) mobText.textContent = isDark ? 'Light Mode' : 'Dark Mode';
        }

        function calculateROI() {
            const kitchens = parseInt(document.getElementById('calc-kitchens')?.value || 0);
            const wardrobes = parseInt(document.getElementById('calc-wardrobes')?.value || 0);
            const drawers = parseInt(document.getElementById('calc-drawers')?.value || 0);
            
            const totalUnits = kitchens + wardrobes;
            const totalHandles = totalUnits * drawers;
            const profileMeters = totalHandles * 0.6; // avg 60cm per handle
            
            // Aluminium is ~3x lighter than steel. 
            const weightSavingsKg = (totalHandles * 0.2).toFixed(1);
            
            const resHandles = document.getElementById('res-handles');
            const resProfiles = document.getElementById('res-profiles');
            const resWeight = document.getElementById('res-weight');
            
            if(resHandles) resHandles.textContent = totalHandles.toLocaleString();
            if(resProfiles) resProfiles.textContent = Math.round(profileMeters).toLocaleString() + " meters";
            if(resWeight) resWeight.innerHTML = `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="mr-1"><path d="M12 19V5M5 12l7-7 7 7"/></svg> ${weightSavingsKg} kg lighter`;
        }
        
        function renderProductGrid"""
if "function toggleDarkMode" not in content:
    content = content.replace("function renderProductGrid", js_helpers)

with open("index.html", "w") as f:
    f.write(content)

print("Dark Mode and Calculator injected successfully.")
