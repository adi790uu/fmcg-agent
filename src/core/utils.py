tools = {
    "get_product_info": {
        "description": "Get information about products, optionally filtered by category",  # noqa
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Category to filter products by (optional)",
                }
            },
        },
    },
    "get_stock_status": {
        "description": "Get stock status for a specific product",
        "parameters": {
            "type": "string",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "Name of the product to check stock for",
                }
            },
            "required": ["product_name"],
        },
    },
}


mock_data = [
    {
        "Category": "Food and Beverages",
        "Product Name": "Organic Almond Butter",
        "Price (USD)": 32.51,
        "Stock Available": 721,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Whole Wheat Bread",
        "Price (USD)": 13.32,
        "Stock Available": 913,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Instant Oatmeal",
        "Price (USD)": 32.79,
        "Stock Available": 112,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Packaged Snacks",
        "Price (USD)": 4.55,
        "Stock Available": 523,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Frozen Veggies",
        "Price (USD)": 32.14,
        "Stock Available": 793,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Natural Honey",
        "Price (USD)": 17.92,
        "Stock Available": 54,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Green Tea",
        "Price (USD)": 38.06,
        "Stock Available": 853,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Bottled Spring Water",
        "Price (USD)": 23.16,
        "Stock Available": 103,
    },
    {
        "Category": "Food and Beverages",
        "Product Name": "Organic Spices",
        "Price (USD)": 29.07,
        "Stock Available": 601,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Herbal Shampoo",
        "Price (USD)": 13.19,
        "Stock Available": 170,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Natural Toothpaste",
        "Price (USD)": 15.97,
        "Stock Available": 691,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Organic Soap",
        "Price (USD)": 4.22,
        "Stock Available": 239,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Sunscreen Lotion",
        "Price (USD)": 1.77,
        "Stock Available": 284,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Hair Oil",
        "Price (USD)": 36.96,
        "Stock Available": 508,
    },
    {
        "Category": "Personal Care",
        "Product Name": "Deodorant",
        "Price (USD)": 41.91,
        "Stock Available": 38,
    },
]
