import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Add OS auto-detect script in the <head>
head_script = """
    <script>
        // Auto-detect OS Dark Mode preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
        }
    </script>
</head>"""

if "prefers-color-scheme" not in content:
    content = content.replace("</head>", head_script)

# 2. Add icon synchronization on page load
sync_script = """
        // Sync dark mode icons on load
        document.addEventListener('DOMContentLoaded', () => {
            const isDark = document.documentElement.classList.contains('dark');
            const moon = document.getElementById('moon-icon');
            const sun = document.getElementById('sun-icon');
            if (moon) moon.classList.toggle('hidden', isDark);
            if (sun) sun.classList.toggle('hidden', !isDark);
            
            const mobText = document.getElementById('mobile-dark-text');
            if (mobText) mobText.textContent = isDark ? 'Light Mode' : 'Dark Mode';
        });

        function toggleDarkMode() {"""

if "Sync dark mode icons on load" not in content:
    content = content.replace("function toggleDarkMode() {", sync_script)

with open("index.html", "w") as f:
    f.write(content)

print("Auto dark mode configured.")
