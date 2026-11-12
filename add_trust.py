import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern to replace
pattern = r'<h2 class="font-serif text-2xl md:text-4xl text-brand-black max-w-4xl mx-auto leading-snug">\s*KUNETT is your new home decorator\. We engineer the premium hardware you reach for every single day\.\s*</h2>'

# New block with Trust Stats
replacement = """<h2 class="font-serif text-2xl md:text-4xl text-brand-black max-w-4xl mx-auto leading-snug mb-12">
                            KUNETT is your new home decorator. We engineer the premium hardware you reach for every single day.
                        </h2>
                        
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-y-10 gap-x-4 max-w-6xl mx-auto pt-4 md:pt-8 border-t border-brand-lightgray/50">
                            <div class="flex flex-col items-center">
                                <span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">10+</span>
                                <span class="text-[10px] md:text-xs font-bold uppercase tracking-widest text-brand-gray">Years in Market</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">100+</span>
                                <span class="text-[10px] md:text-xs font-bold uppercase tracking-widest text-brand-gray">Wholesale Partners</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">Global</span>
                                <span class="text-[10px] md:text-xs font-bold uppercase tracking-widest text-brand-gray">Export Network</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">100%</span>
                                <span class="text-[10px] md:text-xs font-bold uppercase tracking-widest text-brand-gray">Solid Aluminium</span>
                            </div>
                        </div>"""

content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Trust section added.")
