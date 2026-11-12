import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update the openCatalogueModal function to accept optional overrides
old_modal_func = """        function openCatalogueModal(e) {
            if (e) e.preventDefault();
            catalogueModal.classList.add('catalogue-active');
            document.body.style.overflow = 'hidden';
        }"""
new_modal_func = """        function openCatalogueModal(e, title = "Get the Catalogue", subtitle = "Please enter your details to instantly download our full architectural catalogue.") {
            if (e) e.preventDefault();
            const titleEl = document.getElementById('cat-modal-title');
            const subEl = document.getElementById('cat-modal-sub');
            if (titleEl) titleEl.innerText = title;
            if (subEl) subEl.innerText = subtitle;
            
            catalogueModal.classList.add('catalogue-active');
            document.body.style.overflow = 'hidden';
        }"""
content = content.replace(old_modal_func, new_modal_func)

# 2. Add IDs to the modal title/subtitle so we can change them
old_modal_html = """                <h3 class="font-serif text-2xl md:text-3xl text-brand-black mb-2">Get the Catalogue</h3>
                <p class="text-sm text-brand-gray">Please enter your details to instantly download our full architectural catalogue.</p>"""
new_modal_html = """                <h3 id="cat-modal-title" class="font-serif text-2xl md:text-3xl text-brand-black mb-2">Get the Catalogue</h3>
                <p id="cat-modal-sub" class="text-sm text-brand-gray">Please enter your details to instantly download our full architectural catalogue.</p>"""
content = content.replace(old_modal_html, new_modal_html)

# 3. Inject the trigger inside the navigate() function
nav_pattern = r'const activeLink = document\.getElementById\(\'nav-\' \+ page\);\s*if \(activeLink\) activeLink\.classList\.add\(\'active\', \'border-b-2\', \'border-brand-black\'\);'
nav_replacement = """const activeLink = document.getElementById('nav-' + page);
            if (activeLink) activeLink.classList.add('active', 'border-b-2', 'border-brand-black');
            
            // --- Interstitial Lead Capture Trigger ---
            const productCategories = ['200', '300', '400', '450', '500'];
            if (productCategories.includes(page) && !sessionStorage.getItem('leadCaptured')) {
                sessionStorage.setItem('leadCaptured', 'true'); // Only ask once per session
                setTimeout(() => {
                    openCatalogueModal(null, "Unlock Full Pricing", "Enter your details to view our complete architectural range and get wholesale pricing.");
                }, 800); // Slight delay so the page loads behind it first
            }"""
content = re.sub(nav_pattern, nav_replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Interstitial lead capture added.")
