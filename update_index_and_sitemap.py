#!/usr/bin/env python3
"""
update_index_and_sitemap.py
Updates index.html internal links to point to the dedicated static HTML pages,
and regenerates sitemap.xml to include all 8 pages with full image metadata.
"""

import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Desktop Navbar Tier 1
html = html.replace(
    '<a href="#process" onclick="navigate(\'process\'); return false;" id="nav-process"',
    '<a href="our-process.html" id="nav-process"'
)
html = html.replace(
    '<a href="#contact" onclick="navigate(\'contact\'); return false;" id="nav-contact"',
    '<a href="contact.html" id="nav-contact"'
)

# Desktop Navbar Tier 2
html = html.replace(
    '<a href="#200" onclick="navigate(\'200\'); return false;" id="nav-200"',
    '<a href="aluminium-handles.html" id="nav-200"'
)
html = html.replace(
    '<a href="#300" onclick="navigate(\'300\'); return false;" id="nav-300"',
    '<a href="aluminium-handle-profile.html" id="nav-300"'
)
html = html.replace(
    '<a href="#400" onclick="navigate(\'400\'); return false;" id="nav-400"',
    '<a href="wardrobe-counsil-handles.html" id="nav-400"'
)
html = html.replace(
    '<a href="#450" onclick="navigate(\'450\'); return false;" id="nav-450"',
    '<a href="sliding-wardrobe-handles.html" id="nav-450"'
)
html = html.replace(
    '<a href="#500" onclick="navigate(\'500\'); return false;" id="nav-500"',
    '<a href="cabinet-knobs.html" id="nav-500"'
)

# Mobile Menu Links
html = html.replace(
    '<a href="#process" onclick="closeMobileMenu(); navigate(\'process\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Our Process</a>',
    '<a href="our-process.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Our Process</a>'
)
html = html.replace(
    '<a href="#contact" onclick="closeMobileMenu(); navigate(\'contact\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 text-brand-black font-bold">Contact Us</a>',
    '<a href="contact.html" class="text-left py-3 border-b border-brand-lightgray/50 text-brand-black font-bold">Contact Us</a>'
)
html = html.replace(
    '<a href="#200" onclick="closeMobileMenu(); navigate(\'200\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handles</a>',
    '<a href="aluminium-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handles</a>'
)
html = html.replace(
    '<a href="#300" onclick="closeMobileMenu(); navigate(\'300\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handle Profile</a>',
    '<a href="aluminium-handle-profile.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handle Profile</a>'
)
html = html.replace(
    '<a href="#400" onclick="closeMobileMenu(); navigate(\'400\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Counsil Handles</a>',
    '<a href="wardrobe-counsil-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Counsil Handles</a>'
)
html = html.replace(
    '<a href="#450" onclick="closeMobileMenu(); navigate(\'450\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Sliding Counsils</a>',
    '<a href="sliding-wardrobe-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Sliding Counsils</a>'
)
html = html.replace(
    '<a href="#500" onclick="closeMobileMenu(); navigate(\'500\'); return false;" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Knobs</a>',
    '<a href="cabinet-knobs.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Knobs</a>'
)

# Hero button
html = html.replace(
    '<a href="#200" onclick="navigate(\'200\'); return false;" class="bg-brand-black text-white px-8 md:px-10 py-3.5 md:py-4 font-bold text-xs md:text-sm tracking-wide rounded-full hover:opacity-80 transition-opacity shadow-md">',
    '<a href="aluminium-handles.html" class="bg-brand-black text-white px-8 md:px-10 py-3.5 md:py-4 font-bold text-xs md:text-sm tracking-wide rounded-full hover:opacity-80 transition-opacity shadow-md">'
)

