import re

with open("blog_full_final.txt", "r", encoding="utf-8-sig") as f:
    text = f.read()

paragraphs = text.split("\n")
html_parts = []
for p in paragraphs:
    p = p.strip()
    if not p:
        continue
    
    if p.startswith("Meta Title:") or p.startswith("Meta Description:"):
        continue
    elif p.startswith("Why We Choose Aluminium Handles Over Steel"):
        continue
    
    # H2 Matchers
    elif p.startswith("Reasons for choosing") or \
         p.startswith("Aluminium vs Steel Handles: A Simple Comparison") or \
         p.startswith("Aluminium vs Steel Handles: Which One Is Better") or \
         p.startswith("Aluminium vs Steel: Understanding the Basic") or \
         p.startswith("Aluminium vs Steel Handle: Other Important Factors") or \
         p.startswith("Conclusion:"):
        html_parts.append(f"<h2 class=\"text-2xl font-bold mt-10 mb-4 text-brand-black\">{p.replace('*', '').strip()}</h2>")
        
    # H3 Matchers (number lists like 1., 2. )
    elif re.match(r"^\d+\.", p):
        html_parts.append(f"<h3 class=\"text-xl font-bold mt-8 mb-3 text-brand-black\">{p.replace('*', '').strip()}</h3>")
        
    else:
        p = p.replace("\n", " ")
        p = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", p)
        html_parts.append(f"<p class=\"mb-4\">{p}</p>")

html_content = "\n                    ".join(html_parts)
with open("blog_full_final_html.txt", "w") as f:
    f.write(html_content)
