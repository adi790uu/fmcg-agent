# Instructions to setup locally:
1. **Ensure Ollama is Installed**: 
   Before proceeding, make sure that Ollama is installed on your system. Additionally, verify that the `llama3.1` model is available and running. This is essential for the application to function correctly.

2. **Clone the Repository**: 
    ```git clone git@github.com:adi790uu/sarvam.ai-assignment.git```

3. **Navigate to the project directory**:
    ```cd sarvam.ai-assignment ```

4. **Create a virtual environment**:
    ```python3 -m venv env```

5. **Activate the virtual environment**: 
    ```source env/bin/activate```

6. **Install the required packages**: 
    ```pip install -r requirements.txt   ```

7. **Run this command to set path**:
    ```export PYTHONPATH=$(pwd) python src/main.py```

8. **To run the app**:
    ``` streamlit run src/main.py```

# Prompt Engineering Approach:


1. **Agent Prompt**: This is the foundational prompt that outlines the agent's purpose, goals, and essential instructions necessary for the agent to function effectively and as intended.

2. **Tool Call Prompt**: This prompt enables the agent to identify and select the most suitable tools for addressing the end user's query. It includes details about various tools and the response format, which aids in parsing the response to extract the required tools and arguments.


# Components:
- **Agent**: The most crucial component, responsible for generating responses and determining which tools to utilize.

- **OrderService**: Manages order creation and cart operations, including adding items, deleting items, and finalizing orders.

- **ProductService**: Retrieves product information and stock details.


# USECASE Document:

