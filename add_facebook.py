import re

with open("index.html", "r") as f:
    content = f.read()

# Pattern to insert Facebook after Google Business Profile
pattern = r'<li><a href="https://share\.google/ph0nAicuxlc4C8bdU".*?Google Business Profile ↗</a></li>'

replacement = """<li><a href="https://share.google/ph0nAicuxlc4C8bdU" target="_blank" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Google Business Profile ↗</a></li>
                    <li><a href="https://www.facebook.com/profile.php?id=61594388126613" target="_blank" class="hover:text-[#1877F2] transition-colors flex items-center gap-2"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg> Facebook Profile ↗</a></li>"""

content = re.sub(pattern, replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Facebook link added.")
