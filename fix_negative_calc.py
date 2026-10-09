with open("index.html", "r") as f:
    content = f.read()

# 1. Update HTML inputs to have min="0" and oninput to block negative signs
input_k_old = '<input type="number" id="calc-kitchens" value="5" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">'
input_k_new = '<input type="number" min="0" id="calc-kitchens" value="5" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">'

input_w_old = '<input type="number" id="calc-wardrobes" value="10" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">'
input_w_new = '<input type="number" min="0" id="calc-wardrobes" value="10" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">'

input_d_old = '<input type="number" id="calc-drawers" value="8" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="calculateROI()">'
input_d_new = '<input type="number" min="0" id="calc-drawers" value="8" class="w-full bg-brand-offwhite border border-brand-lightgray rounded-xl px-4 py-3 text-brand-black focus:outline-none focus:border-brand-black transition-colors" oninput="this.value = Math.abs(this.value); calculateROI()">'

content = content.replace(input_k_old, input_k_new)
content = content.replace(input_w_old, input_w_new)
content = content.replace(input_d_old, input_d_new)

# 2. Update JS calculation logic
js_old = """        function calculateROI() {
            const kitchens = parseInt(document.getElementById('calc-kitchens')?.value || 0);
            const wardrobes = parseInt(document.getElementById('calc-wardrobes')?.value || 0);
            const drawers = parseInt(document.getElementById('calc-drawers')?.value || 0);"""

js_new = """        function calculateROI() {
            const kitchens = Math.max(0, parseInt(document.getElementById('calc-kitchens')?.value || 0));
            const wardrobes = Math.max(0, parseInt(document.getElementById('calc-wardrobes')?.value || 0));
            const drawers = Math.max(0, parseInt(document.getElementById('calc-drawers')?.value || 0));"""

content = content.replace(js_old, js_new)

with open("index.html", "w") as f:
    f.write(content)

print("Negative calculator bug fixed.")
