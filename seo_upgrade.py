import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Inject JSON-LD Schema into <head>
schema_code = """
    <!-- SEO: JSON-LD Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Harikrushna Enterprise",
      "alternateName": "KUNETT Hardware",
      "image": "https://kunett.in/assets/logo.png",
      "description": "Premier manufacturer and supplier of luxury architectural aluminium hardware, cabinet handles, and profiles.",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Rajkot",
        "addressRegion": "Gujarat",
        "addressCountry": "IN"
      },
      "telephone": "+91 99246 37640",
      "email": "kunetthardware@gmail.com",
      "url": "https://kunett.in"
    }
    </script>
</head>"""
content = content.replace("</head>", schema_code)

# 2. Upgrade Product Grid Image Alt-Text
# Look for: alt="Model ${p.code}"
rich_alt_grid = 'alt="KUNETT Premium Aluminium Architectural Hardware - Model ${p.code} Manufacturer Rajkot"'
content = content.replace('alt="Model ${p.code}"', rich_alt_grid)

# 3. Upgrade PDP Image Alt-Text
# Look for: alt="Model ${product.code}"
rich_alt_pdp = 'alt="High-Resolution View of KUNETT Aluminium Profile Model ${product.code} - Luxury Furniture Hardware"'
content = content.replace('alt="Model ${product.code}"', rich_alt_pdp)

with open("index.html", "w") as f:
    f.write(content)

print("Schema and Alt-Text injected.")
