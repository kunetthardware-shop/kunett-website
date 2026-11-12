import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Inject the renderProductSlider function
slider_js = """        function renderProductSlider(productArray) {
            if (productArray.length === 0) return '<p class="text-brand-gray text-center py-10">No products found.</p>';
            let html = '<div class="flex overflow-x-auto snap-x snap-mandatory gap-4 md:gap-6 pb-6 no-scrollbar -mx-4 px-4 md:mx-0 md:px-0">';
            productArray.forEach(p => {
                html += `
                    <div class="flex-none w-[65%] sm:w-[45%] md:w-[30%] lg:w-[22%] snap-start group cursor-pointer" onclick='navigate("product", "${p.code}")'>
                        <div class="bg-brand-offwhite rounded-xl aspect-[4/3] flex items-center justify-center p-6 mb-4 overflow-hidden relative border border-brand-lightgray/50 group-hover:border-brand-gray transition-colors">
                            <img src="${p.image}" alt="KUNETT Model ${p.code}" class="product-img w-full h-full object-contain mix-blend-multiply" loading="lazy">
                        </div>
                        <div>
                            <p class="text-[10px] font-bold text-brand-gray tracking-widest uppercase mb-1">${p.category}</p>
                            <h3 class="font-serif text-lg md:text-xl font-bold text-brand-black mb-2">Model ${p.code}</h3>
                            <div class="flex flex-wrap gap-1.5">
                                ${p.finishes.slice(0, 4).map(f => `<div class="w-3.5 h-3.5 rounded-full shadow-sm border border-brand-lightgray" style="${getColorStyle(f)}" title="${f}"></div>`).join('')}
                                ${p.finishes.length > 4 ? `<span class="text-[10px] text-brand-gray ml-1 font-medium">+${p.finishes.length - 4}</span>` : ''}
                            </div>
                        </div>
                    </div>
                `;
            });
            html += '</div>';
            return html;
        }
        
        function renderProductGrid(productArray) {"""

content = content.replace("        function renderProductGrid(productArray) {", slider_js)

# 2. Update New Arrivals
new_arrivals_pattern = r'<!-- New Arrivals -->[\s\S]*?renderProductGrid\(\['
new_arrivals_replacement = lambda m: m.group(0).replace('renderProductGrid([', 'renderProductSlider([')
content = re.sub(new_arrivals_pattern, new_arrivals_replacement, content)

# 3. Update Architectural Profiles
profiles_pattern = r'<!-- Profiles -->[\s\S]*?renderProductGrid\(\['
profiles_replacement = lambda m: m.group(0).replace('renderProductGrid([', 'renderProductSlider([')
content = re.sub(profiles_pattern, profiles_replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Slider injected and applied.")
