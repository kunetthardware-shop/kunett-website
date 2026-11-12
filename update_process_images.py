import re

with open("index.html", "r") as f:
    content = f.read()

# Step 3 image replacement
old_img3 = r'<img src="assets/306\.png" alt="Buffing and Electrochemical Anodizing" class="w-\[70%\] h-\[70%\] object-contain mix-blend-multiply hover:scale-105 transition-transform duration-700">'
new_img3 = '<img src="assets/process_anodizing.jpg" alt="Buffing and Electrochemical Anodizing" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">'
content = re.sub(old_img3, new_img3, content)

# Step 4 image replacement
old_img4 = r'<img src="assets/206\.png" alt="Packaged and Delivered Wholesale" class="w-\[70%\] h-\[70%\] object-contain mix-blend-multiply hover:scale-105 transition-transform duration-700">'
new_img4 = '<img src="assets/process_packaging.jpg" alt="Packaged and Delivered Wholesale" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700">'
content = re.sub(old_img4, new_img4, content)

with open("index.html", "w") as f:
    f.write(content)

print("Images replaced.")
