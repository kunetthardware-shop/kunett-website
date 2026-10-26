#!/usr/bin/env python3
"""
build_complete_site.py
Full automated generator for KUNETT Hardware static SEO pages:
- aluminium-handle-profile.html (300 Series)
- aluminium-handles.html (200 Series)
- wardrobe-counsil-handles.html (400 Series)
- sliding-wardrobe-handles.html (450 Series)
- cabinet-knobs.html (500 Series)
- our-process.html (Manufacturing Process in Rajkot)
- contact.html (Contact Us & Showroom)
- index.html (Updated with real static links)
- sitemap.xml (Comprehensive image and page sitemap)
"""

import os
import json
import re

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

def render_head(title, desc, keywords, canonical_url, schema_json):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Harikrushna Enterprise">
    <meta name="geo.region" content="IN-GJ">
    <meta name="geo.placename" content="Rajkot">
    <meta name="geo.position" content="22.239264;70.803659">
    <meta name="ICBM" content="22.239264, 70.803659">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="https://kunetthardware.com/assets/logo.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://kunetthardware.com/assets/logo.png">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="google-site-verification" content="QRnYqolZjasBui8Eh4pJYiUIb8mCODUFxSQsaiOg0UQ" />
    <link rel="canonical" href="{canonical_url}" />
    <!-- Favicon & Site Icons for Google Search -->
    <link rel="shortcut icon" href="https://kunetthardware.com/favicon.ico">
    <link rel="icon" type="image/x-icon" href="https://kunetthardware.com/favicon.ico">
    <link rel="icon" type="image/png" sizes="16x16" href="https://kunetthardware.com/assets/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://kunetthardware.com/assets/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="48x48" href="https://kunetthardware.com/assets/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="https://kunetthardware.com/assets/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="https://kunetthardware.com/assets/favicon-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="https://kunetthardware.com/assets/favicon-512x512.png">
    <link rel="apple-touch-icon" sizes="180x180" href="https://kunetthardware.com/assets/apple-touch-icon.png">
    <link rel="apple-touch-icon" href="https://kunetthardware.com/apple-touch-icon.png">
    <link rel="manifest" href="https://kunetthardware.com/site.webmanifest">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{ pink: '#f4d4d4', black: '#1a1a1a', white: '#ffffff', offwhite: '#f9f9f9', gray: '#757575', lightgray: '#e5e5e5' }}
                    }},
                    fontFamily: {{ sans: ['Inter', 'sans-serif'], serif: ['Playfair Display', 'serif'] }}
                }}
            }}
        }}
    </script>
    <style>
        @keyframes loading {{
            0% {{ width: 0%; transform: translateX(-100%); }}
            50% {{ width: 100%; transform: translateX(0); }}
            100% {{ width: 0%; transform: translateX(200%); }}
        }}
        body {{ background-color: #ffffff; color: #1a1a1a; -webkit-font-smoothing: antialiased; }}
        .product-card {{ transition: transform 0.3s ease; }}
        @media (min-width: 768px) {{ .product-card:hover .product-img {{ transform: translateY(-5px); }} }}
        .product-img {{ transition: transform 0.4s ease; mix-blend-mode: multiply; }}
        .btn-primary {{ background-color: #1a1a1a; color: #ffffff; transition: opacity 0.2s ease; }}
        .btn-primary:hover {{ opacity: 0.85; }}
        .drawer-overlay {{ opacity: 0; visibility: hidden; transition: opacity 0.3s ease, visibility 0.3s ease; }}
        .drawer-overlay.active {{ opacity: 1; visibility: visible; }}
        .drawer-content {{ transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); }}
        .drawer-overlay.active .drawer-content {{ transform: translateX(0); }}
        .catalogue-active {{ opacity: 1 !important; visibility: visible !important; }}
        .catalogue-active #catalogue-modal-content {{ transform: scale(1) !important; opacity: 1 !important; }}
        .nav-link {{ border-bottom: 2px solid transparent; }}
        .nav-link.active {{ color: #1a1a1a; border-bottom: 2px solid #1a1a1a; }}
    </style>
    <!-- Structured Data -->
    <script type="application/ld+json">
    {schema_json}
    </script>
</head>
<body class="bg-brand-offwhite text-brand-black font-sans antialiased overflow-x-hidden selection:bg-brand-black selection:text-white">
"""

def render_navbar(active_key):
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
    <!-- Flying Robot Cursor Companion (Desktop Only) -->
    <div id="cursor-robot" class="hidden md:block fixed pointer-events-none z-[9999] will-change-transform transition-opacity duration-500 opacity-0" style="top: 0; left: 0; transform: translate(-100px, -100px);">
        <svg width="36" height="36" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" class="drop-shadow-lg">
            <line x1="50" y1="20" x2="50" y2="5" stroke="#111" stroke-width="4" stroke-linecap="round"/>
            <circle cx="50" cy="5" r="5" fill="#E23E57" class="animate-pulse"/>
            <rect x="20" y="20" width="60" height="50" rx="12" fill="#1A1A1A"/>
            <rect x="25" y="25" width="50" height="30" rx="6" fill="#0A0A0A"/>
            <circle id="robot-eye-l" cx="35" cy="40" r="5" fill="#00FFCC"/>
            <circle id="robot-eye-r" cx="65" cy="40" r="5" fill="#00FFCC"/>
            <rect x="40" y="60" width="20" height="4" rx="2" fill="#333"/>
        </svg>
    </div>
    <!-- Premium Preloader -->
    <div id="preloader" class="fixed inset-0 z-[9999] bg-white flex justify-center items-center transition-opacity duration-700">
        <div class="flex flex-col items-center gap-4">
            <img src="assets/logo.png" alt="KUNETT Hardware" class="h-16 md:h-24 animate-pulse object-contain">
            <div class="w-48 h-1 bg-brand-lightgray rounded-full overflow-hidden">
                <div class="h-full bg-brand-black rounded-full animate-[loading_1.5s_ease-in-out_infinite]"></div>
            </div>
        </div>
    </div>

    <!-- Sticky Navigation -->
    <nav class="sticky top-0 z-[100] bg-white border-b border-brand-lightgray shadow-sm">
        <div class="max-w-[90rem] mx-auto px-4 md:px-8 py-3 flex items-center justify-between gap-6 bg-white relative z-50">
            
            <a href="/" class="flex-shrink-0 flex items-center z-50">
                <img src="assets/logo.png" alt="KUNETT Hardware - Aluminium Handles & Profiles Manufacturer Rajkot" class="h-16 md:h-24 w-auto object-contain">
            </a>

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

            <div class="hidden md:flex gap-6 items-center flex-nowrap whitespace-nowrap justify-end w-full pl-6">
                <a href="/" id="nav-home" class="nav-link text-sm font-medium {nav_home_class} transition-colors">Home</a>
                <a href="our-process.html" id="nav-process" class="nav-link text-sm font-medium {nav_process_class} transition-colors">Our Process</a>
                <a href="/#blog" id="nav-blog" class="nav-link text-sm font-medium hover:text-brand-gray transition-colors">Blog</a>
                <a href="contact.html" id="nav-contact" class="nav-link text-sm font-medium {nav_contact_class} transition-colors">Contact</a>
                
                <div class="w-px h-5 bg-brand-lightgray mx-1"></div>

                <a href="/#calculator" id="nav-calculator" class="nav-link text-sm font-medium text-brand-black font-bold hover:text-brand-gray transition-colors flex items-center gap-1.5">
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
            <a href="/" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Home</a>
            <a href="our-process.html" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Our Process</a>
            <a href="/#blog" class="text-left py-3 border-b border-brand-lightgray/50 hover:text-brand-gray">Blog</a>
            <a href="/#calculator" class="text-left py-3 border-b border-brand-lightgray/50 text-brand-black flex items-center justify-between font-bold">
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

def render_footer():
    return """
    <!-- Enhanced Luxury Footer -->
    <footer class="border-t border-brand-lightgray pt-16 pb-8 px-6 bg-brand-offwhite">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 mb-12 border-b border-brand-lightgray pb-12">
            <div>
                <img src="assets/logo.png" alt="KUNETT Hardware Logo" class="h-28 md:h-36 w-auto object-contain mb-4">
                <p class="text-sm text-brand-gray max-w-xs leading-relaxed"><strong class="text-brand-black block mb-1">Your new home decorator.</strong>Premier solid aluminium hardware and handle profiles engineered in Rajkot, Gujarat. Direct supply for homeowners, carpenters, and global export.</p>
            </div>
            <div>
                <h4 class="font-bold text-brand-black mb-4">Hardware Collections</h4>
                <ul class="space-y-2.5 text-sm text-brand-gray">
                    <li><a href="aluminium-handles.html" class="hover:text-brand-black transition-colors">Aluminium Handles (200 Series)</a></li>
                    <li><a href="aluminium-handle-profile.html" class="hover:text-brand-black transition-colors font-semibold text-brand-black">Aluminium Handle Profile (300)</a></li>
                    <li><a href="wardrobe-counsil-handles.html" class="hover:text-brand-black transition-colors">Counsil Handles (400 Series)</a></li>
                    <li><a href="sliding-wardrobe-handles.html" class="hover:text-brand-black transition-colors">Sliding Counsils (450 Series)</a></li>
                    <li><a href="cabinet-knobs.html" class="hover:text-brand-black transition-colors">Cabinet Knobs (500 Series)</a></li>
                    <li><a href="our-process.html" class="hover:text-brand-black transition-colors">Factory Manufacturing Process</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-brand-black mb-4">Connect Directly</h4>
                <ul class="space-y-3 text-sm text-brand-gray">
                    <li><a href="https://wa.me/919924637640" target="_blank" class="hover:text-[#25D366] transition-colors flex items-center gap-2"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.192 1.604 6.015L.302 24l6.108-1.6c1.764.957 3.754 1.464 5.62 1.464 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm3.834 17.203c-.161.455-.93 .853-1.312.894-.383.042-.87.126-2.505-.55-1.974-.816-3.238-2.825-3.338-2.961-.101-.136-.798-1.061-.798-2.023 0-.962.5-1.436.682-1.638.181-.202.392-.253.523-.253.131 0 .262 0 .373.01.111.011.262-.042.413.323.151.364.514 1.253.554 1.344.041.091.071.192.01.293-.061.101-.091.162-.181.263-.091.101-.192.222-.272.303-.091.091-.192.192-.081.384.111.192.494.818 1.059 1.323.731.653 1.343.853 1.534.944.192.091.303.081.413-.041.111-.121.484-.565.615-.757.131-.192.262-.162.434-.091.171.071 1.089.515 1.27.606.181.091.303.136.343.212.041.071.041.424-.12.879z"/></svg> WhatsApp Sanjay: +91 99246 37640</a></li>
                    <li><a href="contact.html" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg> support@kunetthardware.com</a></li>
                    <li><a href="https://maps.app.goo.gl/EMsseMvKHpNqxPVh9" target="_blank" class="hover:text-blue-600 transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Rajkot Factory on Google Maps ↗</a></li>
                    <li><a href="https://www.facebook.com/profile.php?id=61594388126613" target="_blank" class="hover:text-[#1877F2] transition-colors flex items-center gap-2"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg> Facebook Profile ↗</a></li>
                    <li><a href="https://www.instagram.com/harikrushna.enterprise/" target="_blank" class="hover:text-[#E1306C] transition-colors flex items-center gap-2"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg> Instagram ↗</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-brand-black mb-4">Resources</h4>
                <ul class="space-y-3 text-sm text-brand-gray">
                    <li><a href="/#blog" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg> Architecture Blog</a></li>
                    <li><a href="#" onclick="openCatalogueModal(event)" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg> Digital Catalogue</a></li>
                    <li><a href="contact.html" class="hover:text-brand-black transition-colors flex items-center gap-2"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg> Factory Inquiries</a></li>
                </ul>
            </div>
        </div>
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center text-xs text-brand-gray">
            <p>© 2026 KUNETT Hardware by Harikrushna Enterprise. All rights reserved.</p>
            <div class="flex gap-4 mt-4 md:mt-0">
                <a href="contact.html" class="hover:text-brand-black transition-colors">Factory Address: Rajkot, Gujarat</a>
                <a href="/" class="hover:text-brand-black transition-colors">Home</a>
            </div>
        </div>
    </footer>
    """

def render_modals_and_scripts(products_json):
    return f"""
    <!-- Product Detail Modal -->
    <div id="product-modal" class="drawer-overlay fixed inset-0 z-[9999] bg-black/60 flex justify-center items-center p-4">
        <div class="bg-white w-full max-w-2xl rounded-3xl shadow-2xl p-6 md:p-10 relative max-h-[90vh] overflow-y-auto transform scale-95 opacity-0 transition-all duration-300" id="product-modal-content">
            <button onclick="closeProductModal()" class="absolute top-5 right-5 p-2 text-brand-gray hover:text-brand-black transition-colors bg-brand-offwhite rounded-full">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
            <div id="modal-product-body"></div>
        </div>
    </div>

    <!-- Inquiry List Drawer Overlay -->
    <div id="inquiry-modal" class="drawer-overlay fixed inset-0 z-[9999] bg-black/60 flex justify-end">
        <div class="drawer-content bg-white w-full max-w-md h-full shadow-2xl flex flex-col p-6 overflow-y-auto" id="inquiry-drawer-content">
            <div class="flex items-center justify-between pb-4 border-b border-brand-lightgray mb-6">
                <h3 class="font-serif text-2xl font-bold text-brand-black">Your Inquiry List</h3>
                <button onclick="closeInquiryModal()" class="p-2 text-brand-gray hover:text-brand-black transition-colors bg-brand-offwhite rounded-full">
                    <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>
            <div id="inquiry-list-items" class="flex-grow space-y-4"></div>
            <div id="inquiry-actions" class="pt-6 border-t border-brand-lightgray mt-auto">
                <button onclick="sendInquiryViaWhatsapp()" id="send-inquiry-btn" class="w-full bg-[#25D366] text-white py-4 rounded-full font-bold text-sm shadow-lg hover:opacity-90 flex items-center justify-center gap-2">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.192 1.604 6.015L.302 24l6.108-1.6c1.764.957 3.754 1.464 5.62 1.464 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm3.834 17.203c-.161.455-.93 .853-1.312.894-.383.042-.87.126-2.505-.55-1.974-.816-3.238-2.825-3.338-2.961-.101-.136-.798-1.061-.798-2.023 0-.962.5-1.436.682-1.638.181-.202.392-.253.523-.253.131 0 .262 0 .373.01.111.011.262-.042.413.323.151.364.514 1.253.554 1.344.041.091.071.192.01.293-.061.101-.091.162-.181.263-.091.101-.192.222-.272.303-.091.091-.192.192-.081.384.111.192.494.818 1.059 1.323.731.653 1.343.853 1.534.944.192.091.303.081.413-.041.111-.121.484-.565.615-.757.131-.192.262-.162.434-.091.171.071 1.089.515 1.27.606.181.091.303.136.343.212.041.071.041.424-.12.879z"/></svg>
                    Send Inquiry on WhatsApp
                </button>
            </div>
        </div>
    </div>

    <!-- Catalogue Lead Gen Modal -->
    <div id="catalogue-modal" class="drawer-overlay fixed inset-0 z-[9999] bg-black/60 flex justify-center items-center p-4">
        <div class="bg-white w-full max-w-md rounded-2xl shadow-2xl p-8 relative transform scale-95 opacity-0 transition-all duration-300" id="catalogue-modal-content">
            <button onclick="closeCatalogueModal()" class="absolute top-4 right-4 p-2 text-brand-gray hover:text-brand-black transition-colors">
                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
            <div class="text-center mb-6 mt-2">
                <h3 id="cat-modal-title" class="font-serif text-2xl md:text-3xl text-brand-black mb-2">Get the Catalogue</h3>
                <p id="cat-modal-sub" class="text-sm text-brand-gray">Please enter your details to instantly download our full architectural catalogue.</p>
            </div>
            <form id="catalogueForm" class="space-y-4">
                <input type="hidden" name="Subject" value="Catalogue Download Lead">
                <input type="hidden" name="Message" value="This user requested to download the digital catalogue.">
                <div>
                    <input type="text" name="Name" required class="w-full border border-brand-lightgray p-3.5 rounded bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="Full Name *">
                </div>
                <div>
                    <input type="email" name="Email" required class="w-full border border-brand-lightgray p-3.5 rounded bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="Email Address *">
                </div>
                <div>
                    <input type="tel" name="Phone" required class="w-full border border-brand-lightgray p-3.5 rounded bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="Phone Number *">
                </div>
                <button type="submit" id="catSubmitBtn" class="btn-primary w-full py-4 rounded-full font-bold text-sm tracking-wide shadow-lg hover:opacity-90 transition-opacity mt-2">
                    Submit & Download
                </button>
                <div id="catFormStatus" class="hidden text-center text-xs font-bold mt-3"></div>
            </form>
        </div>
    </div>

    <!-- Custom Chatbot UI -->
    <div id="kunett-bot-container" class="fixed bottom-6 right-6 z-[100] flex flex-col items-end pointer-events-none">
        <div id="kunett-chat-window" class="hidden w-[90vw] sm:w-80 bg-white rounded-2xl shadow-2xl border border-brand-lightgray overflow-hidden mb-4 transform transition-all origin-bottom-right pointer-events-auto">
            <div class="bg-brand-black text-white p-4 flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center p-1.5">
                        <img src="assets/logo.png" class="filter invert brightness-0 object-contain w-full h-full">
                    </div>
                    <div>
                        <h4 class="font-bold text-sm tracking-wide">KUNETT Assistant</h4>
                        <p class="text-[10px] text-green-400 flex items-center gap-1.5 uppercase font-bold tracking-wider"><span class="w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse"></span> Online</p>
                    </div>
                </div>
                <button onclick="toggleChat()" class="text-white/70 hover:text-white transition-colors focus:outline-none">
                    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>
            
            <div id="chat-messages" class="p-4 h-64 overflow-y-auto bg-[#F8F9FA] flex flex-col gap-2">
                <div class="bg-white border border-brand-lightgray text-brand-black p-3 rounded-tr-xl rounded-bl-xl rounded-br-xl max-w-[85%] shadow-sm self-start text-[13px] leading-relaxed">
                    Hello! I'm the KUNETT virtual assistant. Need finish recommendations, custom profiles, or wholesale pricing? I can connect you directly to Sanjay.
                </div>
            </div>
            
            <div class="p-3 bg-white border-t border-brand-lightgray">
                <div id="chat-options" class="flex flex-wrap gap-1.5 transition-opacity">
                    <button onclick="handleBotOption('finishes')" class="text-[11px] font-medium bg-brand-offwhite border border-brand-lightgray hover:border-brand-gray px-3 py-1.5 rounded-full transition-colors text-left text-brand-black">🎨 Available Finishes?</button>
                    <button onclick="handleBotOption('wholesale')" class="text-[11px] font-medium bg-brand-offwhite border border-brand-lightgray hover:border-brand-gray px-3 py-1.5 rounded-full transition-colors text-left text-brand-black">📦 Wholesale & Export</button>
                    <button onclick="handleBotOption('catalogue')" class="text-[11px] font-medium bg-brand-offwhite border border-brand-lightgray hover:border-brand-gray px-3 py-1.5 rounded-full transition-colors text-left text-brand-black">📖 Get Catalogue</button>
                    <button onclick="handleBotOption('human')" class="text-[11px] font-bold bg-[#25D366] text-white hover:opacity-90 px-3 py-1.5 rounded-full transition-opacity text-left shadow-sm">💬 Chat on WhatsApp</button>
                </div>
            </div>
        </div>
        
        <button onclick="toggleChat()" id="chat-bubble" class="bg-brand-black text-white w-14 h-14 rounded-full shadow-2xl flex items-center justify-center hover:scale-105 transition-transform relative pointer-events-auto focus:outline-none">
            <span class="absolute -top-1 -right-1 flex h-4 w-4">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-4 w-4 bg-red-500 border-2 border-white"></span>
            </span>
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        </button>
    </div>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/919924637640?text=Hello%20KUNETT%20Hardware,%20I%20have%20an%20inquiry%20about%20your%20products." target="_blank" rel="noopener noreferrer" class="fixed bottom-6 left-6 md:bottom-8 md:left-8 bg-[#25D366] text-white p-4 rounded-full shadow-2xl hover:bg-[#1ebe57] hover:scale-110 transition-all duration-300 z-50 flex items-center justify-center group" aria-label="Chat with us on WhatsApp">
        <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.88-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
    </a>

    <!-- Client-Side Scripts -->
    <script>
        const WHATSAPP_NUMBER = "919924637640";
        const products = {products_json};
        let inquiryList = [];
        try {{
            const saved = localStorage.getItem('kunett_inquiry_list');
            if (saved) inquiryList = JSON.parse(saved);
        }} catch(e) {{}}

        let currentModalProduct = null;
        let selectedModalFinishes = [];
        let selectedModalSizes = [];

        function updateInquiryBadges() {{
            const badge = document.getElementById('inquiry-badge');
            const mobileBadge = document.getElementById('mobile-inquiry-badge');
            const count = inquiryList.length;
            if (count > 0) {{
                if (badge) {{ badge.textContent = count; badge.classList.remove('hidden'); }}
                if (mobileBadge) {{ mobileBadge.textContent = count; mobileBadge.classList.remove('hidden'); }}
            }} else {{
                if (badge) badge.classList.add('hidden');
                if (mobileBadge) mobileBadge.classList.add('hidden');
            }}
            try {{ localStorage.setItem('kunett_inquiry_list', JSON.stringify(inquiryList)); }} catch(e) {{}}
        }}

        function toggleMobileMenu() {{
            const menu = document.getElementById('mobile-menu');
            const backdrop = document.getElementById('mobile-backdrop');
            if (menu.classList.contains('translate-x-full')) {{
                menu.classList.remove('translate-x-full');
                if (backdrop) backdrop.classList.remove('opacity-0', 'pointer-events-none');
                document.body.style.overflow = 'hidden';
            }} else {{
                closeMobileMenu();
            }}
        }}

        function closeMobileMenu() {{
            const menu = document.getElementById('mobile-menu');
            const backdrop = document.getElementById('mobile-backdrop');
            if (menu && !menu.classList.contains('translate-x-full')) {{
                menu.classList.add('translate-x-full');
                if (backdrop) backdrop.classList.add('opacity-0', 'pointer-events-none');
                document.body.style.overflow = '';
            }}
        }}

        function openProductModal(code) {{
            const p = products.find(x => x.code === String(code));
            if (!p) return;
            currentModalProduct = p;
            selectedModalFinishes = [];
            selectedModalSizes = [];

            const modal = document.getElementById('product-modal');
            const content = document.getElementById('product-modal-content');
            const body = document.getElementById('modal-product-body');

            body.innerHTML = `
                <div class="flex flex-col md:flex-row gap-8 items-center">
                    <div class="w-full md:w-1/2 aspect-square bg-brand-offwhite rounded-2xl p-6 flex items-center justify-center">
                        <img src="${{p.image}}" class="max-w-full max-h-full object-contain mix-blend-multiply drop-shadow-md">
                    </div>
                    <div class="w-full md:w-1/2">
                        <span class="text-xs font-bold uppercase tracking-widest text-brand-gray">${{p.category}}</span>
                        <h3 class="font-serif text-3xl md:text-4xl text-brand-black mt-1 mb-3">Model ${{p.code}}</h3>
                        <p class="text-sm text-brand-gray leading-relaxed mb-6">${{p.description}}</p>
                        
                        <div class="mb-5">
                            <h5 class="text-xs font-bold uppercase tracking-widest text-brand-black mb-2.5">Select Finish</h5>
                            <div class="flex flex-wrap gap-2" id="modal-finish-options">
                                ${{p.finishes.map(f => `<button type="button" onclick="toggleModalFinish('${{f}}')" id="fin-btn-${{f.replace(/\s+/g, '_')}}" class="text-xs px-3 py-1.5 rounded-full border border-brand-lightgray hover:border-brand-black transition-colors font-medium">${{f}}</button>`).join('')}}
                            </div>
                        </div>

                        <div class="mb-6">
                            <h5 class="text-xs font-bold uppercase tracking-widest text-brand-black mb-2.5">Select Size</h5>
                            <div class="flex flex-wrap gap-2" id="modal-size-options">
                                ${{p.sizes.map(s => `<button type="button" onclick="toggleModalSize('${{s}}')" id="sz-btn-${{s.replace(/[^a-zA-Z0-9]/g, '_')}}" class="text-xs px-3 py-1.5 rounded-full border border-brand-lightgray hover:border-brand-black transition-colors font-medium">${{s}}</button>`).join('')}}
                            </div>
                        </div>

                        <div class="flex flex-col sm:flex-row gap-3">
                            <button type="button" onclick="addModalProductToInquiry()" id="modal-add-btn" class="bg-brand-black text-white px-6 py-3.5 rounded-full font-bold text-xs tracking-wide shadow-md hover:opacity-85 transition-opacity flex-1 text-center">
                                Add to Inquiry List
                            </button>
                            <a href="https://wa.me/${{WHATSAPP_NUMBER}}?text=Hello%20Sanjay,%20I%20am%20interested%20in%20KUNETT%20Model%20${{p.code}}%20(${{p.category}})." target="_blank" class="bg-[#25D366] text-white px-6 py-3.5 rounded-full font-bold text-xs tracking-wide shadow-md hover:opacity-90 transition-opacity flex items-center justify-center gap-1.5">
                                WhatsApp
                            </a>
                        </div>
                    </div>
                </div>
            `;

            modal.classList.add('active');
            setTimeout(() => {{
                content.classList.remove('scale-95', 'opacity-0');
                content.classList.add('scale-100', 'opacity-100');
            }}, 20);
        }}

        function closeProductModal() {{
            const modal = document.getElementById('product-modal');
            const content = document.getElementById('product-modal-content');
            if (content) {{
                content.classList.remove('scale-100', 'opacity-100');
                content.classList.add('scale-95', 'opacity-0');
            }}
            setTimeout(() => {{ if (modal) modal.classList.remove('active'); }}, 250);
        }}

        function toggleModalFinish(f) {{
            const idx = selectedModalFinishes.indexOf(f);
            if (idx > -1) selectedModalFinishes.splice(idx, 1);
            else selectedModalFinishes.push(f);
            const btn = document.getElementById('fin-btn-' + f.replace(/\s+/g, '_'));
            if (btn) {{
                if (selectedModalFinishes.includes(f)) btn.classList.add('bg-brand-black', 'text-white');
                else btn.classList.remove('bg-brand-black', 'text-white');
            }}
        }}

        function toggleModalSize(s) {{
            const idx = selectedModalSizes.indexOf(s);
            if (idx > -1) selectedModalSizes.splice(idx, 1);
            else selectedModalSizes.push(s);
            const btn = document.getElementById('sz-btn-' + s.replace(/[^a-zA-Z0-9]/g, '_'));
            if (btn) {{
                if (selectedModalSizes.includes(s)) btn.classList.add('bg-brand-black', 'text-white');
                else btn.classList.remove('bg-brand-black', 'text-white');
            }}
        }}

        function addModalProductToInquiry() {{
            if (!currentModalProduct) return;
            const btn = document.getElementById('modal-add-btn');
            if (selectedModalFinishes.length === 0 || selectedModalSizes.length === 0) {{
                btn.textContent = "Please pick Finish & Size";
                btn.classList.add('bg-red-500');
                setTimeout(() => {{
                    btn.textContent = "Add to Inquiry List";
                    btn.classList.remove('bg-red-500');
                }}, 2000);
                return;
            }}
            inquiryList.push({{
                product: currentModalProduct,
                finishes: [...selectedModalFinishes],
                sizes: [...selectedModalSizes]
            }});
            updateInquiryBadges();
            btn.textContent = "Added to List ✓";
            btn.classList.add('bg-[#25D366]');
            setTimeout(() => {{
                btn.textContent = "Add to Inquiry List";
                btn.classList.remove('bg-[#25D366]');
                closeProductModal();
            }}, 1200);
        }}

        function openInquiryModal() {{
            const modal = document.getElementById('inquiry-modal');
            const drawer = document.getElementById('inquiry-drawer-content');
            const container = document.getElementById('inquiry-list-items');
            if (inquiryList.length === 0) {{
                container.innerHTML = `<div class="text-center py-16 text-brand-gray text-sm">Your inquiry list is empty.<br>Browse the collection and add models you like!</div>`;
            }} else {{
                container.innerHTML = inquiryList.map((item, idx) => `
                    <div class="flex gap-4 p-3.5 bg-brand-offwhite rounded-xl relative border border-brand-lightgray">
                        <img src="${{item.product.image}}" class="w-16 h-16 object-contain mix-blend-multiply bg-white rounded p-1">
                        <div class="flex-grow">
                            <h5 class="font-bold text-sm">Model ${{item.product.code}}</h5>
                            <p class="text-xs text-brand-gray">${{item.product.category}}</p>
                            <p class="text-[11px] text-brand-black mt-1"><strong>Finishes:</strong> ${{item.finishes.join(', ') || 'Any'}}</p>
                            <p class="text-[11px] text-brand-black"><strong>Sizes:</strong> ${{item.sizes.join(', ') || 'Any'}}</p>
                        </div>
                        <button onclick="removeInquiryItem(${{idx}})" class="text-brand-gray hover:text-red-500 text-xs p-1">✕</button>
                    </div>
                `).join('');
            }}
            modal.classList.add('active');
        }}

        function closeInquiryModal() {{
            const modal = document.getElementById('inquiry-modal');
            if (modal) modal.classList.remove('active');
        }}

        function removeInquiryItem(idx) {{
            inquiryList.splice(idx, 1);
            updateInquiryBadges();
            openInquiryModal();
        }}

        function sendInquiryViaWhatsapp() {{
            if (inquiryList.length === 0) {{
                alert("Please add at least one model to your inquiry list.");
                return;
            }}
            let text = "Hello Sanjay, I would like to inquire about the following KUNETT hardware models:\\n\\n";
            inquiryList.forEach((item, i) => {{
                text += `${{i+1}}. Model ${{item.product.code}} (${{item.product.category}})\\n`;
                if (item.finishes.length) text += `   - Finishes: ${{item.finishes.join(', ')}}\\n`;
                if (item.sizes.length) text += `   - Sizes: ${{item.sizes.join(', ')}}\\n`;
                text += "\\n";
            }});
            text += "Please share availability, delivery time, and pricing.";
            window.open(`https://wa.me/${{WHATSAPP_NUMBER}}?text=${{encodeURIComponent(text)}}`, '_blank');
        }}

        function openCatalogueModal(e) {{
            if (e) e.preventDefault();
            const modal = document.getElementById('catalogue-modal');
            const content = document.getElementById('catalogue-modal-content');
            if (modal && content) {{
                modal.classList.add('catalogue-active');
                setTimeout(() => {{ content.classList.remove('scale-95', 'opacity-0'); content.classList.add('scale-100', 'opacity-100'); }}, 20);
            }}
        }}

        function closeCatalogueModal() {{
            const modal = document.getElementById('catalogue-modal');
            const content = document.getElementById('catalogue-modal-content');
            if (content) {{ content.classList.remove('scale-100', 'opacity-100'); content.classList.add('scale-95', 'opacity-0'); }}
            setTimeout(() => {{ if (modal) modal.classList.remove('catalogue-active'); }}, 250);
        }}

        // Lead form submit
        document.addEventListener('DOMContentLoaded', () => {{
            updateInquiryBadges();
            const form = document.getElementById('catalogueForm');
            if (form) {{
                form.addEventListener('submit', function(e) {{
                    e.preventDefault();
                    const btn = document.getElementById('catSubmitBtn');
                    const status = document.getElementById('catFormStatus');
                    btn.textContent = "Connecting to WhatsApp...";
                    btn.disabled = true;
                    const name = form.querySelector('[name="Name"]')?.value || '';
                    const phone = form.querySelector('[name="Phone"]')?.value || '';
                    const email = form.querySelector('[name="Email"]')?.value || '';
                    const waText = `*Catalogue Download Request*\\n*Name:* ${{name}}\\n*Phone:* ${{phone}}\\n*Email:* ${{email}}\\nPlease send me the KUNETT hardware digital catalogue.`;
                    window.open(`https://wa.me/${{WHATSAPP_NUMBER}}?text=${{encodeURIComponent(waText)}}`, '_blank');
                    status.textContent = "✅ Redirecting to WhatsApp catalogue download...";
                    status.classList.remove('hidden', 'text-red-600');
                    status.classList.add('text-[#25D366]');
                    form.reset();
                    btn.textContent = "Submit & Download";
                    btn.disabled = false;
                    setTimeout(closeCatalogueModal, 2500);
                }});
            }}
        }});

        // Preloader
        function hidePreloader() {{
            const p = document.getElementById('preloader');
            if (p && p.style.display !== 'none') {{
                p.style.opacity = '0';
                setTimeout(() => {{ p.style.display = 'none'; }}, 700);
            }}
        }}
        document.addEventListener('DOMContentLoaded', () => setTimeout(hidePreloader, 600));
        setTimeout(hidePreloader, 1800);

        // Robot
        let mouseX = -100, mouseY = -100, robotX = -100, robotY = -100;
        document.addEventListener('mousemove', e => {{
            mouseX = e.clientX; mouseY = e.clientY;
            const r = document.getElementById('cursor-robot');
            if (r) r.style.opacity = '1';
        }});
        function animRobot() {{
            const robot = document.getElementById('cursor-robot');
            robotX += (mouseX - robotX) * 0.08;
            robotY += (mouseY - robotY) * 0.08;
            if (robot) {{
                robot.style.transform = `translate(${{robotX + 20}}px, ${{robotY + 20}}px)`;
            }}
            requestAnimationFrame(animRobot);
        }}
        requestAnimationFrame(animRobot);

        // Chatbot UI
        function toggleChat() {{
            const win = document.getElementById('kunett-chat-window');
            if (win) win.classList.toggle('hidden');
        }}
        function handleBotOption(opt) {{
            const msgs = document.getElementById('chat-messages');
            if (opt === 'finishes') {{
                msgs.innerHTML += `<div class="bg-brand-black text-white p-2.5 rounded-xl text-xs self-end">Available finishes?</div>`;
                msgs.innerHTML += `<div class="bg-white border border-brand-lightgray p-2.5 rounded-xl text-xs self-start mt-1.5">We offer 8 electrochemical anodized finishes: Matte Black, Rose Gold, Champagne Gold, Antique Brass, SS Matt, and Grey. All are scratch- and corrosion-resistant.</div>`;
            }} else if (opt === 'wholesale') {{
                msgs.innerHTML += `<div class="bg-brand-black text-white p-2.5 rounded-xl text-xs self-end">Wholesale inquiry</div>`;
                msgs.innerHTML += `<div class="bg-white border border-brand-lightgray p-2.5 rounded-xl text-xs self-start mt-1.5">We supply bulk carton packaging across India and export to USA, Germany, and UAE. Direct factory supply eliminates intermediary markups.</div>`;
            }} else if (opt === 'catalogue') {{
                openCatalogueModal();
            }} else if (opt === 'human') {{
                window.open(`https://wa.me/${{WHATSAPP_NUMBER}}?text=Hello%20Sanjay,%20I%20am%20inquiring%20about%20KUNETT%20Hardware.`, '_blank');
            }}
            msgs.scrollTop = msgs.scrollHeight;
        }}
    </script>
</body>
</html>
"""

print("Helper renderers defined.")

# Category pages generation
all_category_configs = [
    {
        'filename': 'aluminium-handle-profile.html',
        'series': '300',
        'active_nav': 'nav-300',
        'name': 'Aluminium Handle Profile',
        'h1': 'Aluminium Handle Profile Manufacturer in Rajkot',
        'sub': 'Continuous J-Pull, G-Profile & Edge-Mounted Architectural Profiles for Modern Modular Kitchens & Luxury Wardrobes',
        'category': 'Cabinet Profile',
        'range': (301, 324),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'CP', 'Grey'],
        'sizes': ['6" To 36" (Custom continuous cuts up to 3 meters)'],
        'meta_title': 'Aluminium Handle Profile Manufacturer | J-Pull & G-Profile | KUNETT Hardware',
        'meta_desc': 'Rajkot’s leading manufacturer of solid aluminium handle profile systems. Continuous J-pull, G-profile, and edge-mount profiles for modular kitchens and wardrobe shutters. Direct factory prices.',
        'meta_keywords': 'aluminium handle profile, aluminium handle profile manufacturer, aluminium profile handles, J pull aluminium profile, G profile aluminium handle, edge handle profile, modular kitchen handle profile, Rajkot aluminium profile manufacturer, KUNETT hardware, Harikrushna Enterprise',
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
        'faqs': [
            ("What makes KUNETT solid aluminium knobs unique?", "Each knob in our 500 Series is CNC-milled from a solid aerospace billet of aluminium. The weight, tactile feel, chamfered bevels, and micro-knurled grip provide an unmistakably luxurious sensation."),
            ("Where are these knobs best installed?", "They are ideal for bathroom vanities, bedroom nightstands, office credenzas, custom dressers, and accent kitchen drawers.")
        ]
    }
]

# Generate each category page
for cfg in all_category_configs:
    prods = build_products(cfg['range'][0], cfg['range'][1], cfg['series'], cfg['category'], cfg['finishes'], cfg['sizes'])
    
    # Structured Data
    schema_graph = [
        {
            "@type": "WebSite",
            "@id": "https://kunetthardware.com/#website",
            "url": "https://kunetthardware.com/",
            "name": "KUNETT Hardware - Aluminium Handles & Profiles",
            "publisher": {"@id": "https://kunetthardware.com/#organization"}
        },
        {
            "@type": ["LocalBusiness", "HomeGoodsStore"],
            "@id": "https://kunetthardware.com/#organization",
            "name": "Harikrushna Enterprise",
            "alternateName": ["KUNETT Hardware", "KUNETT"],
            "image": "https://kunetthardware.com/assets/favicon-512x512.png",
            "logo": "https://kunetthardware.com/assets/favicon-512x512.png",
            "telephone": "+919924637640",
            "url": "https://kunetthardware.com",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Rajkot",
                "addressLocality": "Rajkot",
                "addressRegion": "Gujarat",
                "postalCode": "360002",
                "addressCountry": "IN"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "reviewCount": "48"
            }
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"https://kunetthardware.com/{cfg['filename']}#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://kunetthardware.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": cfg['name'],
                    "item": f"https://kunetthardware.com/{cfg['filename']}"
                }
            ]
        },
        {
            "@type": "CollectionPage",
            "@id": f"https://kunetthardware.com/{cfg['filename']}#collection",
            "name": cfg['h1'],
            "description": cfg['meta_desc'],
            "mainEntity": {
                "@type": "ItemList",
                "name": f"KUNETT {cfg['name']} Range",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "name": f"KUNETT Model {p['code']} {p['category']}",
                        "url": f"https://kunetthardware.com/{cfg['filename']}#model-{p['code']}"
                    } for idx, p in enumerate(prods[:15])
                ]
            }
        },
        {
            "@type": "FAQPage",
            "@id": f"https://kunetthardware.com/{cfg['filename']}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": a
                    }
                } for q, a in cfg['faqs']
            ]
        }
    ]

    schema_json_str = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2)

    # Product Grid HTML
    grid_cards = []
    for p in prods:
        swatches = "".join([f'<div class="w-3 h-3 rounded-full shadow-sm border border-gray-300" style="{get_color_style(f)}" title="{f}"></div>' for f in p['finishes']])
        card = f"""
            <div id="model-{p['code']}" onclick="openProductModal('{p['code']}')" class="product-card flex flex-col group cursor-pointer text-left bg-white p-4 rounded-2xl border border-brand-lightgray hover:border-brand-black hover:shadow-md transition-all">
                <div class="bg-brand-offwhite aspect-square flex items-center justify-center rounded-xl p-4 mb-3 relative overflow-hidden">
                    <img src="{p['image']}" alt="KUNETT Model {p['code']} {p['category']} - Solid Aluminium Hardware Manufacturer Rajkot" loading="lazy" class="product-img object-contain h-full w-full group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute bottom-2 right-2 bg-brand-black text-white rounded-full p-1.5 shadow opacity-0 group-hover:opacity-100 transition-opacity">
                        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
                    </div>
                </div>
                <div class="flex flex-col justify-between items-start flex-grow">
                    <div class="flex items-center justify-between w-full mb-1">
                        <h4 class="font-bold text-base text-brand-black">Model {p['code']}</h4>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-brand-gray">{p['series']} Series</span>
                    </div>
                    <p class="text-xs text-brand-gray mb-3 line-clamp-2">{p['description']}</p>
                    <div class="flex items-center justify-between w-full pt-2 border-t border-brand-lightgray/50 mt-auto">
                        <div class="flex gap-1">{swatches}</div>
                        <span class="text-[11px] font-bold text-brand-black group-hover:underline">View Specs &rarr;</span>
                    </div>
                </div>
            </div>
        """
        grid_cards.append(card)
    grid_html = "\n".join(grid_cards)

    # FAQs HTML
    faq_items = []
    for q, a in cfg['faqs']:
        faq_items.append(f"""
            <div class="bg-white p-6 rounded-2xl border border-brand-lightgray shadow-sm">
                <h3 class="font-bold text-base md:text-lg text-brand-black mb-2 flex items-start gap-3">
                    <span class="text-brand-gray font-serif font-bold text-lg">Q.</span> {q}
                </h3>
                <p class="text-sm text-brand-gray leading-relaxed pl-7">{a}</p>
            </div>
        """)
    faqs_html = "\n".join(faq_items)

    # Full Page Assembly
    canonical_url = f"https://kunetthardware.com/{cfg['filename']}"
    page_html = render_head(cfg['meta_title'], cfg['meta_desc'], cfg['meta_keywords'], canonical_url, schema_json_str)
    page_html += render_navbar(cfg['active_nav'])
    
    page_html += f"""
    <!-- Breadcrumb Bar -->
    <div class="bg-white border-b border-brand-lightgray py-3 px-4 md:px-8">
        <div class="max-w-7xl mx-auto flex items-center gap-2 text-xs text-brand-gray">
            <a href="/" class="hover:text-brand-black transition-colors">Home</a>
            <span>/</span>
            <span class="text-brand-black font-semibold">{cfg['name']}</span>
        </div>
    </div>

    <!-- Main Content Area -->
    <main class="max-w-7xl mx-auto px-4 md:px-6 py-10 md:py-16">
        
        <!-- Hero Header -->
        <header class="text-center md:text-left mb-12 pb-8 border-b border-brand-lightgray">
            <div class="flex flex-wrap items-center gap-2 mb-3 justify-center md:justify-start">
                <span class="text-[11px] font-bold uppercase tracking-widest bg-brand-black text-white px-3 py-1 rounded-full">{cfg['series']} Series Collection</span>
                <span class="text-[11px] font-bold uppercase tracking-widest bg-brand-offwhite text-brand-gray border border-brand-lightgray px-3 py-1 rounded-full">Rajkot Direct Factory Supply</span>
            </div>
            <h1 class="font-serif text-3xl sm:text-5xl md:text-6xl text-brand-black mb-4 leading-tight">{cfg['h1']}</h1>
            <p class="text-brand-gray text-base md:text-xl max-w-3xl leading-relaxed mb-6">{cfg['sub']}</p>
            
            <div class="flex flex-wrap gap-4 items-center justify-center md:justify-start">
                <a href="#collection-grid" class="bg-brand-black text-white px-8 py-3.5 rounded-full font-bold text-xs tracking-wider uppercase hover:opacity-85 transition-opacity shadow-sm">
                    Browse {len(prods)}+ Models
                </a>
                <a href="https://wa.me/919924637640?text=Hello%20Sanjay,%20I%20am%20inquiring%20about%20KUNETT%20{cfg['name']}%20models." target="_blank" class="bg-[#25D366] text-white px-8 py-3.5 rounded-full font-bold text-xs tracking-wider uppercase hover:opacity-90 transition-opacity shadow-sm flex items-center gap-2">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.192 1.604 6.015L.302 24l6.108-1.6c1.764.957 3.754 1.464 5.62 1.464 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm3.834 17.203c-.161.455-.93 .853-1.312.894-.383.042-.87.126-2.505-.55-1.974-.816-3.238-2.825-3.338-2.961-.101-.136-.798-1.061-.798-2.023 0-.962.5-1.436.682-1.638.181-.202.392-.253.523-.253.131 0 .262 0 .373.01.111.011.262-.042.413.323.151.364.514 1.253.554 1.344.041.091.071.192.01.293-.061.101-.091.162-.181.263-.091.101-.192.222-.272.303-.091.091-.192.192-.081.384.111.192.494.818 1.059 1.323.731.653 1.343.853 1.534.944.192.091.303.081.413-.041.111-.121.484-.565.615-.757.131-.192.262-.162.434-.091.171.071 1.089.515 1.27.606.181.091.303.136.343.212.041.071.041.424-.12.879z"/></svg>
                    WhatsApp Sanjay (+91 99246 37640)
                </a>
                <a href="#" onclick="openCatalogueModal(event)" class="border border-brand-black text-brand-black px-6 py-3.5 rounded-full font-bold text-xs tracking-wider uppercase hover:bg-brand-black hover:text-white transition-all">
                    Download Catalogue
                </a>
            </div>
        </header>

        <!-- Category Overview & Architectural Value Section -->
        <section class="mb-14">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6 bg-white p-6 md:p-8 rounded-3xl border border-brand-lightgray shadow-sm">
                <div>
                    <span class="text-xs font-bold uppercase tracking-widest text-brand-gray block mb-1">Material Integrity</span>
                    <h3 class="font-bold text-base text-brand-black mb-1">100% Solid Aluminium</h3>
                    <p class="text-xs text-brand-gray leading-relaxed">Virgin 6063 aerospace alloy. Eliminates brittle zinc breakage and ensures heavy ergonomic weight.</p>
                </div>
                <div>
                    <span class="text-xs font-bold uppercase tracking-widest text-brand-gray block mb-1">Surface Finish</span>
                    <h3 class="font-bold text-base text-brand-black mb-1">Micron Anodized</h3>
                    <p class="text-xs text-brand-gray leading-relaxed">Matte Black, Rose Gold, Champagne, SS Matt. Electrochemical color that will never peel or rust.</p>
                </div>
                <div>
                    <span class="text-xs font-bold uppercase tracking-widest text-brand-gray block mb-1">Custom Sizes</span>
                    <h3 class="font-bold text-base text-brand-black mb-1">Custom-Cut Lengths</h3>
                    <p class="text-xs text-brand-gray leading-relaxed">Standard 6" to 36" cuts or full continuous profiles up to 3 meters for modular factory use.</p>
                </div>
                <div>
                    <span class="text-xs font-bold uppercase tracking-widest text-brand-gray block mb-1">Direct Supply</span>
                    <h3 class="font-bold text-base text-brand-black mb-1">Factory Direct Pricing</h3>
                    <p class="text-xs text-brand-gray leading-relaxed">No intermediary distributor commissions. Direct shipping across Mumbai, Delhi, Bengaluru, and pan-India.</p>
                </div>
            </div>
        </section>

        <!-- Product Grid Header -->
        <section id="collection-grid" class="mb-16">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8 pb-4 border-b border-brand-lightgray">
                <div>
                    <h2 class="font-serif text-2xl md:text-3xl text-brand-black">{cfg['name']} Models ({len(prods)} Items)</h2>
                    <p class="text-xs md:text-sm text-brand-gray">Click any model below to view high-res specifications, available finishes, and add to inquiry list.</p>
                </div>
                <div class="text-xs font-bold uppercase tracking-wider text-brand-gray">
                    Showing 1 – {len(prods)} of {len(prods)} models
                </div>
            </div>

            <!-- Products Grid -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 md:gap-6">
                {grid_html}
            </div>
        </section>

        <!-- Technical FAQs Section -->
        <section class="mb-16 pt-10 border-t border-brand-lightgray">
            <div class="text-center max-w-2xl mx-auto mb-10">
                <span class="text-xs font-bold uppercase tracking-widest text-brand-gray">Frequently Asked Questions</span>
                <h2 class="font-serif text-3xl md:text-4xl text-brand-black mt-2 mb-3">Frequently Asked Questions About {cfg['name']}</h2>
                <p class="text-sm text-brand-gray">Everything you need to know about specifications, installation, finishes, and ordering from KUNETT.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                {faqs_html}
            </div>
        </section>

        <!-- Direct WhatsApp CTA Banner -->
        <section class="bg-brand-black text-white p-8 md:p-12 rounded-3xl flex flex-col md:flex-row items-center justify-between gap-8 shadow-xl">
            <div class="max-w-xl text-center md:text-left">
                <span class="text-xs font-bold uppercase tracking-widest text-green-400 block mb-2">Direct Manufacturer Assistance</span>
                <h3 class="font-serif text-2xl md:text-4xl font-bold mb-3">Need Custom Lengths or Finish Matching?</h3>
                <p class="text-sm text-gray-300 leading-relaxed">Send your architectural drawings, carpenter cut-lists, or kitchen render directly to Sanjay Patel on WhatsApp for instant technical advice and wholesale quotations.</p>
            </div>
            <a href="https://wa.me/919924637640?text=Hello%20Sanjay,%20I%20am%20looking%20for%20guidance%20on%20KUNETT%20{cfg['name']}." target="_blank" class="bg-[#25D366] text-white px-8 py-4 rounded-full font-bold text-sm tracking-wide shadow-lg hover:opacity-90 transition-opacity flex items-center gap-2 flex-shrink-0">
                <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.192 1.604 6.015L.302 24l6.108-1.6c1.764.957 3.754 1.464 5.62 1.464 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm3.834 17.203c-.161.455-.93 .853-1.312.894-.383.042-.87.126-2.505-.55-1.974-.816-3.238-2.825-3.338-2.961-.101-.136-.798-1.061-.798-2.023 0-.962.5-1.436.682-1.638.181-.202.392-.253.523-.253.131 0 .262 0 .373.01.111.011.262-.042.413.323.151.364.514 1.253.554 1.344.041.091.071.192.01.293-.061.101-.091.162-.181.263-.091.101-.192.222-.272.303-.091.091-.192.192-.081.384.111.192.494.818 1.059 1.323.731.653 1.343.853 1.534.944.192.091.303.081.413-.041.111-.121.484-.565.615-.757.131-.192.262-.162.434-.091.171.071 1.089.515 1.27.606.181.091.303.136.343.212.041.071.041.424-.12.879z"/></svg>
                Connect on WhatsApp (+91 99246 37640)
            </a>
        </section>

    </main>
    """
    page_html += render_footer()
    page_html += render_modals_and_scripts(json.dumps(prods))

    with open(cfg['filename'], 'w', encoding='utf-8') as out_f:
        out_f.write(page_html)
    print(f"Generated: {cfg['filename']} ({len(prods)} products pre-rendered)")

print("All category pages generated.")

# 1. Generate our-process.html
process_schema = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebSite",
            "@id": "https://kunetthardware.com/#website",
            "url": "https://kunetthardware.com/",
            "name": "KUNETT Hardware - Manufacturing Process"
        },
        {
            "@type": ["LocalBusiness", "Manufacturer"],
            "@id": "https://kunetthardware.com/#organization",
            "name": "Harikrushna Enterprise",
            "alternateName": "KUNETT Hardware",
            "telephone": "+919924637640",
            "url": "https://kunetthardware.com",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Rajkot",
                "addressLocality": "Rajkot",
                "addressRegion": "Gujarat",
                "postalCode": "360002",
                "addressCountry": "IN"
            }
        },
        {
            "@type": "BreadcrumbList",
            "@id": "https://kunetthardware.com/our-process.html#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://kunetthardware.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Manufacturing Process",
                    "item": "https://kunetthardware.com/our-process.html"
                }
            ]
        }
    ]
}, indent=2)

process_html = render_head(
    "Aluminium Handle Manufacturing Process in Rajkot | KUNETT Hardware",
    "Explore how KUNETT manufactures solid aluminium handles in Rajkot: aerospace alloy extrusion, 5-axis VMC machining, multi-stage buffing, and electrochemical anodizing.",
    "aluminium handle manufacturing process, VMC machining Rajkot, aluminium anodizing factory, hardware manufacturing process, Harikrushna Enterprise",
    "https://kunetthardware.com/our-process.html",
    process_schema
)
process_html += render_navbar('nav-process')
process_html += """
<!-- Breadcrumb Bar -->
<div class="bg-white border-b border-brand-lightgray py-3 px-4 md:px-8">
    <div class="max-w-7xl mx-auto flex items-center gap-2 text-xs text-brand-gray">
        <a href="/" class="hover:text-brand-black transition-colors">Home</a>
        <span>/</span>
        <span class="text-brand-black font-semibold">Our Process</span>
    </div>
</div>

<main class="max-w-7xl mx-auto px-4 md:px-6 py-10 md:py-16">
    <div class="max-w-3xl mx-auto text-center mb-16">
        <span class="text-xs font-bold uppercase tracking-widest text-brand-gray block mb-2">Manufacturing Excellence</span>
        <h1 class="font-serif text-4xl md:text-6xl text-brand-black mb-6">Our 4-Stage Manufacturing Cycle</h1>
        <p class="text-brand-gray text-base md:text-lg leading-relaxed">
            From raw virgin aluminium alloy billets to high-precision VMC machining and micron-level electrochemical anodizing in Rajkot, Gujarat. Here is how we ensure lifelong durability and flawless ergonomics.
        </p>
    </div>

    <!-- Step 1 -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center mb-24">
        <div class="bg-brand-pink/30 aspect-[4/3] rounded-3xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
            <img src="assets/process_aluminium.jpg" alt="Precision Extrusion & Billet Engineering Rajkot" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
        </div>
        <div>
            <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">1</div>
            <h2 class="font-serif text-3xl md:text-4xl text-brand-black mb-4">Extrusion & Die Engineering</h2>
            <p class="text-brand-gray leading-relaxed mb-4">The manufacturing cycle begins with raw, aerospace-grade solid aluminium. Custom extrusion dies are engineered to match the exact architectural specifications of our cabinet handles and profiles.</p>
            <p class="text-brand-gray leading-relaxed">The raw aluminium is heated and pushed through precision dies—forming the foundational, continuous profile with immense structural integrity. This completely eliminates the hollow, fragile feel found in cheap zinc-alloy alternatives.</p>
        </div>
    </div>

    <!-- Step 2 -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center mb-24">
        <div class="order-1 md:order-2 bg-brand-pink/30 aspect-[4/3] rounded-3xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
            <img src="assets/process_vmc.jpg" alt="5-Axis VMC Machining Center Rajkot" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
        </div>
        <div class="order-2 md:order-1">
            <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">2</div>
            <h2 class="font-serif text-3xl md:text-4xl text-brand-black mb-4">Blade Cutting & 5-Axis VMC Machining</h2>
            <p class="text-brand-gray leading-relaxed mb-4">Once profiles are extruded, high-speed automated blades slice the solid aluminium into precise lengths for wardrobes, kitchens, and cabinets.</p>
            <p class="text-brand-gray leading-relaxed">The cut pieces are mounted into our state-of-the-art 5-Axis Vertical Machining Centers (VMC). These computer-controlled machines carve ergonomic curves, mounting holes, and fine chamfers with microscopic accuracy.</p>
        </div>
    </div>

    <!-- Step 3 -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center mb-24">
        <div class="bg-brand-offwhite aspect-[4/3] rounded-3xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
            <img src="assets/process_anodizing.jpg" alt="Buffing and Electrochemical Anodizing Tanks" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
        </div>
        <div>
            <div class="w-12 h-12 bg-brand-black text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">3</div>
            <h2 class="font-serif text-3xl md:text-4xl text-brand-black mb-4">Hand Buffing & Electrochemical Anodizing</h2>
            <p class="text-brand-gray leading-relaxed mb-4">Every milled handle undergoes multi-stage hand buffing to remove micro-imperfections and yield a silky tactile texture.</p>
            <p class="text-brand-gray leading-relaxed">Next, hardware enters electrochemical anodizing baths. Unlike spray paint, anodizing physically alters the surface layer of the aluminium, locking in Matte Black, Rose Gold, Champagne, and Antique finishes that never peel, rust, or tarnish.</p>
        </div>
    </div>

    <!-- Step 4 -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center mb-24">
        <div class="order-1 md:order-2 bg-brand-offwhite aspect-[4/3] rounded-3xl flex items-center justify-center overflow-hidden drop-shadow-xl border border-brand-lightgray">
            <img src="assets/process_packaging.jpg" alt="Quality Inspection & Global Export Packaging" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">
        </div>
        <div class="order-2 md:order-1">
            <div class="w-12 h-12 bg-[#25D366] text-white rounded-full flex justify-center items-center font-serif text-xl mb-6 shadow-md">4</div>
            <h2 class="font-serif text-3xl md:text-4xl text-brand-black mb-4">Quality Inspection & Factory Dispatch</h2>
            <p class="text-brand-gray leading-relaxed mb-4">Each handle is individually inspected under high-intensity lighting for color consistency, edge alignment, and surface smoothness.</p>
            <p class="text-brand-gray leading-relaxed">Approved hardware is packed in scratch-proof wholesale export cartons. Whether delivering to a homeowner in Mumbai or an export container heading to Germany or the USA, hardware arrives pristine and ready to install.</p>
        </div>
    </div>
</main>
"""
process_html += render_footer()
process_html += render_modals_and_scripts("[]")
with open('our-process.html', 'w', encoding='utf-8') as out_f:
    out_f.write(process_html)
print("Generated: our-process.html")


# 2. Generate contact.html
contact_schema = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebSite",
            "@id": "https://kunetthardware.com/#website",
            "url": "https://kunetthardware.com/",
            "name": "KUNETT Hardware - Contact"
        },
        {
            "@type": ["LocalBusiness", "HomeGoodsStore"],
            "@id": "https://kunetthardware.com/#organization",
            "name": "Harikrushna Enterprise",
            "alternateName": "KUNETT Hardware",
            "telephone": "+919924637640",
            "email": "support@kunetthardware.com",
            "url": "https://kunetthardware.com",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Rajkot",
                "addressLocality": "Rajkot",
                "addressRegion": "Gujarat",
                "postalCode": "360002",
                "addressCountry": "IN"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 22.239264,
                "longitude": 70.803659
            }
        },
        {
            "@type": "ContactPage",
            "@id": "https://kunetthardware.com/contact.html#webpage",
            "name": "Contact KUNETT Hardware",
            "description": "Contact KUNETT Hardware in Rajkot for inquiries, custom architectural orders, and dealer partnerships."
        }
    ]
}, indent=2)

contact_html = render_head(
    "Contact KUNETT Hardware | Factory in Rajkot, Gujarat | Harikrushna Enterprise",
    "Contact KUNETT Hardware (Harikrushna Enterprise) in Rajkot for direct factory inquiries, custom handle profile orders, and dealership opportunities. WhatsApp: +91 99246 37640.",
    "contact KUNETT hardware, Harikrushna Enterprise Rajkot phone, aluminium handles supplier contact, hardware factory Rajkot, Sanjay Patel contact",
    "https://kunetthardware.com/contact.html",
    contact_schema
)
contact_html += render_navbar('nav-contact')
contact_html += """
<!-- Breadcrumb Bar -->
<div class="bg-white border-b border-brand-lightgray py-3 px-4 md:px-8">
    <div class="max-w-7xl mx-auto flex items-center gap-2 text-xs text-brand-gray">
        <a href="/" class="hover:text-brand-black transition-colors">Home</a>
        <span>/</span>
        <span class="text-brand-black font-semibold">Contact Us</span>
    </div>
</div>

<main class="max-w-7xl mx-auto px-4 md:px-6 py-10 md:py-16">
    <div class="max-w-3xl mx-auto text-center mb-16">
        <p class="text-xs font-bold uppercase tracking-widest text-brand-gray mb-2">Get in Touch</p>
        <h1 class="font-serif text-4xl md:text-6xl text-brand-black mb-4">Contact KUNETT Hardware</h1>
        <p class="text-brand-gray text-base md:text-lg max-w-xl mx-auto">We'd love to hear from you. Inquire about hardware models, request custom specifications, or visit our manufacturing showroom in Rajkot.</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20">
        <!-- Left: Form -->
        <div class="bg-white p-8 md:p-10 rounded-3xl border border-brand-lightgray shadow-sm">
            <h3 class="font-serif text-2xl md:text-3xl text-brand-black mb-6">Send an Inquiry</h3>
            <form id="contactForm" class="space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-brand-black uppercase tracking-widest mb-2">Full Name *</label>
                        <input type="text" name="Name" required class="w-full border border-brand-lightgray p-4 rounded-xl bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="John Doe">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-brand-black uppercase tracking-widest mb-2">Email Address *</label>
                        <input type="email" name="Email" required class="w-full border border-brand-lightgray p-4 rounded-xl bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="john@example.com">
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-brand-black uppercase tracking-widest mb-2">Phone Number</label>
                        <input type="tel" name="Phone" class="w-full border border-brand-lightgray p-4 rounded-xl bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="+91 99246 37640">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-brand-black uppercase tracking-widest mb-2">Subject</label>
                        <select name="Subject" class="w-full border border-brand-lightgray p-4 rounded-xl bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors appearance-none text-sm">
                            <option>Aluminium Handle Profile Inquiry</option>
                            <option>Solid Aluminium Handles (200 Series)</option>
                            <option>Counsil Handles (400 Series)</option>
                            <option>Sliding Wardrobe Handles</option>
                            <option>Bulk / Wholesale Factory Order</option>
                            <option>International Export & Shipping</option>
                        </select>
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold text-brand-black uppercase tracking-widest mb-2">Message *</label>
                    <textarea name="Message" rows="5" required class="w-full border border-brand-lightgray p-4 rounded-xl bg-brand-offwhite focus:outline-none focus:border-brand-black transition-colors text-sm" placeholder="Describe the models, sizes, or finishes you are interested in..."></textarea>
                </div>
                <button type="submit" id="submitBtn" class="btn-primary w-full py-4 rounded-full font-bold text-sm tracking-wide shadow-lg hover:opacity-90 transition-opacity">
                    Send Message via WhatsApp
                </button>
                <div id="formStatus" class="hidden text-center text-sm font-bold mt-4 p-4 rounded bg-brand-offwhite border border-brand-lightgray"></div>
            </form>
        </div>
        
        <!-- Right: Location Details & Map -->
        <div class="flex flex-col">
            <h3 class="font-serif text-2xl md:text-3xl text-brand-black mb-6">Manufacturing Showroom</h3>
            
            <div class="bg-white p-6 md:p-8 rounded-3xl border border-brand-lightgray mb-8 shadow-sm">
                <h4 class="font-bold text-base uppercase tracking-widest text-brand-black mb-2">Harikrushna Enterprise</h4>
                <p class="text-brand-gray text-sm leading-relaxed mb-6">
                    Official Manufacturers of KUNETT Hardware<br>
                    <a href="https://maps.app.goo.gl/EMsseMvKHpNqxPVh9" target="_blank" rel="noopener noreferrer" class="hover:text-brand-gray transition-colors font-bold text-brand-black">Rajkot, Gujarat, India</a>
                </p>
                <div class="flex flex-col gap-4 text-sm">
                    <a href="https://wa.me/919924637640" target="_blank" class="flex items-center gap-3 text-brand-black hover:text-[#25D366] transition-colors font-medium">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.192 1.604 6.015L.302 24l6.108-1.6c1.764.957 3.754 1.464 5.62 1.464 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm3.834 17.203c-.161.455-.93 .853-1.312.894-.383.042-.87.126-2.505-.55-1.974-.816-3.238-2.825-3.338-2.961-.101-.136-.798-1.061-.798-2.023 0-.962.5-1.436.682-1.638.181-.202.392-.253.523-.253.131 0 .262 0 .373.01.111.011.262-.042.413.323.151.364.514 1.253.554 1.344.041.091.071.192.01.293-.061.101-.091.162-.181.263-.091.101-.192.222-.272.303-.091.091-.192.192-.081.384.111.192.494.818 1.059 1.323.731.653 1.343.853 1.534.944.192.091.303.081.413-.041.111-.121.484-.565.615-.757.131-.192.262-.162.434-.091.171.071 1.089.515 1.27.606.181.091.303.136.343.212.041.071.041.424-.12.879z"/></svg>
                        WhatsApp Sanjay Patel (+91 99246 37640)
                    </a>
                    <a href="mailto:support@kunetthardware.com" class="flex items-center gap-3 text-brand-black hover:text-brand-gray transition-colors font-medium">
                        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg>
                        support@kunetthardware.com
                    </a>
                    <a href="https://maps.app.goo.gl/EMsseMvKHpNqxPVh9" target="_blank" class="flex items-center gap-3 text-brand-black hover:text-blue-600 transition-colors font-medium">
                        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                        Open in Google Maps ↗
                    </a>
                </div>
            </div>
            
            <div class="w-full flex-grow min-h-[300px] rounded-3xl overflow-hidden border border-brand-lightgray shadow-sm">
                <iframe src="https://maps.google.com/maps?q=22.2392638,70.8036592&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </div>
</main>
"""
contact_html += render_footer()
contact_html += render_modals_and_scripts("[]")
with open('contact.html', 'w', encoding='utf-8') as out_f:
    out_f.write(contact_html)
print("Generated: contact.html")

