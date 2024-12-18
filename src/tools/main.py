from core.utils import mock_data


def get_product_info(category=None):
    """Get product information, optionally filtered by category"""
    if category:
        return [item for item in mock_data if item["Category"] == category]
    return mock_data


def get_stock_status(product_name):
    """Get stock status for a specific product"""
    for item in mock_data:
        if item["Product Name"].lower() == product_name.lower():
            print(item["Stock Available"])
            return {
                "product": item["Product Name"],
                "stock": item["Stock Available"],
                "status": "Low" if item["Stock Available"] < 100 else "Good",
            }
    return {"error": "Product not found"}
