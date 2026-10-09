import re

with open("index.html", "r") as f:
    content = f.read()

# 1. ADD THE JS FUNCTION
studio_js = """
        function changeStudioColor(color) {
            const img = document.getElementById('studio-handle-img');
            if(!img) return;
            
            let filterStr = "grayscale(1) brightness(1.2)"; // default silver
            
            if(color === 'Black') {
                filterStr = "grayscale(1) brightness(0.25) contrast(1.5)";
            } else if (color === 'Rose Gold') {
                filterStr = "sepia(0.8) hue-rotate(-30deg) saturate(1.8) brightness(1.0) contrast(1.2)";
            } else if (color === 'Matte Gold') {
                filterStr = "sepia(1) hue-rotate(10deg) saturate(2.5) brightness(1.1) contrast(1.1)";
            } else if (color === 'Champagne') {
                filterStr = "sepia(0.4) hue-rotate(10deg) saturate(1.5) brightness(1.2)";
            }
            
            img.style.filter = filterStr;
        }
"""
if "function changeStudioColor" not in content:
    content = content.replace("function calculateROI() {", studio_js + "\n        function calculateROI() {")

# 2. ADD THE HTML TO THE HOME PAGE
target_html = """                    <!-- How to Inquire Section -->"""
studio_html = """
                    <!-- Interactive Finish Studio -->
                    <section class="py-16 md:py-24 px-4 md:px-6 bg-brand-offwhite border-t border-brand-lightgray mt-12">
                        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-12 lg:gap-20">
                            <div class="w-full lg:w-1/2 flex flex-col items-start">
                                <p class="text-xs font-bold uppercase tracking-widest text-[#d4af37] mb-3 flex items-center gap-2">
                                    <svg class="w-4 h-4 animate-pulse" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path></svg>
                                    Interactive Configurator
                                </p>
                                <h3 class="font-serif text-4xl md:text-6xl text-brand-black mb-6 leading-tight">The Finish Studio</h3>
                                <p class="text-brand-gray text-base md:text-lg mb-10 leading-relaxed max-w-lg">Instantly visualize our premium architectural finishes. Select a material below to watch the hardware transform in real-time.</p>
                                
                                <div class="flex flex-wrap gap-3" id="studio-buttons">
                                    <button onclick="changeStudioColor('Black')" class="flex items-center gap-2.5 px-5 py-3 border border-brand-lightgray rounded-full bg-white hover:border-brand-black hover:shadow-md transition-all">
                                        <div class="w-5 h-5 rounded-full shadow-sm" style="background-color: #1a1a1a;"></div> <span class="text-sm font-bold text-brand-black">Matte Black</span>
                                    </button>
                                    <button onclick="changeStudioColor('Rose Gold')" class="flex items-center gap-2.5 px-5 py-3 border border-brand-lightgray rounded-full bg-white hover:border-brand-black hover:shadow-md transition-all">
                                        <div class="w-5 h-5 rounded-full shadow-sm" style="background: linear-gradient(135deg, #b76e79 0%, #e0bfb8 100%);"></div> <span class="text-sm font-bold text-brand-black">Rose Gold</span>
                                    </button>
                                    <button onclick="changeStudioColor('Matte Gold')" class="flex items-center gap-2.5 px-5 py-3 border border-brand-lightgray rounded-full bg-white hover:border-brand-black hover:shadow-md transition-all">
                                        <div class="w-5 h-5 rounded-full shadow-sm" style="background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 100%);"></div> <span class="text-sm font-bold text-brand-black">Matte Gold</span>
                                    </button>
                                    <button onclick="changeStudioColor('Champagne')" class="flex items-center gap-2.5 px-5 py-3 border border-brand-lightgray rounded-full bg-white hover:border-brand-black hover:shadow-md transition-all">
                                        <div class="w-5 h-5 rounded-full shadow-sm" style="background: linear-gradient(135deg, #F7E7CE 0%, #FFE4C4 100%);"></div> <span class="text-sm font-bold text-brand-black">Champagne</span>
                                    </button>
                                    <button onclick="changeStudioColor('Silver')" class="flex items-center gap-2.5 px-5 py-3 border border-brand-lightgray rounded-full bg-white hover:border-brand-black hover:shadow-md transition-all">
                                        <div class="w-5 h-5 rounded-full shadow-sm border border-gray-300" style="background: linear-gradient(135deg, #C0C0C0 0%, #E8E8E8 100%);"></div> <span class="text-sm font-bold text-brand-black">Silver</span>
                                    </button>
                                </div>
                            </div>
                            
                            <div class="w-full lg:w-1/2 flex justify-center items-center bg-white rounded-[2.5rem] p-12 shadow-2xl min-h-[400px] border border-brand-lightgray relative overflow-hidden group">
                                <div class="absolute inset-0 bg-gradient-to-tr from-brand-offwhite to-white opacity-50"></div>
                                <img id="studio-handle-img" src="assets/200_1.png" alt="Hardware Finish Visualizer" class="relative z-10 w-full h-[300px] object-contain drop-shadow-2xl transition-all duration-700 ease-in-out group-hover:scale-110" style="filter: sepia(0.8) hue-rotate(-30deg) saturate(1.8) brightness(1.0) contrast(1.2);">
                            </div>
                        </div>
                    </section>

                    <!-- How to Inquire Section -->"""

if "The Finish Studio" not in content:
    content = content.replace(target_html, studio_html)

with open("index.html", "w") as f:
    f.write(content)

print("Interactive Studio added.")
