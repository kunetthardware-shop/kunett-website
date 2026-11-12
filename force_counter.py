import re

with open("index.html", "r") as f:
    content = f.read()

# Fix HTML
content = re.sub(
    r'<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">10\+</span>',
    '<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2"><span class="count-up" data-target="10">0</span>+</span>',
    content
)

content = re.sub(
    r'<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2">100\+</span>',
    '<span class="text-4xl md:text-5xl font-serif text-brand-black mb-2"><span class="count-up" data-target="100">0</span>+</span>',
    content
)

# Inject JS Function
js_function = """        function initCounters() {
            const counters = document.querySelectorAll('.count-up');
            const observer = new IntersectionObserver((entries, obs) => {
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
                        obs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            
            counters.forEach(counter => {
                counter.innerText = '0';
                observer.observe(counter);
            });
        }

        function renderOptions() {"""

content = re.sub(r'        function renderOptions\(\) \{', js_function, content)

with open("index.html", "w") as f:
    f.write(content)

print("Forced counter fixes.")
