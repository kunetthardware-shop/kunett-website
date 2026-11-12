#!/usr/bin/env python3
"""
generate_all_seo_pages.py
Creates complete, self-contained, pre-rendered static HTML landing pages
for each hardware category, our-process, and contact page.
Also updates index.html navigation and sitemap.xml.
"""

import os
import json

jpg_models = ['210', '211', '212', '222', '223', '224', '234', '235', '236', '418']

desc_data = {
    'Cabinet Handle': {
        'adjs': ['sleek', 'bold', 'sophisticated', 'refined', 'heavy-duty', 'sculptural', 'precision-milled', 'striking'],
        'feats': ['an ergonomic inner sweep', 'a subtle chamfered edge', 'perfectly spaced mounting points', 'a highly tactile grip', 'clean architectural lines', 'a gentle outward curve', 'a minimalist straight bar profile'],
        'bens': ['effortless pulling power', 'a reassuringly solid feel in hand', 'a seamless transition from wood to metal', 'flawless daily utility', 'an immediate sense of quality'],
        'concs': ['An essential upgrade for contemporary kitchen and wardrobe doors.', 'Engineered to withstand decades of heavy daily use.', 'Instantly elevates the look of any premium cabinetry.', 'A masterclass in modern metalwork.', 'The perfect finishing touch for a high-end interior.']
    },
    'Cabinet Profile': {
        'adjs': ['minimalist', 'ultra-modern', 'discreet', 'seamless', 'flush-fitting', 'linear', 'unobtrusive'],
        'feats': ['an edge-mounted architecture', 'a continuous linear grip', 'a hidden mounting channel', 'a razor-thin visible edge', 'a perfectly angled finger-pull'],
        'bens': ['a stunning handle-less aesthetic', 'uninterrupted flow across your drawers', 'effortless usability without breaking the visual line', 'a streamlined silhouette', 'a perfectly clean façade'],
        'concs': ['The definitive choice for modern, flat-panel cabinetry.', 'A beautiful marriage of hidden form and daily utility.', 'Redefines the edges of your furniture.', 'Subtle, yet incredibly effective.', 'Brings a showroom-quality finish to your home.']
    },
    'Counsil Handle': {
        'adjs': ['commanding', 'substantive', 'elegant', 'geometric', 'imposing', 'luxurious', 'architectural'],
        'feats': ['a deep finger recess', 'a robust backplate', 'distinctive angular cuts', 'a flawlessly smooth face', 'a wide, comfortable stance'],
        'bens': ['superior leverage for heavier doors', 'a striking focal point for the room', 'an opulent touch to your woodwork', 'a highly comfortable grip', 'a distinct visual anchor'],
        'concs': ['Perfectly suited for tall wardrobes and heavy pantry doors.', 'Makes a grand statement in any setting.', 'Built to impress and engineered to last.', 'A true centerpiece for premium furniture.', 'Combines heavy-duty function with high-end luxury.']
    },
    'Sliding Counsil': {
        'adjs': ['flush-mounted', 'streamlined', 'integrated', 'low-profile', 'sleek', 'embedded', 'practical'],
        'feats': ['a perfectly recessed grip cavity', 'smooth inner chamfers', 'a zero-clearance profile', 'a seamless inset design', 'an optimized sliding track angle'],
        'bens': ['effortless side-to-side gliding', 'zero interference with overlapping doors', 'a completely flush aesthetic', 'a comfortable, pinch-free grip', 'smooth operation for heavy panels'],
        'concs': ['The ultimate hardware solution for modern sliding wardrobes.', 'Precision machined to fit flawlessly into your doors.', 'Uncompromising quality for space-saving designs.', 'Where advanced engineering meets subtle design.', 'Glides as beautifully as it looks.']
    },
    'Cabinet Knob': {
        'adjs': ['tactile', 'minimalist', 'refined', 'sculpted', 'geometric', 'petite', 'understated'],
        'feats': ['a knurled perimeter', 'a subtly concave top', 'flawlessly machined bevels', 'a substantial solid-brass feel', 'an architectural profile'],
        'bens': ['an exquisite touch point', 'effortless micro-adjustments to your decor', 'a discrete pop of luxury metal', 'a satisfying tactile experience', 'visual harmony across smaller drawers'],
        'concs': ['The ultimate accent piece for bedside tables and custom vanities.', 'Elevates standard cabinetry into bespoke furniture.', 'Small in stature, monumental in design impact.', 'Designed for those who appreciate microscopic perfection.', 'Subtle luxury at your fingertips.']
    }
}