# Homepage Category Grid Cards
html = html.replace(
    '<a href="#200" onclick="navigate(\'200\'); return false;" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">',
    '<a href="aluminium-handles.html" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">'
)
html = html.replace(
    '<a href="#300" onclick="navigate(\'300\'); return false;" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">',
    '<a href="aluminium-handle-profile.html" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">'
)
html = html.replace(
    '<a href="#400" onclick="navigate(\'400\'); return false;" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">',
    '<a href="wardrobe-counsil-handles.html" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">'
)
html = html.replace(
    '<a href="#450" onclick="navigate(\'450\'); return false;" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">',
    '<a href="sliding-wardrobe-handles.html" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">'
)
html = html.replace(
    '<a href="#500" onclick="navigate(\'500\'); return false;" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">',
    '<a href="cabinet-knobs.html" class="group bg-brand-offwhite rounded-2xl p-6 border border-brand-lightgray hover:border-brand-black transition-all hover:shadow-lg flex flex-col justify-between">'
)

# Footer Contact link
html = html.replace(
    '<li><a href="#" onclick="navigate(\'contact\')"',
    '<li><a href="contact.html"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated: index.html with static page links.")

# 2. Generate sitemap.xml
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://kunetthardware.com/</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/201.png</image:loc>
      <image:title>KUNETT Model 201 Aluminium Cabinet Handle</image:title>
      <image:caption>Solid aerospace-grade aluminium handle for modular kitchen drawers and wardrobe shutters</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/301.png</image:loc>
      <image:title>KUNETT Model 301 Aluminium Handle Profile</image:title>
      <image:caption>Edge-mounted architectural aluminium profile handle for seamless modular kitchen cabinets</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/401.png</image:loc>
      <image:title>KUNETT Model 401 Aluminium Counsil Handle</image:title>
      <image:caption>Deep-recess concealed solid aluminium handle for heavy wardrobe doors and architectural pantry cabinets</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/451.png</image:loc>
      <image:title>KUNETT Model 451 Aluminium Sliding Counsil Handle</image:title>
      <image:caption>Zero-clearance flush-mount sliding handle designed for modern sliding wardrobes and pocket doors</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/501.png</image:loc>
      <image:title>KUNETT Model 501 Aluminium Cabinet Knob</image:title>
      <image:caption>Minimalist solid aluminium geometric cabinet knob for luxury vanities, dressers, and bedside tables</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/aluminium-handle-profile.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/301.png</image:loc>
      <image:title>Aluminium Handle Profile Model 301</image:title>
      <image:caption>J-Pull and G-Profile edge-mounted continuous aluminium handle profile</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/aluminium-handles.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/201.png</image:loc>
      <image:title>Solid Aluminium Handle Model 201</image:title>
      <image:caption>Aerospace-grade solid aluminium pull handle for kitchen and wardrobe</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/wardrobe-counsil-handles.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.90</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/401.png</image:loc>
      <image:title>Concealed Counsil Handle Model 401</image:title>
      <image:caption>Concealed solid aluminium counsil handle for heavy wardrobe shutters</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/sliding-wardrobe-handles.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.90</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/451.png</image:loc>
      <image:title>Sliding Wardrobe Handle Model 451</image:title>
      <image:caption>Flush recessed zero-clearance handle for sliding wardrobes</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/cabinet-knobs.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/501.png</image:loc>
      <image:title>Solid Aluminium Knob Model 501</image:title>
      <image:caption>Geometric minimalist solid aluminium cabinet knob</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/our-process.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/process_vmc.jpg</image:loc>
      <image:title>5-Axis VMC Machining in Rajkot Factory</image:title>
      <image:caption>Precision VMC milling of architectural aluminium handles</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://kunetthardware.com/assets/process_anodizing.jpg</image:loc>
      <image:title>Electrochemical Anodizing Baths</image:title>
      <image:caption>Scratch-proof micron anodizing for hardware finishes</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://kunetthardware.com/contact.html</loc>
    <lastmod>2026-10-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
</urlset>
"""

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
print("Updated: sitemap.xml with 8 indexed URLs.")
