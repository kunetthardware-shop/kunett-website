import re

with open("index.html", "r") as f:
    content = f.read()

founder_html = """<!-- Founder Section -->
                    <section class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-t border-brand-lightgray">
                        <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center gap-12">
                            <div class="w-full md:w-1/2 flex justify-center">
                                <div class="relative w-64 h-64 md:w-80 md:h-80 rounded-full overflow-hidden border-8 border-white shadow-xl">
                                    <img src="assets/sanjay_patel.jpg" alt="Sanjay Patel, Founder of KUNETT" class="w-full h-full object-cover" loading="lazy">
                                </div>
                            </div>
                            <div class="w-full md:w-1/2 text-center md:text-left">
                                <p class="text-[10px] md:text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">A Message from our Founder</p>
                                <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-6">Sanjay Patel</h3>
                                <p class="text-brand-gray text-sm md:text-base leading-relaxed mb-6 italic">
                                    "For over 10 years, my vision has been to elevate Indian manufacturing to the global stage. At Harikrushna Enterprise, we don't just manufacture hardware—we engineer precision. Every single handle that leaves our Rajkot factory carries our promise of aerospace-grade quality, flawless aesthetic finishing, and lifelong endurance. Thank you to the 100+ wholesale partners worldwide who place their trust in us every single day."
                                </p>
                                <p class="text-xs font-bold text-brand-black uppercase tracking-widest">— Founder & CEO, Harikrushna Enterprise</p>
                            </div>
                        </div>
                    </section>

                    <!-- SEO Optimized Content Block -->"""

content = content.replace("<!-- SEO Optimized Content Block -->", founder_html)

with open("index.html", "w") as f:
    f.write(content)

print("Founder section added.")
