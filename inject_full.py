import re

with open("blog2_html.txt", "r") as f:
    html_content = f.read()

# Append CTA
html_content += """
                    <p class="mt-8">Explore our <strong><a href="#" onclick="navigate('200')" class="text-[#f59e0b] hover:underline">Cabinet Handles Collection</a></strong> to find the perfect modern aluminium hardware for your next project.</p>
                    <p class="mt-10 pt-6 border-t border-brand-lightgray text-sm font-bold text-brand-gray uppercase tracking-widest">Written by Ronak Vekariya</p>"""

full_blog_obj = f"""{{
                slug: 'aluminium-vs-steel-handles-for-new-home',
                title: 'Why We Choose Aluminium Handles Over Steel Handles for a New Home',
                date: '15 Sept',
                author: 'Ronak Vekariya',
                excerpt: 'Discover why aluminium handles are better than steel for a lightweight design, durability, modern look, easy maintenance, and versatility.',
                content: `
                    {html_content}
                `,
                image: 'assets/blog_kitchen.jpg'
            }}"""

with open("index.html", "r") as f:
    content = f.read()

# Replace the old one. We'll use a regex that matches from { slug: 'aluminium-vs-steel-handles-for-new-home' up to the matching },
pattern = r"\{\s*slug:\s*'aluminium-vs-steel-handles-for-new-home'.*?image:\s*'assets/blog_kitchen\.jpg'\s*\}"
content = re.sub(pattern, full_blog_obj, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Full blog replaced successfully.")
