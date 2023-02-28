class User:

    def __init__(self, name: str, password: str):
        self.password = password
        self.name = name

class Products:

    def __init__(self,product_name: str, description: str, price: int):
        self.product_name = product_name
        self.description = description
        self.price = price

class CartProducts:

    def __init__(self,product_name: str, product_num: int, price: int, product_price: int):
        self.product_name = product_name
        self.product_num = product_num
        self.price = price
        self.product_price = product_price
