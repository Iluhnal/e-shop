from autentication.model.data import Products
from autentication.authentication import Authentication
from autentication.model.data import CartProducts
products = "resources/products"
products_list = []
prd: Products = Products("", "", 0)

class Reader:

    def cart_reader(self):
        cart_list = []
        cart = "resources/Carts/cart" + Authentication.logged_user.name
        cart_file = open(cart, "r", encoding="utf-8")
        for temp in cart_file.readlines():
            splitted_file = temp.split("|")
            cart_list.append(CartProducts(product_name=str(splitted_file[0]), product_num=int(splitted_file[1]), price=int(
                splitted_file[2]), product_price=int(splitted_file[3])))
        cart_file.close()
        return cart_list

    def get_products(self):
        products_file = open(products, "r", encoding="utf-8")
        for temp in products_file.readlines():
            splited_file = temp.split("|")
            products_list.append(
                Products(product_name=splited_file[0], description=splited_file[1], price=int(splited_file[2])))
        products_file.close()
        return products_list

    def products(self):
        if len(products_list) > 0:
            return products_list
        else:
            return self.get_products()








