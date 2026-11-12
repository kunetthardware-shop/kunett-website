import re

with open("index.html", "r") as f:
    content = f.read()

# Replace the contact form submit logic
contact_fetch_pattern = r"const formData = new FormData\(form\);.*?\}\);"

whatsapp_logic = """const name = form.querySelector('[name="Name"]').value || '';
                    const email = form.querySelector('[name="Email"]').value || '';
                    const phone = form.querySelector('[name="Phone"]').value || '';
                    const company = form.querySelector('[name="Company"]').value || '';
                    const message = form.querySelector('[name="Message"]').value || '';

                    let waText = `Hello KUNETT Support! I have a new inquiry:\n\n*Name:* ${name}\n*Email:* ${email}\n*Phone:* ${phone}\n*Company:* ${company}\n\n*Message:*\n${message}`;
                    
                    window.open(`https://wa.me/919924637640?text=${encodeURIComponent(waText)}`, '_blank');
                    
                    status.textContent = "✅ Redirecting you to WhatsApp...";
                    status.classList.remove('hidden', 'text-red-600', 'border-red-200', 'bg-red-50');
                    status.classList.add('text-[#25D366]', 'border-green-200', 'bg-green-50');
                    form.reset();
                    btn.textContent = 'Send Message';
                    btn.disabled = false;
                });"""

content = re.sub(contact_fetch_pattern, whatsapp_logic, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

print("Contact form routed to WhatsApp.")
