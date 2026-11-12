#!/usr/bin/env python3
"""
build_multipage_seo.py
Generates dedicated, high-ranking static HTML pages for KUNETT Hardware.
Solves the SPA single-page technical limitation by giving Google 8 indexable,
deeply optimized HTML documents with full structured schema, pre-rendered catalogs,
and category-specific content.
"""

import os
import json
import re

# Load base index.html
with open('index.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

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

all_series = {
    '200': {
        'slug': 'aluminium-handles.html',
        'series': '200',
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
    '300': {
        'slug': 'aluminium-handle-profile.html',
        'series': '300',
        'name': 'Aluminium Handle Profile',
        'h1': 'Aluminium Handle Profile Systems Manufacturer in Rajkot',
        'sub': 'Edge-Mounted Architectural J-Pull & G-Profile Systems for Seamless Handle-Less Modular Kitchens & Wardrobes',
        'category': 'Cabinet Profile',
        'range': (301, 324),
        'finishes': ['Black', 'R Gold', 'Gold', 'SS Matt', 'CP', 'Grey'],
        'sizes': ['6" To 36" (Custom cuts up to 3 meters)'],
        'meta_title': 'Aluminium Handle Profile Manufacturer | J-Pull & G-Profile | KUNETT Hardware',
        'meta_desc': 'Rajkot’s premier manufacturer of solid aluminium handle profile systems. Continuous J-pull, G-profile, and edge-mount profiles for modular kitchens and wardrobe shutters. Direct factory prices.',
        'meta_keywords': 'aluminium handle profile, aluminium handle profile manufacturer, aluminium profile handles, J pull aluminium profile, G profile aluminium handle, edge handle profile, modular kitchen handle profile, Rajkot aluminium profile manufacturer, KUNETT hardware, Harikrushna Enterprise',
        'faqs': [
            ("What is an aluminium handle profile?", "An aluminium handle profile is an edge-mounted continuous hardware extrusion that clips or slots directly onto the top or edge of modular cabinet shutters and wardrobe doors. It creates a modern, sleek handle-less aesthetic with a comfortable finger recess."),
            ("What is the difference between J-Profile and G-Profile handles?", "A J-profile handle wraps over the top edge of a drawer shutter with a subtle downward curve, ideal for top kitchen drawers. A G-profile (or Gola profile) sits horizontally or vertically between cabinet shutters, allowing your fingers to hook in from behind for a completely flush, ultra-minimal look."),
            ("What lengths are available for KUNETT aluminium handle profiles?", "We supply standard cut sizes from 6\" to 36\" for modular drawers, as well as full continuous 3-meter (10 ft) profile lengths for carpenters, interior contractors, and factory fabricators."),
            ("Will the finish on aluminium profile handles wear off with daily kitchen use?", "Never. KUNETT profiles undergo multi-tank electrochemical anodizing, not spray painting. The color is integrated into the molecular surface of the aluminium, creating a scratch-resistant, stain-resistant, and grease-proof barrier designed for intensive kitchen environments.")
        ]
    },
    '400': {
        'slug': 'wardrobe-counsil-handles.html',
        'series': '400',
        'name': 'Counsil Handles',
        'h1': 'Aluminium Counsil Handles Manufacturer in Rajkot',
        'sub': 'Substantive Concealed Solid Aluminium Handles Engineered for Heavy Wardrobe Shutters & Pantry Cabinets',
        'category': 'Counsil Handle',
        'range': (401, 418),
        'finishes': ['CP', 'Black', 'R Gold', 'Gold', 'SS Matt'],
        'sizes': ['4"', '6"', '8"', '10"', '12"'],
        'meta_title': 'Aluminium Counsil Handles Manufacturer | Concealed Wardrobe Pulls | KUNETT Hardware',
        'meta_desc': 'Solid aluminium counsil handles & concealed shutter pulls manufactured in Rajkot. Deep ergonomic finger recess engineered for heavy modular wardrobe and pantry doors. Factory direct rates.',
        'meta_keywords': 'counsil handles, aluminium counsil handles, concealed wardrobe handles, flush counsil handle, concealed handles for wardrobe, Rajkot counsil handle manufacturer, KUNETT hardware',
        'faqs': [
            ("What is a counsil handle?", "A counsil handle is a semi-concealed architectural pull that features a deep inner cavity and a wide backplate. It is recessed into the woodwork or edge-mounted to provide maximum leverage when opening heavy wardrobe shutters and tall pantry doors."),
            ("What sizes are available in the 400 Series Counsil Handles?", "We manufacture Model 401 through 418 in standard lengths of 4\", 6\", 8\", 10\", and 12\". Custom project sizes can also be milled using our 5-axis VMC machining centers in Rajkot."),
            ("Why choose aluminium counsil handles over zinc or plastic?", "Solid aluminium counsil handles provide uncompromising rigidity under heavy pulling force. They will not bend, crack, or loosen over time, ensuring a luxury feel throughout decades of daily wardrobe use.")
        ]
    },
    '450': {
        'slug': 'sliding-wardrobe-handles.html',
        'series': '450',
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
    '500': {
        'slug': 'cabinet-knobs.html',
        'series': '500',
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
}

print("Loaded all series metadata.")