def generate_desc(code, category):
    data = desc_data.get(category, desc_data['Cabinet Handle'])
    code_num = int(code)
    h = code_num * 31 + len(category) * 17
    adj = data['adjs'][h % len(data['adjs'])]
    feat = data['feats'][(h >> 1) % len(data['feats'])]
    ben = data['bens'][(h >> 2) % len(data['bens'])]
    conc = data['concs'][(h >> 3) % len(data['concs'])]
    return f"Model {code} is a {adj} {category.lower()} that instantly upgrades your space. Designed with {feat}, it provides {ben}. {conc}"

def get_color_style(color):
    cmap = {
        'Black': 'background-color: #1a1a1a;',
        'R Gold': 'background: linear-gradient(135deg, #b76e79 0%, #e0bfb8 100%);',
        'Gold': 'background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);',
        'SS Matt': 'background: linear-gradient(135deg, #E0E0E0 0%, #9E9E9E 100%);',
        'Antique': 'background: linear-gradient(135deg, #8B7355 0%, #D2B48C 100%);',
        'Grey': 'background-color: #757575;',
        'CP': 'background: linear-gradient(135deg, #FFFFFF 0%, #E0E0E0 100%);'
    }
    return cmap.get(color, 'background-color: #cccccc;')

def build_products(start, end, series, category, finishes, sizes):
    prods = []
    for i in range(start, end + 1):
        code = str(i)
        ext = '.jpg' if code in jpg_models else '.png'
        prods.append({
            'code': code,
            'image': f'assets/{code}{ext}',
            'series': series,
            'category': category,
            'finishes': finishes,
            'sizes': sizes,
            'description': generate_desc(code, category)
        })
    return prods

