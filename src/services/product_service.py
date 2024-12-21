from core.mock_data import products_mock_data


class ProductService:
    def __init__(self):
        self.data = products_mock_data

    def get_all_products_info(self):
        return self.data

    def get_product_info(self, product_name: str):
        for product in self.data:
            if product["Product Name"] == product_name:
                return product
        return None

    def get_product_stock(self, product_name: str):
        for product in self.data:
            if product["Product Name"] == product_name:
                return f"Stock for {product_name} is {product['stock']}"
        return None
