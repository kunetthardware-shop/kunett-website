import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Clean up the garbage at the end
bad_end = """        }
                
                setTimeout(() => {
                    mainContent.style.opacity = '1';
                    mainContent.style.transform = 'translateY(0)';
                }, 50);
                
            }, 250); // wait for fade out
        }

        // Initialize App State"""
        
good_end = """        }

        // Initialize App State"""

content = content.replace(bad_end, good_end)

# 2. Fix the navigate closure
bad_nav_closure = """                    </section>
                `;
            }
        }

        let currentProduct = null;"""

good_nav_closure = """                    </section>
                `;
            }
            
            // Fade back in after DOM is updated
            setTimeout(() => {
                mainContent.style.opacity = '1';
                mainContent.style.transform = 'translateY(0)';
            }, 50);
            
        }, 250); // wait for fade out
    }

        let currentProduct = null;"""

content = content.replace(bad_nav_closure, good_nav_closure)

with open("index.html", "w") as f:
    f.write(content)

print("Fixed syntax errors.")
