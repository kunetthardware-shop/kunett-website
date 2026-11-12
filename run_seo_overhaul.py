import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update Title Tag
old_title = r'<title>KUNETT \| Your new home decorator</title>'
new_title = '<title>Aluminium Handles & Profiles Manufacturer in Rajkot | KUNETT Hardware</title>'
content = re.sub(old_title, new_title, content)

# 2. Update Meta Description
old_desc = r'<meta name="description" content="KUNETT by Harikrushna Enterprise\. Your new home decorator\. Premium architectural aluminium hardware, cabinet handles, profiles, and knobs engineered for modern spaces\.">'
new_desc = '<meta name="description" content="Harikrushna Enterprise (KUNETT) is Rajkot\'s premier manufacturer & global exporter of architectural aluminium handles, wardrobe profiles, counsil handles, and knobs. Supplying wholesale to India, USA & Germany.">'
content = re.sub(old_desc, new_desc, content)

# 3. Update Meta Keywords
old_keywords = r'<meta name="keywords" content="premium aluminium handles, cabinet handles, cabinet profiles, counsil handles, sliding counsils, cabinet knobs, wardrobe handles, modular kitchen hardware, architectural hardware, KUNETT hardware, Harikrushna Enterprise, Rajkot hardware manufacturer, luxury home decorator, custom hardware India">'
new_keywords = '<meta name="keywords" content="aluminium handles manufacturer, aluminium profile handles, cabinet handles manufacturer Rajkot, wardrobe profile handles, aluminium hardware manufacturer India, counsil handles, sliding counsil, cabinet knobs, architectural hardware exporter, modular kitchen aluminium handles, Harikrushna Enterprise, KUNETT hardware, Sanjay Patel Rajkot">'
content = re.sub(old_keywords, new_keywords, content)

# 4. Update OG & Twitter Meta
content = re.sub(
    r'<meta property="og:title" content="KUNETT \| Your new home decorator">',
    '<meta property="og:title" content="Aluminium Handles & Profiles Manufacturer in Rajkot | KUNETT Hardware">',
    content
)
content = re.sub(
    r'<meta property="og:description" content="Premium architectural aluminium hardware, cabinet handles, profiles, and knobs engineered for modern spaces\.">',
    '<meta property="og:description" content="Harikrushna Enterprise (KUNETT) manufactures premium solid aluminium cabinet handles, wardrobe profiles, and architectural hardware in Rajkot, Gujarat. Global exporter.">',
    content
)
content = re.sub(
    r'<meta name="twitter:title" content="KUNETT \| Premium Aluminium Hardware">',
    '<meta name="twitter:title" content="Aluminium Handles & Profiles Manufacturer | KUNETT Hardware">',
    content
)
content = re.sub(
    r'<meta name="twitter:description" content="Architectural cabinet handles, profiles, and knobs engineered for modern spaces\.">',
    '<meta name="twitter:description" content="Premier architectural aluminium handles, wardrobe profiles, and cabinet knobs manufacturer in Rajkot, Gujarat. Global export to USA and Germany.">',
    content
)

# 5. Upgrade JSON-LD Schema
old_json_ld = r'    <!-- SEO: JSON-LD Structured Data -->\s*<script type="application/ld\+json">[\s\S]*?</script>'
new_json_ld = """    <!-- SEO: JSON-LD Structured Data with FAQ and Catalog -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": ["LocalBusiness", "Manufacturer"],
          "@id": "https://kunetthardware.com/#organization",
          "name": "Harikrushna Enterprise",
          "alternateName": "KUNETT Hardware",
          "image": "https://kunetthardware.com/assets/logo.png",
          "logo": "https://kunetthardware.com/assets/logo.png",
          "description": "Premier manufacturer and global exporter of luxury architectural aluminium handles, wardrobe profiles, counsil handles, and cabinet knobs.",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Rajkot",
            "addressLocality": "Rajkot",
            "addressRegion": "Gujarat",
            "postalCode": "360002",
            "addressCountry": "IN"
          },
          "telephone": "+91 99246 37640",
          "email": "support@kunetthardware.com",
          "url": "https://kunetthardware.com",
          "sameAs": [
            "https://www.facebook.com/profile.php?id=61594388126613",
            "https://www.instagram.com/harikrushna.enterprise/",
            "https://share.google/ph0nAicuxlc4C8bdU"
          ],
          "founder": {
            "@type": "Person",
            "name": "Sanjay Patel"
          },
          "areaServed": ["India", "United States", "Germany", "United Kingdom", "Worldwide"],
          "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "KUNETT Architectural Aluminium Hardware",
            "itemListElement": [
              { "@type": "OfferCatalog", "name": "Aluminium Cabinet Handles (200 Series)" },
              { "@type": "OfferCatalog", "name": "Aluminium Cabinet Profiles (300 Series)" },
              { "@type": "OfferCatalog", "name": "Aluminium Counsil Handles (400 Series)" },
              { "@type": "OfferCatalog", "name": "Aluminium Sliding Counsil Handles (450 Series)" },
              { "@type": "OfferCatalog", "name": "Aluminium Cabinet Knobs (500 Series)" }
            ]
          }
        },
        {
          "@type": "FAQPage",
          "@id": "https://kunetthardware.com/#faq",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "Who is the leading aluminium handle manufacturer in Rajkot?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Harikrushna Enterprise under the brand KUNETT Hardware is a premier manufacturer and exporter of solid architectural aluminium cabinet handles, wardrobe profiles, and knobs based in Rajkot, Gujarat, India with over 10 years of manufacturing excellence."
              }
            },
            {
              "@type": "Question",
              "name": "What finishes are available for KUNETT aluminium handles and profiles?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "KUNETT aluminium handles are available in Matte Black, Rose Gold (R Gold), Matte Gold, Champagne, SS Matt (Stainless Steel Finish), Antique Brass, CP (Chrome Plated), and Architectural Grey."
              }
            },
            {
              "@type": "Question",
              "name": "Does KUNETT Hardware export aluminium handles globally to USA and Germany?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes, KUNETT Hardware exports architectural aluminium hardware worldwide, with key export markets including the United States, Germany, the UK, Europe, and Middle Eastern countries."
              }
            },
            {
              "@type": "Question",
              "name": "What aluminium grade is used for manufacturing KUNETT handles?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "KUNETT hardware is manufactured using 100% solid aerospace-grade virgin aluminium alloy, precision-extruded through custom dies and finished with advanced electrochemical anodizing for scratch and corrosion resistance."
              }
            }
          ]
        }
      ]
    }
    </script>"""
