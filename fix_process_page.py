import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern for the top of the 'process' page
pattern = r"""(<div class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-b border-brand-lightgray">
                        <div class="max-w-4xl mx-auto text-center">
                            <p class="text-xs font-bold uppercase tracking-widest text-brand-gray mb-4">Harikrushna Enterprise</p>
                            <h1 class="font-serif text-4xl md:text-6xl text-brand-black mb-6 leading-tight">Precision Manufacturing in Rajkot</h1>
                            <p class="text-brand-gray text-base md:text-xl leading-relaxed max-w-2xl mx-auto">Discover the engineering, materials, and craftsmanship behind every KUNETT handle.</p>
                        </div>
                    </div>)"""

# Add the 4-step cycle right after it
cycle_section = """\\1
                    
                    <!-- 4-Step Cycle -->
                    <section class="py-16 md:py-24 px-4 md:px-6 max-w-7xl mx-auto border-b border-brand-lightgray">
                        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 md:gap-6 relative">
                            <!-- Connecting Line (Desktop Only) -->
                            <div class="hidden md:block absolute top-8 left-[10%] right-[10%] h-px bg-brand-lightgray -z-10"></div>
                            
                            <!-- Step 1 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative z-10">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    1
                                </div>
                                <h4 class="font-bold text-lg mb-3">Extrusion & Die Design</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Raw aerospace-grade aluminium is precisely extruded through custom dies to form the foundational architectural profile.</p>
                            </div>
                            
                            <!-- Step 2 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative z-10">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    2
                                </div>
                                <h4 class="font-bold text-lg mb-3">VMC Machining</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">The aluminium is precision-cut by automated blades and transferred to our VMC centers for flawless shaping and detailing.</p>
                            </div>
                            
                            <!-- Step 3 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative z-10">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    3
                                </div>
                                <h4 class="font-bold text-lg mb-3">Buffing & Anodizing</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Each handle undergoes rigorous buffing, followed by electrochemical anodizing to lock in premium luxury colors.</p>
                            </div>
                            
                            <!-- Step 4 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative z-10">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm group-hover:bg-[#25D366] group-hover:text-white group-hover:border-[#25D366] transition-colors duration-300">
                                    4
                                </div>
                                <h4 class="font-bold text-lg mb-3">Packaged & Delivered</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">The finished hardware is meticulously inspected, securely packaged for wholesale, and delivered directly to your home or project.</p>
                            </div>
                        </div>
                    </section>"""

content = re.sub(pattern, cycle_section, content)

with open("index.html", "w") as f:
    f.write(content)

print("Process page updated with 4-step cycle.")
