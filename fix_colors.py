import re

with open("index.html", "r") as f:
    content = f.read()

old_color_logic = """        function getColorStyle(color) {
            const map = {
                'Black': 'background-color: #1a1a1a;',
                'Rose Gold': 'background: linear-gradient(135deg, #b76e79 0%, #e0bfb8 100%);',
                'Matte Gold': 'background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 100%);',
                'Gold': 'background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);',
                'Silver': 'background: linear-gradient(135deg, #C0C0C0 0%, #E8E8E8 100%);',
                'Champagne': 'background: linear-gradient(135deg, #F7E7CE 0%, #FFE4C4 100%);'
            };
            return map[color] || 'background-color: #cccccc;';
        }"""

new_color_logic = """        function getColorStyle(color) {
            const map = {
                'Black': 'background-color: #1a1a1a;',
                'R Gold': 'background: linear-gradient(135deg, #b76e79 0%, #e0bfb8 100%);',
                'Gold': 'background: linear-gradient(135deg, #FFD700 0%, #DAA520 100%);',
                'SS Matt': 'background: linear-gradient(135deg, #E0E0E0 0%, #9E9E9E 100%);',
                'Antique': 'background: linear-gradient(135deg, #8B7355 0%, #D2B48C 100%);',
                'Grey': 'background-color: #757575;',
                'CP': 'background: linear-gradient(135deg, #FFFFFF 0%, #E0E0E0 100%);'
            };
            return map[color] || 'background-color: #cccccc;';
        }"""

content = content.replace(old_color_logic, new_color_logic)

with open("index.html", "w") as f:
    f.write(content)

print("Color logic fixed.")
