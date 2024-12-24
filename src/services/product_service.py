from src.core.mock_data import products_mock_data


class ProductService:
    def __init__(self):
        try:
            self.data = products_mock_data
        except Exception as e:
            print(e)
            self.data = []

    async def get_all_products_info(self):
        try:
            return f"Here is the list of all the products we have: {self.data}"
        except Exception as e:
            print(e)
            return "Error occurred while fetching all product information."

    async def get_product_info(self, product_name: str):
        try:
            for product in self.data:
                if product["Product Name"].upper() == product_name.upper():
                    return product
            return None
        except Exception as e:
            print(e)
            return "Error occurred while fetching product information."

    async def get_product_stock(self, product_name: str):
        try:
            for product in self.data:
                if product["Product Name"].upper() == product_name.upper():
                    return f"Stock for {product_name} is {product['stock']}"
            return None
        except Exception as e:
            print(e)
            return "Error occurred while fetching product stock."
