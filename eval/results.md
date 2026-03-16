# Interaction Log & Evaluation

Scoring Rubric:

- **Relevance (1-5):** How well does the response address the customer's query? (1 = Irrelevant, 5 = Perfectly relevant)
- **Coherence (1-5):** Is the response grammatically correct and easy to understand? (1 = Incoherent, 5 = Flawless)
- **Helpfulness (1-5):** Does the response provide a useful, actionable answer? (1 = Not helpful, 5 = Very helpful)

| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | "How do I track my order?" | Zero-Shot | To track your order, you will need your order number. Once you have it, please visit the tracking page on our website and enter your details to view your current order status. | 5 | 5 | 4 |
| 1 | "How do I track my order?" | One-Shot | You can track your order by logging into your account or clicking the tracking link included in your shipping confirmation email. | 5 | 5 | 5 |
| 2 | "My discount code isn't working." | Zero-Shot | I'm sorry to hear that. Discount codes can sometimes expire or have specific conditions. Make sure you entered it correctly. If you need more help, I can check the code for you if you provide it. | 4 | 5 | 3 |
| 2 | "My discount code isn't working." | One-Shot | I apologize for the trouble! Please double-check that the code hasn't expired and applies to the items in your cart. If it's still not working, let me know the code and I'll look into it for you. | 5 | 5 | 5 |
| 3 | "Can I return an item without the original packaging?" | Zero-Shot | Returning items without original packaging is usually not allowed. You need all original boxes for returns to be processed correctly. | 3 | 5 | 3 |
| 3 | "Can I return an item without the original packaging?" | One-Shot | We strongly recommend returning items in their original packaging to avoid return shipping damage. However, if you no longer have it, please contact support for alternative arrangements. | 5 | 5 | 4 |
| 4 | "Do you ship internationally?" | Zero-Shot | We offer international shipping to many countries worldwide. Additional customs fees might apply depending on your location. | 5 | 5 | 4 |
| 4 | "Do you ship internationally?" | One-Shot | Yes, we ship to most locations internationally! You can find the full list of supported countries and shipping rates on our shipping information page. | 5 | 5 | 5 |
| 5 | "I received the wrong size for my shirt." | Zero-Shot | That shouldn't happen. If you got the wrong size, please send it back. | 3 | 4 | 2 |
| 5 | "I received the wrong size for my shirt." | One-Shot | I am so sorry about that! Please initiate a return through your order history and select 'Incorrect Item Received' to get a free return label and replacement. | 5 | 5 | 5 |
| 6 | "Where is the nearest physical store?" | Zero-Shot | We have local stores in major cities. You can search online for 'Chic Boutique near me'. | 2 | 4 | 2 |
| 6 | "Where is the nearest physical store?" | One-Shot | We are an online-only boutique at this time and do not have physical store locations, but we do offer an easy online return process! | 5 | 5 | 5 |
| 7 | "How long does standard shipping take?" | Zero-Shot | Standard shipping times vary based on the courier and the distance to the destination. | 3 | 5 | 2 |
| 7 | "How long does standard shipping take?" | One-Shot | Standard shipping typically takes 3-5 business days for domestic orders after processing. | 5 | 5 | 5 |
| 8 | "My package says delivered but I haven't received it." | Zero-Shot | If it says delivered, check with your neighbors or look around your property. It might have been hidden. | 4 | 5 | 3 |
| 8 | "My package says delivered but I haven't received it." | One-Shot | I understand how concerning that is! Sometimes carriers mark packages as delivered prematurely. Please wait 24 hours, and if it still hasn't arrived, contact us directly so we can file a claim and send a replacement. | 5 | 5 | 5 |
| 9 | "Can I change my shipping address after placing the order?" | Zero-Shot | Yes, you can change your address depending on the order status. | 3 | 5 | 3 |
| 9 | "Can I change my shipping address after placing the order?" | One-Shot | We can update your shipping address if your order hasn't processed yet! Please contact support immediately with your order number and the correct address. | 5 | 5 | 5 |
| 10 | "How do I apply a gift card to my purchase?" | Zero-Shot | Gift cards can be applied during checkout. Enter the code in the appropriate field. | 5 | 5 | 4 |
| 10 | "How do I apply a gift card to my purchase?" | One-Shot | You can apply your gift card at checkout! Enter your gift card number in the 'Discount code or gift card' field and click 'Apply'. | 5 | 5 | 5 |
| 11 | "What payment methods do you accept?" | Zero-Shot | We take credit cards and some online payment platforms. | 3 | 5 | 3 |
| 11 | "What payment methods do you accept?" | One-Shot | We accept Visa, MasterCard, American Express, PayPal, and Apple Pay. | 5 | 5 | 5 |
| 12 | "I want to cancel my recent order." | Zero-Shot | Orders can be canceled if they haven't shipped. | 4 | 5 | 3 |
| 12 | "I want to cancel my recent order." | One-Shot | If your order hasn't shipped yet, you can cancel it directly from your order history page. If it has already shipped, you'll need to process a return once it arrives. | 5 | 5 | 5 |
| 13 | "The item I want is out of stock. When will it be back?" | Zero-Shot | Restock times vary on a per-item basis. | 2 | 5 | 2 |
| 13 | "The item I want is out of stock. When will it be back?" | One-Shot | We don't have exact restock dates for all items, but you can sign up for restock notifications on the product page by entering your email! | 5 | 5 | 5 |
| 14 | "Do you offer student discounts?" | Zero-Shot | We sometimes offer discounts. Student discounts may be available through third parties. | 3 | 4 | 2 |
| 14 | "Do you offer student discounts?" | One-Shot | Yes, we offer a 15% student discount! You can verify your student status at checkout through our verification partner to instantly receive your code. | 5 | 5 | 5 |
| 15 | "My item arrived damaged." | Zero-Shot | Damage can occur during transit. Send us a picture. | 4 | 4 | 3 |
| 15 | "My item arrived damaged." | One-Shot | I am incredibly sorry your item arrived damaged! Please send a photo of the damaged item and your order number to our support email, and we will express ship a replacement right away. | 5 | 5 | 5 |
| 16 | "How do I create an account?" | Zero-Shot | Creating an account is easy, just click on the sign up button. | 4 | 5 | 4 |
| 16 | "How do I create an account?" | One-Shot | It's easy! Click the 'Sign In/Register' link at the top right of the homepage and select 'Create Account' to sign up. | 5 | 5 | 5 |
| 17 | "I forgot my password." | Zero-Shot | If you forgot your password, you should try to remember it or reset it. | 2 | 5 | 1 |
| 17 | "I forgot my password." | One-Shot | No worries! Just click the 'Forgot Password' link on the login page, enter your email address, and we will send you a link to reset it. | 5 | 5 | 5 |
| 18 | "Can I exchange an item for a different color?" | Zero-Shot | Exchanges can be done for different colors if available. | 4 | 5 | 3 |
| 18 | "Can I exchange an item for a different color?" | One-Shot | Yes! You can process an exchange for a different color (subject to availability) by using our online return portal found in your order history. | 5 | 5 | 5 |
| 19 | "Are there any upcoming sales or promotions?" | Zero-Shot | We run sales often, especially around holidays. Keep an eye out. | 4 | 5 | 3 |
| 19 | "Are there any upcoming sales or promotions?" | One-Shot | The best way to stay updated on our upcoming sales and exclusive promotions is by subscribing to our email newsletter at the bottom of our homepage! | 5 | 5 | 5 |
| 20 | "How can I contact customer support directly?" | Zero-Shot | You can reach us via our support page or email. | 4 | 5 | 4 |
| 20 | "How can I contact customer support directly?" | One-Shot | You can reach us directly by emailing support@chicboutique.com or by calling 1-800-555-0199 during normal business hours. | 5 | 5 | 5 |
