with open("index.html", "r") as f:
    content = f.read()

# Add an internal and external link to Blog 1 (Rishabh's Wardrobe Blog)
target1 = '<h2 class="text-2xl font-bold mt-10 mb-4 text-brand-black">Final Thoughts</h2>'
replacement1 = """
                    <div class="bg-brand-lightgray/20 p-6 rounded-xl border border-brand-lightgray my-8">
                        <h4 class="font-bold text-brand-black mb-2">📚 Related Reading</h4>
                        <p class="text-sm text-brand-gray mb-1">Still deciding between materials? Read our comprehensive comparison on <a href="#" onclick="navigate('blog-post', 'aluminium-vs-steel-handles-for-new-home'); return false;" class="text-[#f59e0b] hover:underline font-bold">Why We Choose Aluminium Over Steel Handles</a>.</p>
                        <p class="text-sm text-brand-gray">Want to learn more about the science of anodization? Check out this <a href="https://en.wikipedia.org/wiki/Anodizing" target="_blank" rel="noopener noreferrer" class="text-[#f59e0b] hover:underline font-bold">detailed guide on Aluminium Anodization</a>.</p>
                    </div>
                    """ + target1

content = content.replace(target1, replacement1)


# Add an internal and external link to Blog 2 (Ronak's Aluminium vs Steel Blog)
target2 = '<h2 class="text-2xl font-bold mt-10 mb-4 text-brand-black">Conclusion</h2>'
replacement2 = """
                    <div class="bg-brand-lightgray/20 p-6 rounded-xl border border-brand-lightgray my-8">
                        <h4 class="font-bold text-brand-black mb-2">📚 Related Reading</h4>
                        <p class="text-sm text-brand-gray mb-1">Looking for specific styling tips? Read our guide on <a href="#" onclick="navigate('blog-post', 'how-to-choose-aluminium-handle-for-wardrobe'); return false;" class="text-[#f59e0b] hover:underline font-bold">How to Choose the Right Aluminium Handle for Your Wardrobe</a>.</p>
                        <p class="text-sm text-brand-gray">Read more about modern architectural trends at <a href="https://www.architecturaldigest.com/" target="_blank" rel="noopener noreferrer" class="text-[#f59e0b] hover:underline font-bold">Architectural Digest</a>.</p>
                    </div>
                    """ + target2

content = content.replace(target2, replacement2)

with open("index.html", "w") as f:
    f.write(content)

print("Internal and External SEO links added successfully.")
