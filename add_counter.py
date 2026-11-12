import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update HTML structure for the numbers
html_pattern = r'<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">10\+</span>'
html_repl1 = '<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2"><span class="count-up" data-target="10">0</span>+</span>'
content = content.replace(html_pattern, html_repl1)

html_pattern2 = r'<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">100\+</span>'
html_repl2 = '<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2"><span class="count-up" data-target="100">0</span>+</span>'
content = content.replace(html_pattern2, html_repl2)

# 2. Add the initCounters() function
js_function = """        function initCounters() {
            const counters = document.querySelectorAll('.count-up');
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = +entry.target.getAttribute('data-target');
                        let count = 0;
                        const duration = 2000;
                        const increment = target / (duration / 16);
                        
                        const updateCount = () => {
                            count += increment;
                            if (count < target) {
                                entry.target.innerText = Math.ceil(count);
                                requestAnimationFrame(updateCount);
                            } else {
                                entry.target.innerText = target;
                            }
                        };
                        updateCount();
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            
            counters.forEach(counter => {
                counter.innerText = '0';
                observer.observe(counter);
            });
        }

        function renderOptions() {"""

content = content.replace("        function renderOptions() {", js_function)

# 3. Call initCounters() at the end of the page === 'home' block
# Find where the home block ends.
# It ends right before `else if (page === 'calculator')` or similar. Let's find exactly what comes after `if (page === 'home')`
