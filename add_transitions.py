import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update <main> tag to include transition classes
main_tag_pattern = r'<main id="main-content" class="(.*?)">'
if 'transition-all' not in content:
    content = re.sub(main_tag_pattern, r'<main id="main-content" class="\1 transition-all duration-300 opacity-100 transform translate-y-0">', content)

# 2. Modify navigate() start
nav_start_pattern = r'window\.scrollTo\(0, 0\);\s*if \(page === \'calculator\'\) \{'

nav_start_replacement = """const mainContent = document.getElementById('main-content');
            mainContent.style.opacity = '0';
            mainContent.style.transform = 'translateY(10px)';
            
            setTimeout(() => {
                window.scrollTo(0, 0);

            if (page === 'calculator') {"""

content = re.sub(nav_start_pattern, nav_start_replacement, content)

# 3. Modify navigate() end
nav_end_pattern = r'\}\s*// Initialize App State'

nav_end_replacement = """}
                
                setTimeout(() => {
                    mainContent.style.opacity = '1';
                    mainContent.style.transform = 'translateY(0)';
                }, 50);
                
            }, 250); // wait for fade out
        }

        // Initialize App State"""

content = re.sub(nav_end_pattern, nav_end_replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Transitions added.")
