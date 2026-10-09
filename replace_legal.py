import re

with open("index.html", "r") as f:
    content = f.read()

legal_html = """                    <div class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-b border-brand-lightgray">
                        <div class="max-w-4xl mx-auto text-center">
                            <h1 class="font-serif text-4xl md:text-5xl text-brand-black mb-6 leading-tight">Legal & Policies</h1>
                            <p class="text-brand-gray text-base md:text-xl leading-relaxed max-w-2xl mx-auto">Official terms, conditions, and privacy policies for KUNETT Hardware wholesalers and dealers.</p>
                        </div>
                    </div>
                    <section class="py-12 md:py-20 px-4 md:px-6 max-w-4xl mx-auto min-h-[50vh]">
                        
                        <div class="mb-16">
                            <h2 class="font-serif text-3xl font-bold mb-6 text-brand-black border-b border-brand-lightgray pb-4">Privacy Policy</h2>
                            <p class="text-brand-gray leading-relaxed text-sm">We respect your privacy and are committed to protecting your personal data. Any information collected through our inquiry system or catalogue downloads is used strictly for fulfilling your architectural hardware requests. We do not sell your data to third parties. If you have any questions regarding these policies, you may contact our legal team at kunetthardware@gmail.com.</p>
                        </div>

                        <div class="mb-16">
                            <div class="flex flex-col md:flex-row md:items-end justify-between border-b border-brand-lightgray pb-4 mb-6">
                                <div>
                                    <h2 class="font-serif text-3xl font-bold text-brand-black">Wholesale Terms & Conditions</h2>
                                    <p class="text-brand-gray text-sm mt-1 uppercase tracking-widest font-bold">KUNETT HARDWARE</p>
                                </div>
                                <button onclick="window.print()" class="mt-4 md:mt-0 flex items-center gap-2 text-sm font-bold text-[#f59e0b] hover:text-brand-black transition-colors print:hidden">
                                    <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2M6 14h12v8H6z"/></svg>
                                    Print Document
                                </button>
                            </div>
                            
                            <p class="text-brand-black font-medium mb-6"><strong>Applicable To:</strong> All Wholesalers, Dealers & Authorized Business Customers</p>
                            
                            <ol class="list-decimal pl-5 space-y-4 text-brand-gray text-sm leading-relaxed">
                                <li>All orders placed with KUNETT Hardware shall be considered confirmed only after approval by the company or its authorized representative.</li>
                                <li>The customer shall verify the product code, quantity, colour/finish, and other order details before confirming the order.</li>
                                <li>Once an order has been confirmed, any cancellation, modification or change shall require prior approval from KUNETT Hardware.</li>
                                <li>All wholesale prices shall be as per the latest price list or quotation issued by KUNETT Hardware and may be revised from time to time based on market conditions, raw-material costs, manufacturing costs, transportation or applicable taxes.</li>
                                <li>The price applicable to an order shall be the price confirmed by KUNETT Hardware at the time of order acceptance.</li>
                                <li>Payment shall be made according to the payment terms mutually agreed between KUNETT Hardware and the customer.</li>
                                <li>Orders requiring advance payment shall be processed for dispatch only after the payment has been received and confirmed.</li>
                                <li>Credit facilities, wherever applicable, shall be provided only to approved customers and shall remain subject to the agreed credit limit and payment period.</li>
                                <li>Any outstanding payment beyond the agreed due date may cause the temporary suspension of further dispatches or credit facilities until the outstanding amount is cleared.</li>
                                <li>Certain products may be subject to minimum order quantity, carton quantity or packing requirements, which shall be communicated at the time of quotation or order confirmation.</li>
                                <li>Dispatch shall be processed after the applicable order is completed and payment requirements are met. Delivery timelines provided by KUNETT Hardware are estimated and may vary depending on production, availability, transportation and other circumstances.</li>
                                <li>The customer shall check the number of packages and visible condition of the goods upon delivery and report any shortage, incorrect quantity, or visible damage to KUNETT Hardware promptly.</li>
                                <li>Any shortage or damage claim must be supported by the relevant invoice/order details and photographs or videos wherever required. Transit-related claims may be subject to verification with the transporter.</li>
                                <li>KUNETT Hardware products are supplied subject to standard quality inspection procedures. Genuine manufacturing defects reported within the applicable claim period may be inspected and considered for replacement or other suitable resolution.</li>
                                <li>Replacement of any product shall be subject to inspection and approval by KUNETT Hardware. Damage caused by improper storage, handling, installation, modification, misuse, or normal wear and tear shall not be considered a manufacturing defect.</li>
                                <li>Products shall not be returned or exchanged without prior approval from KUNETT Hardware. Returns due to change of preference, incorrect ordering, slow-moving stock or customer preference shall not normally be accepted.</li>
                                <li>Any approved return must be unused, undamaged, and in acceptable original packaging. Customized, modified, used or damaged products may not be eligible for return or exchange.</li>
                                <li>Product specifications, dimensions, finishes, packaging and availability may be changed from time to time as part of product development or manufacturing improvements.</li>
                                <li>Minor variations in colour, finish, texture or appearance may occur due to manufacturing processes, photography, lighting or display conditions.</li>
                                <li>Wholesalers may use official KUNETT Hardware product images, catalogues, logos, and marketing materials to genuinely promote KUNETT Hardware products.</li>
                                <li>The KUNETT Hardware name, logo, product specifications, and marketing materials shall not be altered or used misleadingly. No wholesaler or dealer shall represent themselves as an employee, manufacturer, or official spokesperson of KUNETT Hardware without written authorization.</li>
                                <li>All wholesalers and dealers are expected to maintain professional business conduct and timely payment practices. Continued supply and commercial facilities may be reviewed based on payment history and outstanding balances.</li>
                                <li>KUNETT Hardware reserves the right to modify, update, or revise these terms from time to time. The latest approved terms shall apply to future transactions.</li>
                                <li>Any exception or special commercial arrangement shall be valid only when approved by KUNETT Hardware in writing.</li>
                                <li>Placement of an order with KUNETT Hardware shall constitute acceptance of these Wholesale Terms & Conditions.</li>
                            </ol>
                            
                            <!-- Customer Acknowledgement Form for Printing -->
                            <div class="mt-16 bg-white border-2 border-brand-lightgray p-8 md:p-10 rounded-xl shadow-sm break-inside-avoid">
                                <h3 class="font-serif text-2xl font-bold mb-8 text-brand-black">CUSTOMER ACKNOWLEDGEMENT</h3>
                                
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-y-8 gap-x-12 text-brand-black text-sm mb-12 font-medium">
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">Firm / Business Name:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">Wholesaler / Dealer Name:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">GST No.:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">Mobile No.:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">Signature & Stamp:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    <div class="flex items-end"><span class="whitespace-nowrap mr-3">Date:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                </div>
                                
                                <div class="border-t border-brand-lightgray pt-8 flex flex-col md:flex-row justify-between items-start gap-12">
                                    <div>
                                        <h4 class="font-bold text-lg text-brand-black mb-2 tracking-wide uppercase">KUNETT HARDWARE</h4>
                                        <p class="text-sm text-brand-gray mb-1">Harikrushna Enterprise</p>
                                        <p class="text-sm text-brand-gray mb-1">Founder: Sanjay Patel</p>
                                        <p class="text-sm text-brand-gray mb-1">Mobile: +91 9924637640</p>
                                        <p class="text-sm text-brand-gray">Location: Rajkot, Gujarat</p>
                                    </div>
                                    <div class="flex flex-col gap-8 text-sm font-medium text-brand-black w-full md:w-auto md:min-w-[300px]">
                                        <div class="flex items-end"><span class="whitespace-nowrap mr-3">Authorized Signature:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                        <div class="flex items-end"><span class="whitespace-nowrap mr-3">Company Seal:</span> <div class="flex-grow border-b border-gray-400"></div></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>"""

# Using regex to find the `else if (page === 'legal') { ... }` block
# We can search for the HTML part specifically and replace it.
target_pattern = r'<div class="bg-brand-offwhite py-16 md:py-24 px-4 md:px-6 border-b border-brand-lightgray">.*?<section class="py-12 md:py-20 px-4 md:px-6 max-w-4xl mx-auto min-h-\[50vh\]">.*?</section>'
content = re.sub(target_pattern, legal_html, content, flags=re.DOTALL)

# Update footer links text
content = content.replace("Privacy Policy", "Wholesale Terms")
content = content.replace("Terms of Service", "Privacy Policy")

with open("index.html", "w") as f:
    f.write(content)

print("Legal terms injected.")
