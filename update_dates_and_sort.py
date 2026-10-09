import re

with open("index.html", "r") as f:
    content = f.read()

# Fix "Sept" to "Sep" for JavaScript Date compatibility
content = content.replace("date: '28 Sept',", "date: '28 Sep 2026',")
content = content.replace("date: '15 Sept',", "date: '15 Sep 2026',")
content = content.replace("date: '5 Oct',", "date: '5 Oct 2026',")
content = content.replace("date: 'October 5, 2026',", "date: '5 Oct 2026',")
content = content.replace("date: '15 Sept',", "date: '15 Sep 2026',")

# Update the rendering logic to sort the blogs by date before displaying
target_render = "blogs.forEach(blog => {"
replacement_render = """
                let sortedBlogs = [...blogs].sort((a, b) => new Date(b.date) - new Date(a.date));
                sortedBlogs.forEach(blog => {"""

if target_render in content and replacement_render not in content:
    content = content.replace(target_render, replacement_render)

with open("index.html", "w") as f:
    f.write(content)

print("Dates standardized and sorting logic injected.")
