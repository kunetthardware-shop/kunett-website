import re

with open("index.html", "r") as f:
    content = f.read()

new_blog = """
            {
                slug: 'aluminium-vs-steel-handles-for-new-home',
                title: 'Why We Choose Aluminium Handles Over Steel Handles for a New Home',
                date: 'October 5, 2026',
                author: 'RISHABH VIRANI',
                excerpt: 'Discover why aluminium handles are better than steel for a lightweight design, durability, modern look, easy maintenance, and versatility.',
                content: `
                    <p class="mb-4">When selecting aluminium handles for our new home decoration with doors, windows, cabinets, furniture, and other uses, the handle material matters more than you might think. A quality handle not only looks good but also needs to be sturdy, comfortable, and durable enough to be used for extended periods of time. Two metals that are commonly used include aluminium and steel, among others.</p>
                    <p class="mb-4">Another reason we prefer aluminium is the design and finishing freedom it offers. It can be shaped into different profiles and finished in different styles to match the look of modern furniture. With proper surface treatment, aluminium can also resist everyday wear and corrosion.</p>
                    <p class="mb-4">Steel has its own strengths and can be an excellent material for many applications. However, when you want a handle that feels light, looks modern, and offers design flexibility, aluminium becomes a natural choice. Ultimately, the right material depends on the application, quality, and finish—but for modern furniture, aluminium offers a combination that is hard to ignore.</p>

                    <h2 class="text-2xl font-bold mt-10 mb-4 text-brand-black">Reasons for choosing Aluminium Handles over Steel Handles</h2>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">1. Lightweight</h3>
                    <p class="mb-4">One of the greatest strengths of aluminium is that it is lightweight. An aluminium handle is lighter than an iron handle, which makes it easier to fit in new houses. The great thing about aluminium is that it is not only light but also durable enough.</p>
                    <p class="mb-4">This makes it perfect for doors, windows, cabinets, furniture, and other hardware.</p>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">2. Better Resistance to Corrosion</h3>
                    <p class="mb-4">Handles can be exposed to moisture and humidity and the changing environment. The rusting process will occur on steel when its protective coating gets damaged and when it gets exposed to moisture for a prolonged period.</p>
                    <p class="mb-4">The surface of aluminium forms a natural oxide coating which acts as a protective measure against corrosion. Aluminium handles can be made more resistant to the environment through an appropriate finishing method like anodising and powder coating.</p>
                    <p class="mb-4">Thus, aluminium can be considered a good choice for such places.</p>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">3. Modern and Attractive Appearance</h3>
                    <p class="mb-4">The appearance of a handle can make a noticeable difference to the overall look of a product. Aluminium provides a clean, modern appearance, which can be finished in all types of colours, designs, and surface treatments.</p>
                    <p class="mb-4">From raw material to finish colours like black, silver, rose gold, gold or other custom colours, aluminium provides manufacturers with new modern design possibilities. This flexibility allows aluminium handles to complement both traditional and contemporary designs.</p>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">4. Easy to Manufacture and Customise</h3>
                    <p class="mb-4">This metal is quite easy to process and can be moulded into any shape depending on the need. Different handle shapes can thus be manufactured based on their size, profile, shape, and finish.</p>
                    <p class="mb-4">For manufacturers and companies, this feature is very important as handles can be designed according to the requirements of the product rather than following standard designs.</p>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">5. Easier Handling and Installation</h3>
                    <p class="mb-4">Due to the light nature of aluminium handles, it is easy to carry them around, position them, and fix them in place. It becomes especially helpful when a lot of handles are involved in building and manufacturing processes. Being lighter helps to lower the weight of the final product.</p>

                    <h3 class="text-xl font-bold mt-8 mb-3 text-brand-black">6. Good Strength-to-Weight Ratio</h3>
                    <p class="mb-4">One of the myths is that aluminium gives up on strength. Although steel is generally stronger in most of its basic mechanical properties than aluminium, strength is not the only characteristic that matters when making a decision about which handle to choose.</p>
                    <p class="mb-4">The aluminium metal offers a reasonable strength-to-weight ratio and can provide adequate strength for various furniture, architectural, and hardware applications at low weight of the finished item. Of course, it depends on the alloy, shape, dimensions, wall thickness, process, and usage of the handle.</p>
                    <p class="mb-4">Therefore, a properly designed aluminium handle can offer the required performance at low weight. This is especially valuable for furniture and architectural hardware.</p>

                    <h2 class="text-2xl font-bold mt-10 mb-4 text-brand-black">Understanding the Basic Difference</h2>
                    <p class="mb-4">Both aluminium and steel are strong and useful engineering materials, yet their characteristics are rather dissimilar. First of all, the difference lies in weight. Aluminium has the density of 2.7 g/cm³, whereas that of steel equals 7.8–8.0 g/cm³. In simple words, a certain aluminium part weighs about one third of the same steel part.</p>
                    <p class="mb-4">This makes aluminium the perfect choice in case weight reduction is important. Steel, on the other hand, usually offers greater strength and stiffness. This material is a good choice for those situations when the handles are likely to carry large loads, to receive heavy impact or be used in harsh working conditions.</p>

                    <h2 class="text-2xl font-bold mt-10 mb-4 text-brand-black">Conclusion</h2>
                    <p class="mb-4">It may not seem a big thing when selecting handles for your future house construction, but it really matters how comfortable you will be when using the furniture. Aluminium handles have the benefits of being <strong>lightweight, anti-corrosive, durable, modern-looking, and easy to shape into different designs</strong> that make them great for many parts of a house.</p>
                    <p class="mb-4">When compared to steel handles, those made from aluminium are easier because they are lighter and resistant to rusting, thus suitable to be used in rooms like kitchens, bathrooms, wardrobes, and windows that tend to be moist and humid. Moreover, aluminium handles are available in many forms, so you may choose those that fit your modern furniture and room designs.</p>

                    <p class="mt-8">Explore our <strong><a href="#" onclick="navigate('200')" class="text-[#f59e0b] hover:underline">Cabinet Handles Collection</a></strong> to find the perfect modern aluminium hardware for your next project.</p>
                    <p class="mt-10 pt-6 border-t border-brand-lightgray text-sm font-bold text-brand-gray uppercase tracking-widest">Written by RISHABH VIRANI</p>
                `,
                image: 'assets/blog_kitchen.jpg'
            },
"""

new_content = content.replace("const blogs = [", f"const blogs = [\n{new_blog}")

with open("index.html", "w") as f:
    f.write(new_content)

print("Blog 2 successfully injected.")
