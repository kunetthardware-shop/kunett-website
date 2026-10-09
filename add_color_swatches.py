import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Inject the getColorStyle helper function
color_function = """
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

content = content.replace("function renderProductGrid", color_function)

# 2. Update the Grid rendering (look for Finishes: text)
# In current code: <p class="text-sm text-brand-gray mb-4">Finishes: ${p.finishes.join(', ')}</p>
grid_find = "<p class=\"text-sm text-brand-gray mb-4\">Finishes: ${p.finishes.join(', ')}</p>"
grid_replace = """<div class="flex items-center gap-3 mb-4">
                                        <span class="text-xs font-bold uppercase tracking-widest text-brand-gray">Finishes:</span>
                                        <div class="flex gap-1.5">
                                            ${p.finishes.map(f => `<div class="w-4 h-4 rounded-full border border-gray-300 shadow-sm" style="${getColorStyle(f)}" title="${f}"></div>`).join('')}
                                        </div>
                                    </div>"""

if grid_find in content:
    content = content.replace(grid_find, grid_replace)

# 3. Update the PDP rendering
# In current code: <li><strong>Finishes:</strong> ${product.finishes.join(', ')}</li>
pdp_find = "<li><strong>Finishes:</strong> ${product.finishes.join(', ')}</li>"
pdp_replace = """<li class="flex items-center gap-4 mt-6">
                                        <strong>Finishes:</strong> 
                                        <div class="flex gap-3">
                                            ${product.finishes.map(f => `
                                                <div class="flex items-center gap-2 bg-white px-3 py-1.5 rounded-full border border-brand-lightgray shadow-sm">
                                                    <div class="w-4 h-4 rounded-full border border-gray-300" style="${getColorStyle(f)}"></div>
                                                    <span class="text-sm text-brand-black font-medium">${f}</span>
                                                </div>
                                            `).join('')}
                                        </div>
                                    </li>"""

if pdp_find in content:
    content = content.replace(pdp_find, pdp_replace)

with open("index.html", "w") as f:
    f.write(content)

print("Color swatches injected.")