all_pages = [
    {
        'filename': 'aluminium-handle-profile.html',
        'series': '300',
        'active_nav': 'nav-300',
        'name': 'Aluminium Handle Profile',
        'h1': 'Aluminium Handle Profile Manufacturer in Rajkot',
        'sub': 'Edge-Mounted Architectural J-Pull & G-Profile Systems for Seamless Handle-Less Modular Kitchens & Wardrobes',
        'category': 'Cabinet Profile',
        'range': (301, 324),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'CP', 'Grey'],
        'sizes': ['6" To 36" (Custom cuts up to 3 meters)'],
        'meta_title': 'Aluminium Handle Profile Manufacturer | J-Pull & G-Profile | KUNETT Hardware',
        'meta_desc': 'Rajkot\'s premier manufacturer of solid aluminium handle profile systems. Continuous J-pull, G-profile, and edge-mount profiles for modular kitchens and wardrobe shutters. Direct factory prices.',
        'meta_keywords': 'aluminium handle profile, aluminium handle profile manufacturer, aluminium profile handles, J pull aluminium profile, G profile aluminium handle, edge handle profile, modular kitchen handle profile, Rajkot aluminium profile manufacturer, KUNETT hardware, Harikrushna Enterprise',
        'breadcrumbs': [('Home', 'index.html'), ('Aluminium Handle Profile', 'aluminium-handle-profile.html')],
        'content_intro': """
            <div class="bg-white rounded-3xl p-8 md:p-12 border border-brand-lightgray mb-12 shadow-sm">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-bold uppercase tracking-widest bg-brand-black text-white px-3.5 py-1.5 rounded-full mb-4">Architectural Edge Systems</span>
                    <h2 class="font-serif text-2xl md:text-4xl text-brand-black mb-4">Why Architects & Modular Kitchen Fabricators Choose KUNETT Profiles</h2>
                    <p class="text-brand-gray text-base md:text-lg leading-relaxed mb-6">
                        In modern interior architecture, visual clutter is eliminated in favor of clean, continuous lines. KUNETT 300 Series Aluminium Handle Profiles deliver that seamless handle-less aesthetic without sacrificing everyday ergonomics. Machined from virgin 6063 aerospace-grade aluminium and treated with electrochemical anodization, our profiles fit effortlessly onto standard 18mm and 19mm shutter edges.
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4 border-t border-brand-lightgray/60">
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">J-Pull & G-Profile Options</h4>
                            <p class="text-xs text-brand-gray">Available in top edge wrap (J-Profile) or recessed channel (Gola / G-Profile) configurations.</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">Continuous 3-Meter Bars</h4>
                            <p class="text-xs text-brand-gray">Supplied pre-cut (6" to 36") or as full 3-meter profiles for custom on-site carpenter fabrication.</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">Scratch-Proof Anodizing</h4>
                            <p class="text-xs text-brand-gray">Matte Black, Rose Gold, Champagne Gold, and SS Matt that resist oil, fingerprints, and moisture.</p>
                        </div>
                    </div>
                </div>
            </div>
        """,
        'faqs': [
            ("What is an aluminium handle profile?", "An aluminium handle profile is an edge-mounted continuous hardware extrusion that clips or slots directly onto the top or edge of modular cabinet shutters and wardrobe doors. It creates a modern, sleek handle-less aesthetic with a comfortable finger recess."),
            ("What is the difference between J-Profile and G-Profile handles?", "A J-profile handle wraps over the top edge of a drawer shutter with a subtle downward curve, ideal for top kitchen drawers. A G-profile (or Gola profile) sits horizontally or vertically between cabinet shutters, allowing your fingers to hook in from behind for a completely flush, ultra-minimal look."),
            ("What lengths are available for KUNETT aluminium handle profiles?", "We supply standard cut sizes from 6\" to 36\" for modular drawers, as well as full continuous 3-meter (10 ft) profile lengths for carpenters, interior contractors, and factory fabricators."),
            ("Will the finish on aluminium profile handles wear off with daily kitchen use?", "Never. KUNETT profiles undergo multi-tank electrochemical anodizing, not spray painting. The color is integrated into the molecular surface of the aluminium, creating a scratch-resistant, stain-resistant, and grease-proof barrier designed for intensive kitchen environments.")
        ]
    },
    {
        'filename': 'aluminium-handles.html',
        'series': '200',
        'active_nav': 'nav-200',
        'name': 'Aluminium Handles',
        'h1': 'Solid Aluminium Handles Manufacturer in Rajkot',
        'sub': 'Premium Aerospace-Grade Solid Aluminium Pull Handles for Modular Kitchens, Wardrobe Shutters & Cabinet Drawers',
        'category': 'Cabinet Handle',
        'range': (201, 246),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'Antique', 'Grey'],
        'sizes': ['6"', '8"', '12"', '18"', '24"', '30"', '36"', '48"'],
        'meta_title': 'Solid Aluminium Handles Manufacturer in Rajkot | KUNETT Hardware',
        'meta_desc': 'Leading manufacturer of solid aluminium handles & cabinet pull handles in Rajkot, India. 100% aerospace-grade virgin alloy for luxury kitchens and wardrobes. Factory direct prices.',
        'meta_keywords': 'aluminium handles, solid aluminium handles, aluminium cabinet handles, aluminium pull handles, modular kitchen aluminium handles, wardrobe handles, Rajkot hardware manufacturer, KUNETT hardware, Harikrushna Enterprise',
        'breadcrumbs': [('Home', 'index.html'), ('Aluminium Handles', 'aluminium-handles.html')],
        'content_intro': """
            <div class="bg-white rounded-3xl p-8 md:p-12 border border-brand-lightgray mb-12 shadow-sm">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-bold uppercase tracking-widest bg-brand-black text-white px-3.5 py-1.5 rounded-full mb-4">Solid Architectural Hardware</span>
                    <h2 class="font-serif text-2xl md:text-4xl text-brand-black mb-4">Precision CNC-Machined Solid Aluminium Handles</h2>
                    <p class="text-brand-gray text-base md:text-lg leading-relaxed mb-6">
                        Every handle in the KUNETT 200 Series is carved from solid aerospace-grade aluminium alloy billets. Unlike light, hollow zinc or fragile plastic pulls, KUNETT handles deliver an unmistakable reassuring weight, structural stability, and razor-sharp chamfered details. Designed for modular kitchens, floor-to-ceiling wardrobes, and luxury office cabinetry.
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4 border-t border-brand-lightgray/60">
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">Sizes Up To 48 Inches</h4>
                            <p class="text-xs text-brand-gray">Extended lengths designed specifically for full-height sliding and hinged wardrobe shutters.</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">Standard Hole Centers</h4>
                            <p class="text-xs text-brand-gray">Universal metric and imperial center-to-center hole spacing for effortless carpenter installation.</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-black text-sm mb-1">Direct Factory Pricing</h4>
                            <p class="text-xs text-brand-gray">Genuine manufacturer pricing across India for homeowners, dealers, and modular furniture brands.</p>
                        </div>
                    </div>
                </div>
            </div>
        """,
        'faqs': [
            ("What makes KUNETT solid aluminium handles better than zinc alloy handles?", "Unlike cheap hollow zinc handles that break or corrode over time, KUNETT handles are precision-machined from 100% solid aerospace-grade virgin 6063 aluminium alloy. They never rust, feature an unyielding solid weight, and retain their micron-anodized finish for decades."),
            ("What sizes are available for KUNETT solid aluminium handles?", "Standard lengths include 6\", 8\", 12\", 18\", 24\", 30\", 36\", and 48\" for tall wardrobe shutters. Custom architectural lengths and hole center-to-center distances can be manufactured for bulk projects."),
            ("Can individual homeowners buy aluminium handles directly?", "Yes! Homeowners across India can order directly at factory pricing with zero intermediary markups. We deliver safely packaged boxes directly to your doorstep in Mumbai, Delhi, Bengaluru, Hyderabad, Rajkot, and all Indian cities."),
            ("Which finishes are available for the 200 Series?", "Our signature finishes include Matte Black, Rose Gold, Champagne Gold, Stainless Steel Matt (SS Matt), Antique Brass, and Graphite Grey. All finishes are created via electrochemical anodizing that will never peel or tarnish.")
        ]
    },
    {
        'filename': 'wardrobe-counsil-handles.html',
        'series': '400',
        'active_nav': 'nav-400',
        'name': 'Counsil Handles',
        'h1': 'Aluminium Counsil Handles Manufacturer in Rajkot',
        'sub': 'Substantive Concealed Solid Aluminium Handles Engineered for Heavy Wardrobe Shutters & Pantry Cabinets',
        'category': 'Counsil Handle',
        'range': (401, 418),
        'finishes': ['CP', 'Black', 'R Gold', 'Gold', 'SS Matt'],
        'sizes': ['4"', '6"', '8"', '10"', '12"'],
        'meta_title': 'Aluminium Counsil Handles Manufacturer | Concealed Wardrobe Pulls | KUNETT',
        'meta_desc': 'Solid aluminium counsil handles & concealed shutter pulls manufactured in Rajkot. Deep ergonomic finger recess engineered for heavy modular wardrobe and pantry doors. Factory direct rates.',
        'meta_keywords': 'counsil handles, aluminium counsil handles, concealed wardrobe handles, flush counsil handle, concealed handles for wardrobe, Rajkot counsil handle manufacturer, KUNETT hardware',
        'breadcrumbs': [('Home', 'index.html'), ('Counsil Handles', 'wardrobe-counsil-handles.html')],
        'content_intro': """
            <div class="bg-white rounded-3xl p-8 md:p-12 border border-brand-lightgray mb-12 shadow-sm">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-bold uppercase tracking-widest bg-brand-black text-white px-3.5 py-1.5 rounded-full mb-4">Concealed Ergonomics</span>
                    <h2 class="font-serif text-2xl md:text-4xl text-brand-black mb-4">Deep-Recess Concealed Counsil Handles for Wardrobes</h2>
                    <p class="text-brand-gray text-base md:text-lg leading-relaxed mb-6">
                        Heavy wooden wardrobe shutters and pantry doors require exceptional pulling leverage. The KUNETT 400 Series Counsil Handles are engineered with a deep, curved finger pocket and a sturdy backplate. Recessed neatly into the shutter edge or surface, they offer a commanding grip while preserving a flush, minimalist architectural profile.
                    </p>
                </div>
            </div>
        """,
        'faqs': [
            ("What is a counsil handle?", "A counsil handle is a semi-concealed architectural pull that features a deep inner cavity and a wide backplate. It is recessed into the woodwork or edge-mounted to provide maximum leverage when opening heavy wardrobe shutters and tall pantry doors."),
            ("What sizes are available in the 400 Series Counsil Handles?", "We manufacture Model 401 through 418 in standard lengths of 4\", 6\", 8\", 10\", and 12\". Custom project sizes can also be milled using our 5-axis VMC machining centers in Rajkot."),
            ("Why choose aluminium counsil handles over zinc or plastic?", "Solid aluminium counsil handles provide uncompromising rigidity under heavy pulling force. They will not bend, crack, or loosen over time, ensuring a luxury feel throughout decades of daily wardrobe use.")
        ]
    },
    {
        'filename': 'sliding-wardrobe-handles.html',
        'series': '450',
        'active_nav': 'nav-450',
        'name': 'Sliding Counsils',
        'h1': 'Sliding Wardrobe Aluminium Handles Manufacturer',
        'sub': 'Zero-Clearance Flush Recessed Solid Aluminium Handles Designed for Modern Sliding Wardrobes & Pocket Doors',
        'category': 'Sliding Counsil',
        'range': (451, 455),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'Grey'],
        'sizes': ['4"', '6"', '8"', '10"', '12"', '18"', '24"', '36"'],
        'meta_title': 'Sliding Wardrobe Aluminium Handles | Zero-Clearance Flush Counsils | KUNETT',
        'meta_desc': 'Flush-mounted solid aluminium sliding counsil handles for modern sliding wardrobes and pocket doors. Zero-clearance profile prevents door collision. Direct factory rates.',
        'meta_keywords': 'sliding wardrobe handles, sliding counsil handles, flush wardrobe handles, recessed sliding door handles, pocket door handles, aluminium sliding handles Rajkot, KUNETT hardware',
        'breadcrumbs': [('Home', 'index.html'), ('Sliding Counsils', 'sliding-wardrobe-handles.html')],
        'content_intro': """
            <div class="bg-white rounded-3xl p-8 md:p-12 border border-brand-lightgray mb-12 shadow-sm">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-bold uppercase tracking-widest bg-brand-black text-white px-3.5 py-1.5 rounded-full mb-4">Zero-Clearance Architecture</span>
                    <h2 class="font-serif text-2xl md:text-4xl text-brand-black mb-4">Zero-Interference Flush Handles for Sliding Shutters</h2>
                    <p class="text-brand-gray text-base md:text-lg leading-relaxed mb-6">
                        Standard handles collide and damage overlapping sliding wardrobe doors. The KUNETT 450 Series features an ultra-low flush silhouette that nests completely inside the shutter routing. Doors glide past each other smoothly with zero friction, while providing a comfortable, pinch-free grip.
                    </p>
                </div>
            </div>
        """,
        'faqs': [
            ("Why are zero-clearance sliding handles essential for sliding wardrobes?", "In sliding wardrobes, overlapping doors must pass each other with very tight tolerances (often only 5mm to 10mm). KUNETT 450 Series handles are flush-recessed so doors glide smoothly past each other without colliding or scratching."),
            ("How are sliding counsil handles installed?", "A precision groove is routed into the wooden shutter according to our CAD specifications, and the aluminium handle is securely embedded and fastened from the rear or side.")
        ]
    },
    {
        'filename': 'cabinet-knobs.html',
        'series': '500',
        'active_nav': 'nav-500',
        'name': 'Cabinet Knobs',
        'h1': 'Solid Aluminium Cabinet Knobs Manufacturer in Rajkot',
        'sub': 'Minimalist Architectural Solid Aluminium Knobs for Luxury Vanities, Drawers, Nightstands & Dressers',
        'category': 'Cabinet Knob',
        'range': (501, 508),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'Grey'],
        'sizes': ['2" Diameter & Geometric Profiles'],
        'meta_title': 'Solid Aluminium Cabinet Knobs Manufacturer | Minimalist Drawer Knobs | KUNETT',
        'meta_desc': 'Precision-milled solid aluminium cabinet knobs for luxury bathrooms, modular kitchens, nightstands, and dressers. Available in 8 anodized designer finishes. Factory direct supply.',
        'meta_keywords': 'aluminium cabinet knobs, solid aluminium knobs, drawer knobs, kitchen cabinet knobs, luxury vanity knobs, minimalist furniture knobs, Rajkot knob manufacturer, KUNETT hardware',
        'breadcrumbs': [('Home', 'index.html'), ('Cabinet Knobs', 'cabinet-knobs.html')],
        'content_intro': """
            <div class="bg-white rounded-3xl p-8 md:p-12 border border-brand-lightgray mb-12 shadow-sm">
                <div class="max-w-3xl">
                    <span class="inline-block text-xs font-bold uppercase tracking-widest bg-brand-black text-white px-3.5 py-1.5 rounded-full mb-4">Micro-Machined Luxury</span>
                    <h2 class="font-serif text-2xl md:text-4xl text-brand-black mb-4">Solid Aluminium Knobs for Designer Furniture</h2>
                    <p class="text-brand-gray text-base md:text-lg leading-relaxed mb-6">
                        Small hardware makes a monumental design statement. The KUNETT 500 Series features CNC-milled solid aluminium geometric and circular knobs with knurled perimeters, concave touch points, and polished bevels. Perfect for luxury master bathroom vanities, custom nightstands, and dressing tables.
                    </p>
                </div>
            </div>
        """,
        'faqs': [
            ("What makes KUNETT solid aluminium knobs unique?", "Each knob in our 500 Series is CNC-milled from a solid aerospace billet of aluminium. The weight, tactile feel, chamfered bevels, and micro-knurled grip provide an unmistakably luxurious sensation."),
            ("Where are these knobs best installed?", "They are ideal for bathroom vanities, bedroom nightstands, office credenzas, custom dressers, and accent kitchen drawers.")
        ]
    }
]

