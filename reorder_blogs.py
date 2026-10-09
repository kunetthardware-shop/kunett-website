import re

with open("index.html", "r") as f:
    content = f.read()

# Standardize Blog 1 date
content = content.replace("October 5, 2026", "5 Oct")

# We will just write a dynamic JavaScript sorter in the renderBlog() function!
# Let's find where blogs are rendered.
# The rendering is usually something like:
# const grid = document.getElementById('blog-grid');
# grid.innerHTML = blogs.map(blog => ...).join('');

# We can replace `blogs.map` with a sorted version, or we can just sort the `blogs` array directly right after it's declared, or right before rendering.
# It's better to sort right before rendering.
# Let's check how blogs are rendered in `index.html`.
