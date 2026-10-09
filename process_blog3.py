import re

with open("blog3.txt", "r", encoding="utf-8-sig") as f:
    text = f.read()

paragraphs = text.split("\n")
html_parts = []
for p in paragraphs:
    p = p.strip()
    if not p:
        continue
    
    if p.startswith("Meta Title:") or p.startswith("Meta Description:") or p.startswith("URL Slug:") or p.startswith("Primary Keyword:") or p.startswith("Secondary Keywords:") or p.startswith("Suggested Article Category:") or p.startswith("Suggested Featured Image ALT Text:") or p.startswith("aluminium profile handle") or p.startswith("aluminium furniture handles") or p.startswith("modular furniture handles") or p.startswith("aluminium cabinet handles") or p.startswith("aluminium wardrobe profile") or p.startswith("modern furniture hardware") or p.startswith("profile handles for furniture") or p.startswith("modern aluminium handles"):
        continue
        
    if "Modern aluminium profile handle for modular furniture by KUNETT Hardware" in p or "Discover how aluminium profile handles can improve the look" in p or "Aluminium Profile Handles: A Modern Solution for Modular Furniture | KUNETT" in p or "aluminium-profile-handles-modern-modular-furniture" in p:
        continue
        
    if p.startswith("H1:"):
        continue
    
    if p.startswith("H2:"):
        html_parts.append(f"<h2 class=\"text-2xl font-bold mt-10 mb-4 text-brand-black\">{p.replace('H2:', '').strip()}</h2>")
    elif p.startswith("H3:"):
        html_parts.append(f"<h3 class=\"text-xl font-bold mt-8 mb-3 text-brand-black\">{p.replace('H3:', '').strip()}</h3>")
    else:
        p = p.replace("\n", " ")
        p = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", p)
        html_parts.append(f"<p class=\"mb-4\">{p}</p>")

html_content = "\n                    ".join(html_parts)

# Add internal linking as requested at the bottom
html_content += """
                    <div class="bg-brand-lightgray/20 p-6 rounded-xl border border-brand-lightgray my-8">
                        <h4 class="font-bold text-brand-black mb-2">📚 Related Reading</h4>
                        <p class="text-sm text-brand-gray mb-1">Choosing handles for your doors? Read our guide on <a href="#" onclick="navigate('blog-post', 'aluminium-vs-steel-handles-for-new-home'); return false;" class="text-[#f59e0b] hover:underline font-bold">Aluminium vs Steel Handles</a>.</p>
                        <p class="text-sm text-brand-gray">Want to upgrade your bedroom? See <a href="#" onclick="navigate('blog-post', 'how-to-choose-aluminium-handle-for-wardrobe'); return false;" class="text-[#f59e0b] hover:underline font-bold">How to Choose the Right Aluminium Handle for Your Wardrobe</a>.</p>
                    </div>
                    <p class="mt-8">Explore our <strong><a href="#" onclick="navigate('300')" class="text-[#f59e0b] hover:underline">Aluminium Profile Handles Collection</a></strong> to find the perfect modern hardware for your modular furniture.</p>
                    <p class="mt-10 pt-6 border-t border-brand-lightgray text-sm font-bold text-brand-gray uppercase tracking-widest">Written by Rishabh Virani</p>"""

full_blog_obj = f"""{{
                slug: 'aluminium-profile-handles-modern-modular-furniture',
                title: 'Aluminium Profile Handles: A Modern Solution for Modular Furniture',
                date: '28 Sept',
                author: 'Rishabh Virani',
                excerpt: 'Discover how aluminium profile handles can improve the look and functionality of modular furniture. Learn about their benefits, finishes and applications.',
                content: `
                    {html_content}
                `,
                image: 'assets/blog_wardrobe.jpg'
            }},"""

with open("index.html", "r") as f:
    content = f.read()

# Insert right after `const blogs = [`
new_content = content.replace("const blogs = [", f"const blogs = [\n{full_blog_obj}")

with open("index.html", "w") as f:
    f.write(new_content)

print("Blog 3 added successfully.")
