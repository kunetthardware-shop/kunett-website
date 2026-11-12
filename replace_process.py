import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r'<!-- How to Inquire Section -->[\s\S]*?<!-- Founder / Brand Story -->'

replacement = """<!-- Manufacturing Process Section -->
                    <section class="py-16 md:py-24 px-4 md:px-6 max-w-7xl mx-auto border-t border-brand-lightgray mt-10 md:mt-16">
                        <div class="text-center mb-12 md:mb-16">
                            <p class="text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">How It's Made</p>
                            <h3 class="font-serif text-3xl md:text-5xl text-brand-black mb-4">The KUNETT Manufacturing Cycle</h3>
                            <p class="text-brand-gray text-sm md:text-base max-w-2xl mx-auto">From raw aerospace-grade aluminium to a luxury cabinet handle. See how we engineer premium architectural hardware at our Rajkot facility.</p>
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 md:gap-6 relative">
                            <!-- Connecting Line (Desktop Only) -->
                            <div class="hidden md:block absolute top-8 left-[10%] right-[10%] h-px bg-brand-lightgray -z-10"></div>
                            
                            <!-- Step 1 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm z-10 group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    1
                                </div>
                                <h4 class="font-bold text-lg mb-3">Extrusion & Die Design</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Raw aerospace-grade aluminium is precisely extruded through custom dies to form the foundational architectural profile.</p>
                            </div>
                            
                            <!-- Step 2 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm z-10 group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    2
                                </div>
                                <h4 class="font-bold text-lg mb-3">VMC Machining</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">The aluminium is precision-cut by automated blades and transferred to our VMC centers for flawless shaping and detailing.</p>
                            </div>
                            
                            <!-- Step 3 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm z-10 group-hover:bg-brand-black group-hover:text-white transition-colors duration-300">
                                    3
                                </div>
                                <h4 class="font-bold text-lg mb-3">Buffing & Anodizing</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Each handle undergoes rigorous buffing, followed by electrochemical anodizing to lock in premium luxury colors.</p>
                            </div>
                            
                            <!-- Step 4 -->
                            <div class="flex flex-col items-center text-center group bg-white p-6 rounded-2xl border border-brand-lightgray hover:border-brand-black transition-colors shadow-sm relative">
                                <div class="w-16 h-16 bg-brand-offwhite border border-brand-lightgray text-brand-black rounded-full flex justify-center items-center font-serif text-2xl mb-6 shadow-sm z-10 group-hover:bg-[#25D366] group-hover:text-white group-hover:border-[#25D366] transition-colors duration-300">
                                    4
                                </div>
                                <h4 class="font-bold text-lg mb-3">Packaged & Delivered</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">The finished hardware is meticulously inspected, securely packaged for wholesale, and delivered directly to your home or project.</p>
                            </div>
                        </div>
                    </section>

                    <!-- Founder / Brand Story -->"""

content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Process section replaced.")
