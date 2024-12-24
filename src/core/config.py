MODEL = "llama3.1"

tools = {
    "get_product_info": {
        "description": "Get information about a product",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "Category to filter products by (optional)",
                }
            },
            "required": ["product_name"],
        },
    },
    "cancel_order": {
        "description": "Cancel an exisiting order.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Id associated with the order",
                }
            },
            "required": ["product_name"],
        },
    },
    "get_product_stock": {
        "description": "Get stock for a specific product",
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
    "get_current_total": {
        "description": "Retrieve the current total amount in the cart",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    "get_current_cart_items": {
        "description": "Get a list of items currently in the cart",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    "get_all_orders": {
        "description": "Get all orders made by the user",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    "add_products_to_cart": {
        "description": "Add a product/products to the shopping cart",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name_list": {
                    "type": "dictionary",
                    "description": "Name of the products to add to cart as key and the number of units as value by default it will be 1.",  # noqa
                }
            },
            "example": "{'Green Tea': 1}, {'Frozen Veggies': 1}",
            "required": ["product_name_list"],
        },
    },
    "remove_products_from_cart": {
        "description": "Remove a product/products from the shopping cart",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name_list": {
                    "type": "string",
                    "description": "Name of the products to remove from cart",
                }
            },
            "example": "Green Tea, Frozen Veggies",
            "required": ["product_name_list"],
        },
    },
    "create_order": {
        "description": "Create a new order from the current cart contents",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    "get_all_products_info": {
        "description": "Get information about all available products",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
}
