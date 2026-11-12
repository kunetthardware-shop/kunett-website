import re

with open("index.html", "r") as f:
    content = f.read()

# Replace the broken preloader logic
bad_logic = r"// Preloader Logic\s*window\.addEventListener\('load', function\(\) \{.*?\n        \}\);"

good_logic = """// Preloader Logic (Failsafe)
        function hidePreloader() {
            const preloader = document.getElementById('preloader');
            if (preloader && preloader.style.display !== 'none') {
                preloader.style.opacity = '0';
                setTimeout(() => {
                    preloader.style.display = 'none';
                }, 700);
            }
        }
        
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(hidePreloader, 800);
        });
        
        // Absolute failsafe: Hide after 2 seconds no matter what
        setTimeout(hidePreloader, 2000);"""

content = re.sub(bad_logic, good_logic, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Preloader logic fixed.")