Please refer to the [USECASE document](https://www.notion.so/Assignment-15f7e705910d80ddaacee00be03db5ef?pvs=4).

# Example Conversations:

## Conversation - 1

**Assistant**: Hey, How can I help you today!

---
**User**: add Green tea and hair oil to my cart

---
**Assistant**: The products have been added to your cart successfully. Your current cart contains:

- Green Tea (100gm): ₹120
- Hair Oil (200ml): ₹180

Would you like to proceed with checkout or add more products?

---

**User**: Okay, create my order.

---

**Assistant**: Your order has been created successfully!

- **Order ID**: 639a88e9ec2049f78dc5ca1479f6ffa7
- **Products**:
  - GREEN TEA (1 unit) - ₹120
  - HAIR OIL (1 unit) - ₹180
- **Total Amount**: ₹612.40
- **Order Date**: December 24, 2024

We have sent you an email with your order details. If you need any assistance or have questions about your order, please feel free to contact us.

Thank you for shopping at GreenLife Foods!

---

**User**: Cancel my order with Order ID: 639a88e9ec2049f78dc5ca1479f6ffa7.

---

**Assistant**: The order with Order ID: 639a88e9ec2049f78dc5ca1479f6ffa7 has been cancelled successfully.

Is there anything else I can assist you with? Would you like to place a new order or inquire about our products?

## Conversation - 2

**Assistant**: Hey, how can I help you today!

---

**User**: Hi there.

---

**Assistant**: Hello! I'm happy to assist you in finding the best organic food products from GreenLife Foods. We specialize in providing high-quality, chemical-free food items that cater to the needs of Indian customers.

Before we begin, could you please let me know what specific products or categories you're interested in learning more about? Are you looking for something particular like fruits, vegetables, grains, or perhaps some other category?

We have a wide range of organic products available, and I'd be happy to guide you through our offerings.

---

**User**: Can you list me all the products you have?

---

**Assistant**: Here is the list of all the products we have:

**Food and Beverages**
- Organic Almond Butter: Smooth, creamy almond butter made from organic almonds. Perfect for spreading on toast or adding to smoothies. (Price: ₹2666.82, Stock: 721)
- Whole Wheat Bread: Freshly baked whole wheat bread made with 100% whole grain flour. High in fiber and nutrients. (Price: ₹1092.24, Stock: 913)
- Instant Oatmeal: Quick-cooking organic oatmeal packets. Ready in minutes, perfect for a healthy breakfast. (Price: ₹2688.78, Stock: 112)
- Packaged Snacks: Assorted healthy snacks including nuts, dried fruits, and whole grain crackers. (Price: ₹373.10, Stock: 523)
- Frozen Veggies: Mixed vegetables flash-frozen at peak freshness. Includes broccoli, carrots, and peas. (Price: ₹2635.48, Stock: 793)
- Natural Honey: Pure, unfiltered honey sourced from local beekeepers. Rich in antioxidants and natural enzymes. (Price: ₹1470.56, Stock: 54)
- Green Tea: Premium Japanese green tea leaves. Rich in antioxidants with a subtle, refreshing flavor. (Price: ₹3117.92, Stock: 853)
- Bottled Spring Water: Natural spring water sourced from pristine mountain springs. Available in recyclable bottles. (Price: ₹1899.12, Stock: 103)
- Organic Spices: Collection of certified organic spices including cinnamon, turmeric, and black pepper. (Price: ₹2384.74, Stock: 601)

**Personal Care**
- Herbal Shampoo: Gentle, sulfate-free shampoo made with natural herbs and essential oils. Suitable for all hair types. (Price: ₹1081.58, Stock: 170)
- Natural Toothpaste: Fluoride-free toothpaste made with natural ingredients. Mint flavor for fresh breath. (Price: ₹1310.34, Stock: 691)
- Organic Soap: Handcrafted soap made with organic oils and botanical extracts. Gentle on sensitive skin. (Price: ₹346.04, Stock: 239)
- Sunscreen Lotion: Broad-spectrum SPF 50 sunscreen with natural minerals. Water-resistant and reef-safe. (Price: ₹145.14, Stock: 284)
- Hair Oil: Nourishing hair oil blend with coconut, argan, and jojoba oils. Promotes healthy hair growth. (Price: ₹3031.52, Stock: 508)
- Deodorant: All-natural deodorant with essential oils. Aluminum-free and long-lasting protection. (Price: ₹3435.62, Stock: 38)

Let me know if you'd like to order any of these products!

---

**User**: Can you add Sunscreen Lotion and Natural Toothpaste to my cart?

---

**Assistant**: I've added Sunscreen Lotion and Natural Toothpaste to your cart.

Your current cart:
- Sunscreen Lotion (Price: ₹145.14, Stock: 284)
- Natural Toothpaste (Price: ₹1310.34, Stock: 691)

Would you like to add more products or proceed with the checkout?

---

**User**: Okay, what is my current total?

---

**Assistant**: Based on your current cart and order history, I can confirm that your total comes out to be ₹1,455.48.

Your cart currently contains:
- Sunscreen Lotion (Price: ₹145.14)
- Natural Toothpaste (Price: ₹1310.34)

Would you like to add more products or proceed with the checkout?

---

**User**: Okay, can you remove Sunscreen Lotion and add Green Tea?

---

**Assistant**: I've removed Sunscreen Lotion and added Green Tea to your cart.

Your current cart:
- Natural Toothpaste (Price: ₹1310.34, Stock: 691)
- Green Tea (Price: ₹3117.92, Stock: 853)

Your total comes out to be ₹4,428.26.

---

**User**: Okay, create my order now, thank you.

---

**Assistant**: Order created successfully!

Here is your order summary:
- **Order ID**: 647fed9148374e9e898765198fe0ad2a
- **Date**: 2024-12-24
- **Products**:
  - Natural Toothpaste (Quantity: 1)
  - Green Tea (Quantity: 1)
- **Total**: ₹4,428.26

We will process your order and ship it out to you shortly. Thank you for shopping with us!


# Limitations 

- No after delivery or order tracking assistance available currently.
- No persistance of data, integrating a databse such as postgresql would be ideal for this application.
- Stock management not available.