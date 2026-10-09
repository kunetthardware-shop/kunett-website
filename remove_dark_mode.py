import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Remove the auto-detect script in head
auto_detect_pattern = r"<script>\s*if \(localStorage\.theme === 'dark'.*?</script>"
content = re.sub(auto_detect_pattern, "", content, flags=re.DOTALL)

# 2. Remove desktop dark mode toggle button
desktop_btn_pattern = r'<button onclick="toggleDarkMode\(\)".*?</button>'
content = re.sub(desktop_btn_pattern, "", content, flags=re.DOTALL)

# 3. Remove mobile dark mode toggle button
mobile_btn_pattern = r'<button onclick="toggleDarkMode\(\); closeMobileMenu\(\)".*?</button>'
content = re.sub(mobile_btn_pattern, "", content, flags=re.DOTALL)

# 4. Remove toggleDarkMode function
toggle_func_pattern = r'function toggleDarkMode\(\) \{.*?\n        \}'
content = re.sub(toggle_func_pattern, "", content, flags=re.DOTALL)

# 5. Remove html.dark CSS rules (Optional, but let's try to strip it out to clean up)
css_pattern = r'html\.dark .*?\}'
content = re.sub(css_pattern, "", content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Dark mode removed successfully.")
