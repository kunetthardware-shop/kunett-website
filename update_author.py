with open("index.html", "r") as f:
    content = f.read()

# Update the author field
content = content.replace("author: 'KUNETT Hardware',", "author: 'RISHABH VIRANI',")

# Append the name to the bottom of the content string
target_string = "<p class=\"mb-4\">If you're looking for modern aluminium handles for wardrobes, cabinets or other furniture, explore the <a href=\"#\" onclick=\"navigate('home')\" class=\"text-[#f59e0b] hover:underline font-bold\">KUNETT Hardware collection</a> and choose a design that fits your furniture's style and purpose.</p>"
replacement_string = target_string + "\n                    <p class=\"mt-10 pt-6 border-t border-brand-lightgray text-sm font-bold text-brand-gray uppercase tracking-widest\">Written by RISHABH VIRANI</p>"

content = content.replace(target_string, replacement_string)

with open("index.html", "w") as f:
    f.write(content)

print("Author updated successfully.")
