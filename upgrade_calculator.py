import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Replace the Calculator HTML block
calc_html_pattern = r"if \(page === 'calculator'\) \{.*?\} else if \(page === 'legal'\) \{"

new_calc_html = """if (page === 'calculator') {
                let html = `
                    <div class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-b border-brand-lightgray">
                        <div class="max-w-4xl mx-auto text-center">
                            <h1 class="font-serif text-4xl md:text-5xl text-brand-black mb-6 leading-tight">B2B Project Calculator</h1>
                            <p class="text-brand-gray text-base md:text-xl leading-relaxed max-w-2xl mx-auto">Instantly estimate total hardware requirements across your entire architectural project.</p>
                        </div>
                    </div>
                    <section class="py-12 md:py-20 px-4 md:px-6 max-w-5xl mx-auto min-h-[50vh]">
                        <div class="bg-white border border-brand-lightgray rounded-3xl p-8 md:p-12 shadow-sm">
                            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                                <div>
                                    <h3 class="font-serif text-2xl font-bold mb-6 text-brand-black">Project Scope</h3>
                                    <div class="space-y-6">
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Number of Modular Kitchens</label>
                                            <input type="number" min="0" id="calc-kitchens" value="2" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Number of Wardrobes</label>
                                            <input type="number" min="0" id="calc-wardrobes" value="4" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Other Rooms (Bedrooms, Living)</label>
                                            <input type="number" min="0" id="calc-rooms" value="3" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">
                                        </div>
                                    </div>
                                    <p class="text-xs text-brand-gray mt-6 italic">* Estimates assume standard luxury modular layouts.</p>
                                </div>
                                <div class="bg-[#111111] text-white p-8 rounded-2xl flex flex-col justify-center border border-[#333333]">
                                    <h3 class="font-serif text-2xl font-bold mb-8 text-brand-offwhite">Estimated Hardware</h3>
                                    
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-4 mb-6">
                                        <div>
                                            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-1">Cabinet Handles</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-handles">0</p>
                                        </div>
                                        <div>
                                            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-1">Aluminium Profiles</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-profiles">0 m</p>
                                        </div>
                                        <div>
                                            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-1">Counsil Handles</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-counsil">0</p>
                                        </div>
                                        <div>
                                            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-1">Sliding Counsils</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-sliding">0</p>
                                        </div>
                                        <div>
                                            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-1">Cabinet Knobs</p>
                                            <p class="text-2xl font-serif text-[#d4af37]" id="res-knobs">0</p>
                                        </div>
                                    </div>

                                    <div class="pt-6 border-t border-[#333333]">
                                        <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Weight Savings vs Steel</p>
                                        <p class="text-2xl font-serif text-[#25D366] flex items-center gap-2" id="res-weight">
                                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
                                            0 kg lighter
                                        </p>
                                        <p class="text-[10px] text-gray-500 mt-2">Aluminium puts significantly less stress on hinges, increasing furniture lifespan.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `;
                mainContent.innerHTML = html;
                setTimeout(calculateROI, 100);
            } else if (page === 'legal') {"""

content = re.sub(calc_html_pattern, new_calc_html, content, flags=re.DOTALL)

# 2. Replace the calculateROI() JS function
js_pattern = r'function calculateROI\(\) \{.*?\}\s*function renderProductGrid'

new_js = """function calculateROI() {
            const kitchens = Math.max(0, parseInt(document.getElementById('calc-kitchens')?.value || 0));
            const wardrobes = Math.max(0, parseInt(document.getElementById('calc-wardrobes')?.value || 0));
            const rooms = Math.max(0, parseInt(document.getElementById('calc-rooms')?.value || 0));
            
            // Estimates per unit
            const kitchenHandles = kitchens * 12;
            const kitchenProfiles = kitchens * 15; // meters
            const kitchenCounsil = kitchens * 4;
            
            const wardrobeHandles = wardrobes * 4;
            const wardrobeProfiles = wardrobes * 5; // meters
            const wardrobeSliding = wardrobes * 2;
            const wardrobeCounsil = wardrobes * 4;
            
            const roomHandles = rooms * 4;
            const roomKnobs = rooms * 6;
            
            // Totals
            const totalHandles = kitchenHandles + wardrobeHandles + roomHandles;
            const totalProfiles = kitchenProfiles + wardrobeProfiles;
            const totalCounsil = kitchenCounsil + wardrobeCounsil;
            const totalSliding = wardrobeSliding;
            const totalKnobs = roomKnobs;
            
            const totalItems = totalHandles + totalCounsil + totalSliding + totalKnobs;
            const weightSavings = (totalItems * 0.17) + (totalProfiles * 0.5); // kg
            
            const resHandles = document.getElementById('res-handles');
            const resProfiles = document.getElementById('res-profiles');
            const resCounsil = document.getElementById('res-counsil');
            const resSliding = document.getElementById('res-sliding');
            const resKnobs = document.getElementById('res-knobs');
            const resWeight = document.getElementById('res-weight');
            
            if(resHandles) resHandles.textContent = totalHandles.toLocaleString();
            if(resProfiles) resProfiles.textContent = Math.round(totalProfiles).toLocaleString() + " m";
            if(resCounsil) resCounsil.textContent = totalCounsil.toLocaleString();
            if(resSliding) resSliding.textContent = totalSliding.toLocaleString();
            if(resKnobs) resKnobs.textContent = totalKnobs.toLocaleString();
            if(resWeight) resWeight.innerHTML = `<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" class="mr-1"><path d="M12 19V5M5 12l7-7 7 7"/></svg> ${weightSavings.toFixed(1)} kg lighter`;
        }
        
        function renderProductGrid"""

content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Advanced Calculator with all hardware categories integrated.")
