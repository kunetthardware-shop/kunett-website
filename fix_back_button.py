import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update the navigate function signature and add history API
old_nav_def = r"function navigate\(page, productId = null\) \{"
new_nav_def = """function navigate(page, productId = null, isPopState = false) {
            
            if (!isPopState) {
                let url = `#${page}`;
                if (productId) url += `?id=${productId}`;
                window.history.pushState({ page, productId }, "", url);
            }
"""
content = re.sub(old_nav_def, new_nav_def, content)


# 2. Update the initialization logic at the bottom of the script
old_init = r"// Initialize Home Page\s*navigate\('home'\);"
new_init = """// Initialize App State (Mobile Back Button Support)
        window.addEventListener('popstate', (e) => {
            if (e.state && e.state.page) {
                navigate(e.state.page, e.state.productId, true);
            } else {
                navigate('home', null, true);
            }
        });

        // Initialize Home Page based on URL or default
        if (window.location.hash) {
            let hash = window.location.hash.replace('#', '').split('?');
            let page = hash[0];
            let pid = hash.length > 1 ? hash[1].replace('id=', '') : null;
            navigate(page, pid, true);
        } else {
            navigate('home');
        }"""
content = re.sub(old_init, new_init, content)

with open("index.html", "w") as f:
    f.write(content)

print("Back button logic added.")
