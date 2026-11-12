import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Add Preloader HTML right after body tag
body_pattern = r'(<body class="[^"]*">)'
preloader_html = """\\1
    <!-- Premium Preloader -->
    <div id="preloader" class="fixed inset-0 z-[9999] bg-white flex justify-center items-center transition-opacity duration-700">
        <div class="flex flex-col items-center gap-4">
            <img src="assets/logo.png" alt="KUNETT Hardware" class="h-16 md:h-24 animate-pulse object-contain">
            <div class="w-48 h-1 bg-brand-lightgray rounded-full overflow-hidden">
                <div class="h-full bg-brand-black rounded-full animate-[loading_1.5s_ease-in-out_infinite]"></div>
            </div>
        </div>
    </div>
"""
if 'id="preloader"' not in content:
    content = re.sub(body_pattern, preloader_html, content)

# 2. Add loading animation keyframes to the style block
style_pattern = r'(<style>)'
keyframes = """\\1
        @keyframes loading {
            0% { width: 0%; transform: translateX(-100%); }
            50% { width: 100%; transform: translateX(0); }
            100% { width: 0%; transform: translateX(200%); }
        }
"""
if '@keyframes loading' not in content:
    content = re.sub(style_pattern, keyframes, content)

# 3. Add JavaScript to hide the preloader on load
script_pattern = r'(// Initialize Home Page\s*navigate\(\'home\'\);)'
js_code = """\\1

        // Preloader Logic
        window.addEventListener('load', function() {
            const preloader = document.getElementById('preloader');
            if (preloader) {
                // Keep it visible for 1.2 seconds for a premium feel
                setTimeout(() => {
                    preloader.style.opacity = '0';
                    setTimeout(() => {
                        preloader.style.display = 'none';
                    }, 700); // Wait for transition
                }, 1200);
            }
        });"""

if '// Preloader Logic' not in content:
    content = re.sub(script_pattern, js_code, content)

with open("index.html", "w") as f:
    f.write(content)

print("Preloader added successfully.")
