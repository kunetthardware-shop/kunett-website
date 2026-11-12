import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r'(<h4 class="font-bold text-lg mb-3">Packaged & Delivered</h4>[\s\S]*?</section>)\s*<section class="py-16 md:py-24 px-4 md:px-6 max-w-7xl mx-auto">[\s\S]*?</section>\s*`;\s*\} else if \(page === \'product\'\)'

detailed_sections = """\\1
                    
                    <section class="py-16 md:py-24 px-4 md:px-6 max-w-7xl mx-auto">
                        <!-- Step 1 Details -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24 items-center mb-24">
                            <div class="bg-brand-lightgray/30 aspect-[4/3] rounded-2xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
                                <img src="assets/process_aluminium.jpg" alt="Extrusion and Die Design of Aerospace-Grade Aluminium" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
                            </div>
                            <div>
                                <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">1</div>
                                <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-6">Extrusion & Die Engineering</h3>
                                <p class="text-brand-gray leading-relaxed mb-6">The manufacturing cycle begins with raw, aerospace-grade solid aluminium. Before any cutting happens, custom extrusion dies are engineered to match the exact architectural specifications of our cabinet handles and profiles.</p>
                                <p class="text-brand-gray leading-relaxed">The raw aluminium is heated and pushed through these precision dies—forming the foundational, continuous profile. This highly technical step ensures that every KUNETT handle possesses immense structural integrity and ergonomic weight, completely eliminating the hollow, fragile feel found in cheap zinc-alloy alternatives.</p>
                            </div>
                        </div>
                        
                        <!-- Step 2 Details -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24 items-center mb-24 md:flex-row-reverse">
                            <div class="order-1 md:order-2 bg-brand-pink/30 aspect-[4/3] rounded-2xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
                                <img src="assets/process_vmc.jpg" alt="VMC Machining and Blade Cutting" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
                            </div>
                            <div class="order-2 md:order-1">
                                <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">2</div>
                                <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-6">Blade Cutting & VMC Machining</h3>
                                <p class="text-brand-gray leading-relaxed mb-6">Once the continuous architectural profiles are successfully extruded, they are moved to our precision cutting stations. High-speed, automated blades slice the solid aluminium into the exact lengths required for wardrobes, kitchens, and cabinets.</p>
                                <p class="text-brand-gray leading-relaxed">The cut pieces are then securely mounted into our state-of-the-art 5-Axis Vertical Machining Centers (VMC). These computer-controlled machines meticulously carve out the ergonomic curves, mounting holes, and fine detailing with microscopic accuracy. This guarantees that every hardware piece perfectly aligns with your modular furniture.</p>
                            </div>
                        </div>

                        <!-- Step 3 Details -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24 items-center mb-24">
                            <div class="bg-brand-offwhite aspect-[4/3] rounded-2xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
                                <img src="assets/306.png" alt="Buffing and Electrochemical Anodizing" class="w-[70%] h-[70%] object-contain mix-blend-multiply hover:scale-105 transition-transform duration-700">
                            </div>
                            <div>
                                <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">3</div>
                                <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-6">Buffing & Electrochemical Anodizing</h3>
                                <p class="text-brand-gray leading-relaxed mb-6">A precision cut is nothing without a flawless surface. Every milled handle undergoes a rigorous, multi-stage hand-buffing process to remove microscopic manufacturing imperfections and create a perfectly smooth, luxurious texture.</p>
                                <p class="text-brand-gray leading-relaxed">Next, the hardware enters our advanced electrochemical anodizing baths. Unlike cheap spray paint, anodizing physically alters the surface layer of the aluminium, locking in our premium signature colors—such as Rose Gold, Matte Black, and Antique. This process creates an incredibly hardened, corrosion-resistant surface that will never fade, peel, or rust.</p>
                            </div>
                        </div>

                        <!-- Step 4 Details -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24 items-center md:flex-row-reverse">
                            <div class="order-1 md:order-2 bg-brand-offwhite aspect-[4/3] rounded-2xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
                                <img src="assets/206.png" alt="Packaged and Delivered Wholesale" class="w-[70%] h-[70%] object-contain mix-blend-multiply hover:scale-105 transition-transform duration-700">
                            </div>
                            <div class="order-2 md:order-1">
                                <div class="w-12 h-12 bg-[#25D366] text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">4</div>
                                <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-6">Quality Inspection & Delivery</h3>
                                <p class="text-brand-gray leading-relaxed mb-6">The final stage of the KUNETT manufacturing cycle is uncompromising quality control. Each cabinet handle and architectural profile is individually inspected under harsh lighting for color consistency, structural perfection, and flawless finishing.</p>
                                <p class="text-brand-gray leading-relaxed">Once approved, the hardware is securely wrapped and packaged in high-grade wholesale cartons to prevent any transit damage. Whether you are a B2B wholesaler, a factory owner, or an interior designer outfitting a luxury home, your hardware is dispatched immediately and delivered directly to your door, ready for installation.</p>
                            </div>
                        </div>
                    </section>
                `;
            } else if (page === 'product')"""

content = re.sub(pattern, detailed_sections, content)

with open("index.html", "w") as f:
    f.write(content)

print("Detailed paragraphs added to process page.")
