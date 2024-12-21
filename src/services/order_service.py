from core.mock_data import products_mock_data
from pydantic import BaseModel
from datetime import date
import ast


class Order(BaseModel):
    products: list[dict]
    total: float
    order_date: date


class OrderService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.cart = []
            self.total = 0
            self.orders = []

    def add_products_to_cart(self, product_name_list):
        products = ast.literal_eval(product_name_list)
        products = {key.upper(): value for key, value in products.items()}

        count = 0
        available_products = {
            data["Product Name"].upper(): data for data in products_mock_data
        }  # noqa
        for product in products.items():
            if product[0] in available_products:
                existing_product = next(
                    (item for item in self.cart if item["Name"] == product[0]),
                    None,
                )
                if existing_product:
                    existing_product["quantity"] += product[1]
                    self.total += (
                        available_products[existing_product["Name"]]["price"]
                        * product[1]
                    )
                else:
                    self.cart.append(
                        {
                            "Name": product[0],
                            "quantity": product[1],
                        }
                    )
                    self.total += (
                        available_products[product[0]]["price"] * product[1]
                    )  # noqa
                count += 1
        if len(products) == count:
            return True, "Products added to the cart successfully!"
        return False, "Products not available!"

    def remove_products_from_cart(self, product_name_list: str):
        products = [product.upper() for product in product_name_list.split(",")]  # noqa
        count = 0
        available_products = {
            data["Product Name"].upper(): data for data in products_mock_data
        }  # noqa
        for product in self.cart:
            if product["Name"] in products:
                self.cart.remove(product)
                self.total -= (
                    available_products[product["Name"]]["price"]
                    * product["quantity"]  # noqa
                )
                count += 1
        if len(products) == count:
            return True, "Products removed from the cart successfully!"
        return False, "Product not found in Cart!"

    def create_order(self):
        new_order = Order(
            products=self.cart,
            total=self.total,
            order_date=date.today(),
        )
        self.cart = []
        self.total = 0
        self.orders.append(new_order)
        return "Order created successfully!", new_order.model_dump_json()

    def get_current_total(self):
        return self.total

    def get_current_cart_items(self):
        return f"current cart items {self.cart}"

    def get_all_orders(self):
        return self.orders
