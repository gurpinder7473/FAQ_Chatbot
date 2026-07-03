"""
FAQ dataset for the chatbot.
Add / edit / remove entries here — each item needs a "question" and an "answer".
"""

FAQ_DATA = [
    # Account & Login
    {"question": "How do I create an account?", "answer": "Click 'Sign Up' on the top right, enter your email and password, then verify your email to activate your account."},
    {"question": "How can I reset my password?", "answer": "Go to Settings > Account > Reset Password and follow the instructions sent to your email."},
    {"question": "I forgot my username, what should I do?", "answer": "Use the 'Forgot Username' link on the login page and enter your registered email to retrieve it."},
    {"question": "How do I delete my account?", "answer": "Go to Settings > Account > Delete Account. Note that this action is permanent and cannot be undone."},
    {"question": "Can I change my registered email address?", "answer": "Yes, go to Settings > Profile > Email and enter your new email address. You'll need to verify it."},
    {"question": "Why can't I log into my account?", "answer": "Check that your email and password are correct. If the issue persists, use 'Forgot Password' to reset it or contact support."},
    {"question": "How do I update my profile information?", "answer": "Go to Settings > Profile and edit your name, phone number, or address, then click Save."},
    {"question": "Is two-factor authentication available?", "answer": "Yes, enable it under Settings > Security > Two-Factor Authentication for extra account protection."},

    # Orders & Shipping
    {"question": "How can I track my order?", "answer": "Go to 'My Orders' and click on the order to see real-time tracking information."},
    {"question": "How long does shipping take?", "answer": "Standard shipping takes 3-5 business days, and express shipping takes 1-2 business days."},
    {"question": "Do you offer international shipping?", "answer": "Yes, we ship to over 50 countries. Shipping fees and times vary by location."},
    {"question": "Can I change my shipping address after placing an order?", "answer": "You can change the address within 1 hour of placing the order by contacting support, before it ships."},
    {"question": "What should I do if my order hasn't arrived?", "answer": "Check the tracking link first. If it's delayed beyond the estimated date, contact our support team for assistance."},
    {"question": "Do you offer same-day delivery?", "answer": "Same-day delivery is available in select cities for orders placed before 12 PM."},
    {"question": "How much does shipping cost?", "answer": "Shipping is free for orders above $50; otherwise a flat fee of $5 applies."},
    {"question": "Can I cancel my order?", "answer": "Orders can be cancelled within 1 hour of placement from the 'My Orders' page."},
    {"question": "What happens if my package is lost?", "answer": "If your tracking shows no movement for 7+ days, contact support and we will investigate or send a replacement."},

    # Payments
    {"question": "What payment methods do you accept?", "answer": "We accept credit cards, debit cards, UPI, net banking, and PayPal."},
    {"question": "Is it safe to save my card details?", "answer": "Yes, all payment data is encrypted and stored securely using industry-standard PCI-DSS compliance."},
    {"question": "Why was my payment declined?", "answer": "This can happen due to insufficient funds, incorrect card details, or bank restrictions. Try another payment method or contact your bank."},
    {"question": "Do you offer cash on delivery?", "answer": "Yes, cash on delivery is available for orders under $100 in select regions."},
    {"question": "Can I pay in installments?", "answer": "Yes, we support EMI options through select banks and credit cards at checkout."},
    {"question": "Will I get an invoice for my purchase?", "answer": "Yes, an invoice is emailed automatically after every successful order and is also available in 'My Orders'."},

    # Refunds & Returns
    {"question": "Do you offer refunds?", "answer": "Yes, we offer full refunds within 30 days of purchase for eligible items."},
    {"question": "How do I return a product?", "answer": "Go to 'My Orders', select the item, click 'Return', and follow the instructions to schedule a pickup."},
    {"question": "How long does a refund take to process?", "answer": "Refunds are processed within 5-7 business days after we receive the returned item."},
    {"question": "Can I exchange a product instead of returning it?", "answer": "Yes, select 'Exchange' instead of 'Return' on the order page and choose your preferred replacement."},
    {"question": "What items are non-returnable?", "answer": "Perishable goods, personal care items, and clearance-sale products are non-returnable."},
    {"question": "Do I have to pay for return shipping?", "answer": "Return shipping is free for defective or incorrect items; otherwise a small fee may apply."},

    # Products
    {"question": "How do I know if a product is in stock?", "answer": "Product availability is shown on the product page. 'In Stock' means it's ready to ship immediately."},
    {"question": "Do you offer size guides?", "answer": "Yes, a size guide is available on every clothing and footwear product page."},
    {"question": "Are your products covered under warranty?", "answer": "Most electronics come with a 1-year manufacturer warranty; check the product page for specific details."},
    {"question": "Can I get notified when an out-of-stock item is back?", "answer": "Yes, click 'Notify Me' on the product page and we'll email you when it's back in stock."},
    {"question": "Do you sell gift cards?", "answer": "Yes, digital gift cards are available in denominations from $10 to $500 under the Gift Cards section."},

    # Customer Support
    {"question": "How do I contact customer support?", "answer": "You can email us at support@example.com, call our helpline, or use the live chat on our website."},
    {"question": "What are your business hours?", "answer": "We are open Monday to Friday, 9 AM to 6 PM, and Saturday 10 AM to 4 PM."},
    {"question": "Is customer support available 24/7?", "answer": "Live chat support is available 24/7; phone support is available during business hours only."},
    {"question": "How do I file a complaint?", "answer": "Go to Support > File a Complaint, describe the issue, and our team will respond within 24 hours."},
    {"question": "Can I speak to a human agent instead of a chatbot?", "answer": "Yes, type 'agent' in the chat window at any time to be connected to a live support representative."},

    # Subscriptions & Memberships
    {"question": "How do I cancel my subscription?", "answer": "Go to Settings > Subscriptions > Manage, then click 'Cancel Subscription'."},
    {"question": "What are the benefits of a premium membership?", "answer": "Premium members get free shipping, early access to sales, and exclusive discounts."},
    {"question": "How much does the premium plan cost?", "answer": "The premium plan costs $9.99 per month or $99 per year, saving you 2 months."},
    {"question": "Will I be charged automatically after my free trial?", "answer": "Yes, your subscription auto-renews at the end of the trial unless you cancel beforehand."},
    {"question": "Can I pause my subscription instead of cancelling?", "answer": "Yes, go to Settings > Subscriptions > Pause, available for up to 3 months."},

    # Technical Issues
    {"question": "The app keeps crashing, what should I do?", "answer": "Try updating the app to the latest version, clearing the cache, or reinstalling it. Contact support if the issue continues."},
    {"question": "Why is the website loading slowly?", "answer": "This may be due to your internet connection or high traffic. Try refreshing or clearing your browser cache."},
    {"question": "I'm not receiving email notifications, why?", "answer": "Check your spam folder and ensure notifications are enabled in Settings > Notifications."},
    {"question": "How do I clear my browser cache?", "answer": "Go to your browser settings, find 'Privacy' or 'History', and select 'Clear Browsing Data'."},

    # Privacy & Security
    {"question": "How is my personal data protected?", "answer": "We use encryption and comply with data protection regulations like GDPR to keep your data secure."},
    {"question": "Do you share my data with third parties?", "answer": "We do not sell your data. It's only shared with trusted partners for order fulfillment and payment processing."},
    {"question": "How do I opt out of marketing emails?", "answer": "Click 'Unsubscribe' at the bottom of any marketing email, or manage preferences in Settings > Notifications."},

    # Loyalty & Discounts
    {"question": "Do you have a loyalty rewards program?", "answer": "Yes, earn points on every purchase which can be redeemed for discounts on future orders."},
    {"question": "How do I apply a discount code?", "answer": "Enter your discount code in the 'Promo Code' field at checkout before completing your payment."},
    {"question": "Why isn't my coupon code working?", "answer": "Check the expiration date and minimum order requirements. Some coupons can't be combined with other offers."},
    {"question": "Do you offer student discounts?", "answer": "Yes, students get 10% off with a verified student email through our student discount program."},

    # Miscellaneous
    {"question": "Do you have a mobile app?", "answer": "Yes, our app is available for free on both the App Store and Google Play."},
    {"question": "Can I place a bulk order for my business?", "answer": "Yes, contact our business sales team at business@example.com for bulk order pricing."},
    {"question": "Do you have physical retail stores?", "answer": "Yes, we have stores in major cities. Use the 'Store Locator' on our website to find one near you."},
    {"question": "How do I unsubscribe from your newsletter?", "answer": "Click the 'Unsubscribe' link at the bottom of any newsletter email."},
    {"question": "What is your company's return policy in detail?", "answer": "Items can be returned within 30 days in original condition with proof of purchase for a full refund or exchange."},
]