content = re.sub(old_json_ld, new_json_ld, content)

# 6. Update Hero H1 in navigate('home')
old_h1 = r'<h1 class="font-serif text-4xl md:text-7xl lg:text-8xl text-brand-black drop-shadow-sm mb-4 md:mb-6 leading-tight capitalize">Your new home<br>decorator\.</h1>'
new_h1 = """<h1 class="font-serif text-3xl sm:text-5xl md:text-6xl lg:text-7xl text-brand-black drop-shadow-sm mb-4 md:mb-6 leading-tight capitalize">
                                Aluminium Handles &amp; Profiles Manufacturer
                                <span class="text-base sm:text-xl md:text-2xl font-sans font-medium text-brand-black/80 block mt-3">
                                    KUNETT Architectural Hardware &bull; Your New Home Decorator &bull; Rajkot, India
                                </span>
                            </h1>"""
content = re.sub(old_h1, new_h1, content)

# 7. Add FAQ section right before the Bottom CTA
faq_section = """
                    <!-- Frequently Asked Questions (SEO Keyword Rich) -->
                    <section class="py-16 md:py-24 px-4 md:px-6 max-w-5xl mx-auto border-t border-brand-lightgray">
                        <div class="text-center mb-12">
                            <p class="text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Wholesale &amp; Technical Inquiries</p>
                            <h3 class="font-serif text-3xl md:text-4xl text-brand-black mb-4">Frequently Asked Questions</h3>
                            <p class="text-brand-gray text-sm md:text-base max-w-xl mx-auto">Everything you need to know about sourcing architectural aluminium hardware directly from our Rajkot manufacturing facility.</p>
                        </div>
                        <div class="space-y-4">
                            <div class="border border-brand-lightgray rounded-xl p-6 bg-brand-offwhite">
                                <h4 class="font-bold text-base md:text-lg text-brand-black mb-2">Who is the manufacturer behind KUNETT Hardware?</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">KUNETT is the flagship architectural hardware brand of <strong>Harikrushna Enterprise</strong>, founded by Sanjay Patel in Rajkot, Gujarat. With over 10 years of manufacturing experience, we operate advanced extrusion, cutting, and VMC CNC machining facilities supplying over 100+ wholesale partners across India and exporting globally.</p>
                            </div>
                            <div class="border border-brand-lightgray rounded-xl p-6 bg-brand-offwhite">
                                <h4 class="font-bold text-base md:text-lg text-brand-black mb-2">What finishes and colors are available for aluminium handles?</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Our aluminium handles and profiles are available in Matte Black, Rose Gold (R Gold), Matte Gold, SS Matt (Stainless Steel finish), Champagne, CP (Chrome Plated), Antique Brass, and Architectural Grey. All finishes undergo multi-stage buffing and electrochemical anodization to prevent oxidation and fading.</p>
                            </div>
                            <div class="border border-brand-lightgray rounded-xl p-6 bg-brand-offwhite">
                                <h4 class="font-bold text-base md:text-lg text-brand-black mb-2">Do you export aluminium handles to the United States and Germany?</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">Yes! A substantial volume of our manufacturing is exported to international markets including the United States, Germany, the UK, Europe, and the UAE. We provide secure international export packaging, custom profile cut lengths, and wholesale freight coordination.</p>
                            </div>
                            <div class="border border-brand-lightgray rounded-xl p-6 bg-brand-offwhite">
                                <h4 class="font-bold text-base md:text-lg text-brand-black mb-2">Why choose solid aluminium hardware over zinc or steel?</h4>
                                <p class="text-sm text-brand-gray leading-relaxed">100% solid aerospace-grade aluminium will never rust, warp, or crack. It delivers substantial weight savings for sliding wardrobe doors and kitchen cabinets while offering sharp architectural lines and superior anodized finishes that outlast electroplated zinc hardware.</p>
                            </div>
                        </div>
                    </section>

                    <!-- Bottom Call to Action -->"""

content = re.sub(r'(\s*<!-- Bottom Call to Action -->)', faq_section, content)

with open("index.html", "w") as f:
    f.write(content)

print("SEO overhaul successfully applied!")
