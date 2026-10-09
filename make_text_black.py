with open("index.html", "r") as f:
    content = f.read()

# Replace bronze/gold classes with black/gray classes for text readability
content = content.replace('text-[#b45309] hover:underline font-bold', 'text-brand-black underline hover:text-brand-gray font-bold')
content = content.replace('text-[#b45309] hover:underline', 'text-brand-black underline hover:text-brand-gray')
content = content.replace('hover:text-[#b45309]', 'hover:text-brand-gray')
content = content.replace('group-hover:text-[#b45309]', 'group-hover:text-brand-gray')

# Mobile contact
content = content.replace('text-[#b45309]">Contact Us', 'text-brand-black font-bold">Contact Us')

# Print legal doc
content = content.replace('text-[#b45309] hover:text-brand-black', 'text-brand-black hover:text-brand-gray')

# Mobile calculator
content = content.replace('text-[#9a6a12] flex items-center justify-between', 'text-brand-black flex items-center justify-between font-bold')

# Desktop calculator
content = content.replace('text-[#d4af37] hover:text-brand-black', 'text-brand-black font-bold hover:text-brand-gray')

# Interactive studio label
content = content.replace('text-[#9a6a12] mb-3 flex items-center gap-2', 'text-brand-black mb-3 flex items-center gap-2')

# The stars! Make sure they stay gold. They are currently text-[#b45309].
# Let's change them to the bright gold:
content = content.replace('gap-1 text-[#b45309]', 'gap-1 text-[#d4af37]')

with open("index.html", "w") as f:
    f.write(content)

print("Text colors converted to black.")
