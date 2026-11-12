import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update Hero Section text
hero_pattern = r'Premium aluminium hardware engineered for modern spaces and designed to endure\.'
hero_replacement = 'Premium aluminium hardware engineered for modern spaces. Exporting globally to the US, Europe, and worldwide.'
content = re.sub(hero_pattern, hero_replacement, content)

# 2. Update Contact Form Options
contact_options_pattern = r'<option>Bulk / Wholesale Order</option>'
contact_options_replacement = '<option>Bulk / Wholesale Order</option>\n                                                <option>International Export & Shipping</option>'
content = re.sub(contact_options_pattern, contact_options_replacement, content)

# 3. Update Chatbot option text
chatbot_btn_pattern = r'📦 Wholesale Orders'
chatbot_btn_replacement = '📦 Wholesale & Export'
content = re.sub(chatbot_btn_pattern, chatbot_btn_replacement, content)

chatbot_text_pattern = r'📦 How do wholesale inquiries work\?'
chatbot_text_replacement = '📦 Do you export internationally?'
content = re.sub(chatbot_text_pattern, chatbot_text_replacement, content)

chatbot_response_pattern = r'It\'s easy! Browse our catalogue, select your models, finishes, and sizes, and click \'Add to Inquiry List\'. Once you\'ve added everything, click \'My List\' to send the exact manifest directly to our WhatsApp for wholesale pricing.'
chatbot_response_replacement = 'Yes, we export globally to the US, Germany, and worldwide! Browse our catalogue, select your models, and click \'Add to Inquiry List\'. Send the manifest to our WhatsApp for international B2B pricing and shipping details.'
content = re.sub(chatbot_response_pattern, chatbot_response_replacement, content)

# 4. Update SEO Block
seo_pattern = r'Based in Rajkot, India, <strong>Harikrushna Enterprise</strong> is a premier manufacturer and supplier of luxury architectural hardware'
seo_replacement = 'Based in Rajkot, India, <strong>Harikrushna Enterprise</strong> is a premier manufacturer and global exporter of luxury architectural hardware'
content = re.sub(seo_pattern, seo_replacement, content)

with open("index.html", "w") as f:
    f.write(content)

print("Global updates applied.")
