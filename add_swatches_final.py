import re

with open("index.html", "r") as f:
    content = f.read()

# Make sure getColorStyle is there. If not, add it before renderProductGrid
color_func = """
        function getColorStyle(color) {
            const map = {
                'Black': 'background-color: #1a1a1a;',
                'Rose Gold': 'background: linear-gradient(135deg, #b76e79 0%, #e0bfb8 100%);',
                'Matte Gold': 'background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 100%);',
                'Gold': 'background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);',
                'Silver': 'background: linear-gradient(135deg, #C0C0C0 0%, #E8E8E8 100%);',
                'Champagne': 'background: linear-gradient(135deg, #F7E7CE 0%, #FFE4C4 100%);'
            };
            return map[color] || 'background-color: #cccccc;';
        }

        function renderProductGrid"""

if "function getColorStyle" not in content:
    content = content.replace("function renderProductGrid", color_func)

# 1. Update Product Grid to show swatches
# We look for: <p class="text-[10px] md:text-sm text-brand-gray">${p.category}</p>
grid_target = """<p class="text-[10px] md:text-sm text-brand-gray">${p.category}</p>"""
grid_replace = """<p class="text-[10px] md:text-sm text-brand-gray mb-2">${p.category}</p>
                            <div class="flex gap-1.5 mt-auto">
                                ${p.finishes.map(f => `<div class="w-3.5 h-3.5 rounded-full shadow-sm border border-gray-300" style="${getColorStyle(f)}" title="${f}"></div>`).join('')}
                            </div>"""

if grid_target in content:
    content = content.replace(grid_target, grid_replace)

# 2. Update the PDP Finishes Buttons
# Look for:
# btn.className = `${baseClasses} ${stateClasses}`;
# btn.textContent = f;
pdp_target = """btn.className = `${baseClasses} ${stateClasses}`;
                btn.textContent = f;"""
pdp_replace = """btn.className = `${baseClasses} ${stateClasses} flex items-center gap-2`;
                btn.innerHTML = `<div class="w-3.5 h-3.5 rounded-full shadow-sm border border-white/50" style="${getColorStyle(f)}"></div> <span>${f}</span>`;"""

if pdp_target in content:
    content = content.replace(pdp_target, pdp_replace)

with open("index.html", "w") as f:
    f.write(content)

print("Swatches added securely.")
