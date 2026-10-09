with open("index.html", "r") as f:
    content = f.read()

# Fix the amber text globally (f59e0b -> b45309)
content = content.replace('text-[#f59e0b]', 'text-[#b45309]')
content = content.replace('hover:text-[#f59e0b]', 'hover:text-[#b45309]')
content = content.replace('group-hover:text-[#f59e0b]', 'group-hover:text-[#b45309]')

# Fix the specific d4af37 text that is on light backgrounds
content = content.replace('text-[#d4af37] flex items-center gap-1.5', 'text-[#9a6a12] flex items-center gap-1.5') # Desktop calc nav
content = content.replace('text-[#d4af37] flex items-center justify-between', 'text-[#9a6a12] flex items-center justify-between') # Mobile calc nav
content = content.replace('text-[#d4af37] mb-3 flex items-center gap-2', 'text-[#9a6a12] mb-3 flex items-center gap-2') # Interactive configurator text

with open("index.html", "w") as f:
    f.write(content)

print("Yellow text contrast fixed.")