print(f"Prepared configuration for {len(all_pages)} category pages.")

def render_navbar(active_key):
    # Tier 1 & Tier 2 navigation
    # active_key can be 'nav-home', 'nav-process', 'nav-contact', 'nav-200', 'nav-300', 'nav-400', 'nav-450', 'nav-500'
    
    tier2_items = [
        ('nav-200', 'aluminium-handles.html', 'Aluminium Handles'),
        ('nav-300', 'aluminium-handle-profile.html', 'Aluminium Handle Profile'),
        ('nav-400', 'wardrobe-counsil-handles.html', 'Counsil Handles'),
        ('nav-450', 'sliding-wardrobe-handles.html', 'Sliding Counsils'),
        ('nav-500', 'cabinet-knobs.html', 'Cabinet Knobs')
    ]
    
    tier2_links = []
    for nav_id, url, label in tier2_items:
        is_active = (nav_id == active_key)
        active_class = "text-brand-black border-b-2 border-brand-black pb-0.5" if is_active else "text-brand-gray hover:text-brand-black"
        tier2_links.append(f'<a href="{url}" id="{nav_id}" class="nav-link text-xs font-bold uppercase tracking-widest {active_class} transition-colors">{label}</a>')
    tier2_html = "\n            ".join(tier2_links)

    nav_home_class = "text-brand-black border-b-2 border-brand-black" if active_key == 'nav-home' else "hover:text-brand-gray"
    nav_process_class = "text-brand-black border-b-2 border-brand-black" if active_key == 'nav-process' else "hover:text-brand-gray"
    nav_contact_class = "text-brand-black border-b-2 border-brand-black" if active_key == 'nav-contact' else "hover:text-brand-gray"

    return f"""
    <!-- Sticky Navigation - Perfectly In-Line -->
    <nav class="sticky top-0 z-[100] bg-white border-b border-brand-lightgray shadow-sm">
        <div class="max-w-[90rem] mx-auto px-4 md:px-8 py-3 flex items-center justify-between gap-6 bg-white relative z-50">
            
            <!-- Logo (Left Aligned) -->
            <a href="index.html" class="flex-shrink-0 flex items-center z-50">
                <img src="assets/logo.png" alt="KUNETT Hardware - Aluminium Handles & Profiles Manufacturer Rajkot" class="h-16 md:h-24 w-auto object-contain">
            </a>

            <!-- Mobile: Quick Icons (Right Aligned) -->
            <div class="flex md:hidden items-center gap-5 z-50 bg-white">
                <a href="#inquiry" onclick="openInquiryModal(); return false;" class="relative text-brand-black p-1 focus:outline-none" aria-label="Inquiry List">
                    <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
                    <span id="mobile-inquiry-badge" class="absolute -top-1 -right-1 bg-brand-black text-white text-[10px] rounded-full w-4 h-4 flex items-center justify-center hidden">0</span>
                </a>
                <button onclick="toggleMobileMenu()" class="text-brand-black p-1 focus:outline-none" aria-label="Toggle Navigation Menu">
                    <svg id="hamburger-icon" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
                    <svg id="close-icon" class="hidden" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Desktop: Navigation Links (Hidden on Mobile) -->
            <div class="hidden md:flex gap-6 items-center flex-nowrap whitespace-nowrap justify-end w-full pl-6">
                <a href="index.html" id="nav-home" class="nav-link text-sm font-medium {nav_home_class} transition-colors">Home</a>
                <a href="our-process.html" id="nav-process" class="nav-link text-sm font-medium {nav_process_class} transition-colors">Our Process</a>
                <a href="index.html#blog" id="nav-blog" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Blog</a>
                <a href="contact.html" id="nav-contact" class="nav-link text-sm font-medium {nav_contact_class} transition-colors">Contact</a>
                
                <div class="w-px h-5 bg-brand-lightgray mx-1"></div>

                <a href="index.html#calculator" id="nav-calculator" class="nav-link text-sm font-medium text-brand-black font-bold hover:text-brand-gray transition-colors flex items-center gap-1.5">
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg> Calculator
                </a>
                
                <a href="#inquiry" onclick="openInquiryModal(); return false;" id="nav-inquiry" class="nav-link text-sm font-bold hover:text-brand-gray transition-colors flex items-center gap-1.5">
                    Inquiry List <span id="inquiry-badge" class="bg-brand-black text-white text-[10px] rounded-full w-5 h-5 flex items-center justify-center hidden shadow-sm">0</span>
                </a>
                
                <a href="#" onclick="openCatalogueModal(event)" class="text-sm font-bold bg-brand-black text-white px-6 py-2.5 rounded-full hover:opacity-80 transition-opacity ml-2 shadow-sm">
                    Catalogue
                </a>
            </div>
        </div>

        <!-- Secondary Product Categories Navbar -->
        <div class="hidden md:flex justify-center gap-12 bg-brand-offwhite border-t border-brand-lightgray py-3 shadow-sm relative z-40">
            {tier2_html}
        </div>
    </nav>
    
    <!-- Mobile Menu Drawer Backdrop -->
    <div id="mobile-backdrop" onclick="closeMobileMenu()" class="md:hidden fixed inset-0 bg-black/60 z-[90] transition-opacity duration-300 opacity-0 pointer-events-none"></div>

    <!-- Mobile Menu Drawer (Slide from Right) -->
    <div id="mobile-menu" class="md:hidden fixed top-0 right-0 w-[85vw] max-w-sm h-full bg-white shadow-2xl transition-transform duration-300 transform translate-x-full z-[100] flex flex-col">
        <div class="p-6 border-b border-brand-lightgray flex justify-between items-center bg-brand-offwhite">
            <span class="font-serif text-2xl text-brand-black font-bold">Menu</span>
            <button onclick="closeMobileMenu()" class="p-2 text-brand-black hover:text-brand-gray transition-colors bg-white rounded-full shadow-sm border border-brand-lightgray">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
        </div>

        <div class="flex flex-col p-6 gap-2 text-base font-bold text-brand-black overflow-y-auto flex-grow pb-24">
            <a href="index.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Home</a>
            <a href="our-process.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Our Process</a>
            <a href="index.html#blog" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Blog</a>
            <a href="index.html#calculator" class="text-left py-3 border-b border-brand-lightgray/50 text-brand-black flex items-center justify-between font-bold">
                Project Calculator <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/><line x1="8" y1="18" x2="16" y2="18"/></svg>
            </a>
            
            <a href="aluminium-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handles</a>
            <a href="aluminium-handle-profile.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Aluminium Handle Profile</a>
            <a href="wardrobe-counsil-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Counsil Handles</a>
            <a href="sliding-wardrobe-handles.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Sliding Counsils</a>
            <a href="cabinet-knobs.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Cabinet Knobs</a>
            <a href="contact.html" class="text-left py-3 border-b border-brand-lightgray/50 text-brand-black font-bold">Contact Us</a>
            <a href="#inquiry" onclick="closeMobileMenu(); openInquiryModal(); return false;" class="text-left py-3 border-b border-brand-lightgray/50">My Inquiry List</a>
            <a href="#" onclick="closeMobileMenu(); openCatalogueModal(event)" class="mt-8 text-center text-sm bg-brand-black text-white px-5 py-4 rounded-full shadow-lg">Download Catalogue</a>
        </div>
    </div>
    """

print("Navbar renderer ready.")
