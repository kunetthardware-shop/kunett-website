import re

with open("index.html", "r") as f:
    content = f.read()

# Fix the duplicate closure that is causing a fatal syntax error
bad_closure = """                    btn.disabled = false;
                });
                });

            } else if (page === 'home') {"""

good_closure = """                    btn.disabled = false;
                });

            } else if (page === 'home') {"""

content = content.replace(bad_closure, good_closure)

with open("index.html", "w") as f:
    f.write(content)

print("Syntax error fixed.")
