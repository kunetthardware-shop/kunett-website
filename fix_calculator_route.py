with open("index.html", "r") as f:
    content = f.read()

target = "if (page === 'legal') {"
replacement = """if (page === 'calculator') {
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

if "if (page === 'calculator')" not in content:
    content = content.replace(target, replacement)

with open("index.html", "w") as f:
    f.write(content)

print("Calculator route injected successfully.")
