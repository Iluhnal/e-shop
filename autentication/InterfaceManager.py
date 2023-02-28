import tkinter
from tkinter import *

from autentication.Changer import Change
from autentication.Checking import Check
from autentication.authentication import Authentication
from autentication.file_manager import RegistrationManager
from autentication.filleReader import Reader
from autentication.model.data import *


class CartCounter:
    def __init__(self, productAmount: Label, productPrice: Label, oneProductPrice: int, productName: str):
        self.productAmount = productAmount
        self.product_price = productPrice
        self.oneProductPrice = oneProductPrice
        self.productName = productName


name = ""
password = ""
Read = Reader()
products_loc = "resources/products"


def __init__(self, user: User):
    self.user = user


def registrate_admin():
    add_admin = Tk()
    add_admin.geometry("400x300")

    name_label = Label(add_admin, text="Введіть нікнейм")
    pswrd_label = Label(add_admin, text="Введіть пароль")
    name_enter = Entry(add_admin, width=20)
    password_enter = Entry(add_admin, width=20)
    confrim_btn = Button(add_admin, text="Прийняти", width=15, height=3,
                         command=lambda: register_admin(User(name_enter.get(), password_enter.get())))

    name_label.place(relx=0.13, rely=0.01)
    pswrd_label.place(relx=0.13, rely=0.1)
    name_enter.place(relx=0.4, rely=0.01)
    password_enter.place(relx=0.4, rely=0.1)
    confrim_btn.place(relx=0.4, rely=0.16)

    add_admin.mainloop()


def register_admin(User):
    RegistrationManager.registrate_admin(User)


def inAdminAcc(previous_window: Tk):
    admin_page = Tk()
    previous_window.destroy()
    admin_page.geometry("800x600")

    mainmenu = Menu(admin_page)
    admin_page.config(menu=mainmenu)

    page_set = Menu(mainmenu, tearoff=0)
    page_set.add_command(label="Додати нового Адміна", command=lambda: registrate_admin())
    page_set.add_command(label="nonfun", command=lambda: new_product())
    page_set.add_command(label="Зміна інформації/Видалення", command=lambda: openAdminProductsScreen(admin_page))

    user_cab = Menu(mainmenu, tearoff=0)
    user_cab.add_command(label="Корзина")

    mainmenu.add_cascade(label="Редагування", menu=page_set)
    mainmenu.add_cascade(label="Особистий кабінет", menu=user_cab)

    admin_page.mainloop()


def chng_info():
    chng_page = Tk()
    chng_page.geometry("400x300")


def openAdminProductsScreen(previous_window: Tk):
    products_screen = Tk()
    products_screen.geometry('')
    previous_window.destroy()

    products_reader = Reader()
    my_products = products_reader.products()

    for i in range(len(my_products)):
        product_name = Label(products_screen, text=my_products[i].product_name)
        product_name.grid(row=i, column=0)
        description = Label(products_screen, text=my_products[i].description)
        description.grid(row=i, column=1)
        price = Label(products_screen, text=my_products[i].price)
        price.grid(row=i, column=2)
        open_button = Button(products_screen, text="Відкрити",
                             command=lambda x=i: openAdminProduct(products_screen, my_products[x]))
        open_button.grid(row=i, column=3)

    products_screen.mainloop()


def new_product():
    product_page = Tk()
    product_page.geometry("600x300")

    product_name = Label(product_page, text="Введіть назву товару")
    product_description = Label(product_page, text="Введіть опис товару")
    product_price = Label(product_page, text="Введіть ціну товару")
    name_enter = Entry(product_page, width=30)
    description_enter = Entry(product_page, width=50)
    price_enter = Entry(product_page, width=10)
    confrim_btn = Button(product_page, width=15, height=3, text="Прийняти",
                         command=lambda: add_product(name_enter.get(), description_enter.get(), price_enter.get()))

    product_name.place(relx=0.08, rely=0.03)
    product_description.place(relx=0.08, rely=0.13)
    product_price.place(relx=0.08, rely=0.23)
    name_enter.place(relx=0.3, rely=0.03)
    description_enter.place(relx=0.3, rely=0.13)
    price_enter.place(relx=0.3, rely=0.23)
    confrim_btn.place(relx=0.4, rely=0.45)

    product_page.mainloop()


def openAdminProduct(previous_window: Tk, my_products):
    product_page = Tk()
    product_page.geometry('1000x350')
    previous_window.destroy()

    def changeNick(new_name):

        file = []
        products = open(products_loc, "r", encoding="utf-8")
        for temp in products.readlines():
            splited_file = temp.split("|")
            file.append(splited_file)
        products.close()
        chng = open(products_loc, "w", encoding="utf-8")
        chng.write("")
        chng.close()
        track = open(products_loc, "a", encoding="utf-8")
        for i in range(len(file)):
            if my_products.product_name == file[i][0]:
                file[i][0] = new_name
                my_products.product_name = new_name
            track.write("" + file[i][0] + "|" + file[i][1] + "|" + file[i][2] + "|\n")
        track.close()
        openAdminProductsScreen(product_page)

    def changeDeskription(new_deskription):
        file = []
        products = open(products_loc, "r", encoding="utf-8")
        for temp in products.readlines():
            splited_file = temp.split("|")
            file.append(splited_file)
        products.close()
        chng = open(products_loc, "w", encoding="utf-8")
        chng.write("")
        chng.close()
        track = open(products_loc, "a", encoding="utf-8")
        for i in range(len(file)):
            if my_products.product_name == file[i][0]:
                file[i][1] = new_deskription
                my_products.description = new_deskription
            track.write("" + str(file[i][0]) + "|" + file[i][1] + "|" + file[i][2] + "|\n")
        track.close()
        openAdminProductsScreen(product_page)

    def changePrice(new_price):
        file = []
        products = open(products_loc, "r", encoding="utf-8")
        for temp in products.readlines():
            splited_file = temp.split("|")
            file.append(splited_file)
        products.close()
        chng = open(products_loc, "w", encoding="utf-8")
        chng.write("")
        chng.close()
        track = open(products_loc, "a", encoding="utf-8")
        for i in range(len(file)):
            if my_products.product_name == file[i][0]:
                file[i][2] = new_price
                my_products.price = new_price
            track.write("" + file[i][0] + "|" + file[i][1] + "|" + file[i][2] + "|\n")
        track.close()
        openAdminProductsScreen(product_page)

    def delIt():
        file = []
        products = open(products_loc, "r", encoding="utf-8")
        for temp in products.readlines():
            splited_file = temp.split("|")
            file.append(splited_file)
            products.close()
        chng = open(products_loc, "w", encoding="utf-8")
        chng.write("")
        chng.close()
        track = open(products_loc, "a", encoding="utf-8")
        for i in range(len(file)-1):
            if my_products.product_name == file[i][0]:
                del file[i]
            track.write(file[i][0] + "|" + file[i][1] + "|" + file[i][2] + "|\n")
        track.close()
        openAdminProductsScreen(product_page)

    product_name = Label(product_page, text=my_products.product_name, font=("Comic Sans MS", 16))
    product_name.place(relx=0.01, rely=0.01)
    description = Label(product_page, text=my_products.description, font=("Comic Sans MS", 16))
    description.place(relx=0.3, rely=0.01)
    price = Label(product_page, text=my_products.price * 1, font=("Comic Sans MS", 16))
    price.place(relx=0.9, rely=0.01)
    del_button = Button(product_page, text="Видалити", command=lambda: delIt(), font=("Arial", 8))
    del_button.place(relx=0.02, rely=0.4)
    name_btn = Button(product_page, text="Змінити назву", command=lambda: changeNick(entr.get()), font=("Arial", 8))
    description_btn = Button(product_page, text="Змінити опис", command=lambda: changeDeskription(entr.get()),
                             font=("Arial", 8))
    price_btn = Button(product_page, text="Змінити ціну", command=lambda: changePrice(entr.get()), font=("Arial", 8))
    entr = Entry(product_page)

    name_btn.place(relx=0.02, rely=0.1)
    description_btn.place(relx=0.02, rely=0.2)
    price_btn.place(relx=0.02, rely=0.3)
    entr.place(relx=0.12, rely=0.25)


def add_product(name, description, price):
    products = open(products_loc, "a", encoding="utf-8")
    products.write(str(name) + "|")
    products.write(str(description) + "|")
    products.write(str(price) + "|\n")


all_price = 0.0


def openCart(previous_window: Tk):
    global num
    global all_price

    def changeNum(to_add, product_counter: CartCounter):
        global num
        global all_price
        if num < 2 and to_add == -1:
            return

        num = num + to_add
        product_counter.productAmount['text'] = product_counter.productAmount['text'] + to_add

        all_prd_num['text'] = num
        all_price = all_price + product_counter.oneProductPrice
        if to_add == 1:

            last_price['text'] = last_price['text'] + product_counter.oneProductPrice
            product_counter.product_price['text'] = product_counter.product_price[
                                                        'text'] + product_counter.oneProductPrice
            all_price = all_price + product_counter.oneProductPrice
        else:
            last_price['text'] = last_price['text'] - product_counter.oneProductPrice
            product_counter.product_price['text'] = product_counter.product_price[
                                                        'text'] - product_counter.oneProductPrice
            all_price = all_price - product_counter.oneProductPrice

        for i in range(len(my_products)):
            if my_products[i].product_name == product_counter.productName:
                my_products[i].product_num = product_counter.productAmount['text']

    def delit(product_counter: CartCounter, current_cart_screen):
        global num

        user_cart = "resources/Carts/cart" + Authentication.logged_user.name
        chng = open(user_cart, "w", encoding="utf-8")
        chng.write("")
        chng.close()
        track = open(user_cart, "a", encoding="utf-8")
        for i in range(len(my_products) - 1):
            if product_counter.productName == my_products[i].product_name:
                del my_products[i]
            track.write("" + str(my_products[i].product_name) + "|" + str(my_products[i].product_num) + "|" + str(
                my_products[i].price) + "|" + str(my_products[i].product_price) + "|\n")
        track.close()

        openCart(current_cart_screen)

    def full_del():
        user_cart = "resources/Carts/cart" + Authentication.logged_user.name
        cart = open(user_cart, "w")
        cart.close()
        quit()

    def buyIt():
        buy_screen = Tk()
        buy_screen.geometry("400x300")

        text = Label(buy_screen, text="Загальна ціна/кількість товарів:")
        prd_price = Label(buy_screen, text=last_price['text'])
        all_num = Label(buy_screen, text=num)
        cnfrm_btn = Button(buy_screen, text="Придбати", command=lambda: full_del())

        text.place(relx=0.25, rely=0.05)
        prd_price.place(relx=0.4, rely=0.15)
        all_num.place(relx=0.55, rely=0.15)
        cnfrm_btn.place(relx=0.45, rely=0.3)

    cart_screen = Tk()
    previous_window.destroy()
    cart_screen.geometry("800x600")
    Read.cart_reader()

    products_reader = Reader()
    my_products = products_reader.cart_reader()


    for i in range(len(my_products)):
        name_prnt = Label(cart_screen, text=my_products[i].product_name)
        prd_num = Label(cart_screen, text=int(my_products[i].product_num))
        price = Label(cart_screen, text=my_products[i].price)
        product_object = CartCounter(productAmount=prd_num, productPrice=price,
                                     oneProductPrice=my_products[i].product_price,
                                     productName=my_products[i].product_name)
        all_price = float(all_price) + my_products[i].price
        add_btn = Button(cart_screen, text="+", height=1, width=1, command=lambda x=product_object: changeNum(1, x))
        minus_btn = Button(cart_screen, text="-", height=1, width=1, command=lambda x=product_object: changeNum(-1, x))
        del_btn = Button(cart_screen, text="Видалити товар", height=1, width=15,
                         command=lambda x=product_object: delit(x, cart_screen))
        num = num + int(my_products[i].product_num)

        name_prnt.grid(row=i, column=0)
        prd_num.grid(row=i, column=1)
        price.grid(row=i, column=2)
        add_btn.grid(row=i, column=3)
        minus_btn.grid(row=i, column=4)
        del_btn.grid(row=i, column=5)

    last_price = Label(cart_screen, text=all_price, font=("Comic Sans MS", 16))
    all_prd_num = Label(cart_screen, text=num)
    buy_btn = Button(cart_screen, text="Придбати", height=1, width=15, command=lambda: buyIt())

    last_price.place(relx=0.6, rely=0.05)
    all_prd_num.place(relx=0.6, rely=0.02)
    buy_btn.place(relx=0.5, rely=0.8)

def InAcc(previous_window: Tk):
    menu_screen = Tk()
    previous_window.destroy()
    menu_screen.geometry('')

    products_screen = Button(menu_screen, text="Товари")
    products_screen.bind("<Button-1>", lambda event, button=products_screen: openProductsScreen(menu_screen))
    products_screen.place(relx=0.01, rely=0.01)

    user_page = Button(menu_screen, text="Особистий кабінет")
    user_page.bind("<Button-1>", lambda event, button=user_page: openUserPage(menu_screen))
    user_page.place(relx=0.01, rely=0.15)

    menu_screen.mainloop()


def pass_chg(previous_window: Tk):
    pass_chng = Tk()
    previous_window.destroy()
    pass_chng.geometry("400x300")

    Changes = Change()

    enter = Label(pass_chng, text="Введіть новий пароль")
    enter.place(relx=0.14, rely=0.01)
    new_pass = Entry(pass_chng, width=25)
    new_pass.place(relx=0.4, rely=0.01)
    confrim_btn = Button(pass_chng, text="Прийняти", width=15, height=2,
                         command=lambda: Changes.changePassword(new_pass.get()))
    confrim_btn.place(relx=0.4, rely=0.1)

    pass_chng.mainloop()


def nick_chng(previous_window: Tk):
    name_chng = Tk()
    previous_window.destroy()
    name_chng.geometry("400x300")

    Changes = Change()

    enter = Label(name_chng, text="Введіть новий нікнейм")
    enter.place(relx=0.2, rely=0.01)
    new_name = Entry(name_chng, width=25)
    new_name.place(relx=0.4, rely=0.01)
    confrim_btn = Button(name_chng, text="Прийняти", width=15, height=2,
                         command=lambda: Changes.changeNick(new_name.get()))
    confrim_btn.place(relx=0.4, rely=0.1)

    name_chng.mainloop()


def openUserPage(previous_window: Tk):
    user_page = Tk()
    previous_window.destroy()
    user_page.geometry('400x300')

    mainmenu = Menu(user_page)
    user_page.config(menu=mainmenu)

    page_set = Menu(mainmenu, tearoff=0)
    page_set.add_command(label="Зміна паролю", command=lambda: pass_chg(user_page))
    page_set.add_command(label="Зміна номеру/пошти", command=lambda: nick_chng(user_page))

    user_cab = Menu(mainmenu, tearoff=0)
    user_cab.add_command(label="Корзина", command=lambda: openCart(user_page))

    mainmenu.add_cascade(label="Налаштування", menu=page_set)
    mainmenu.add_cascade(label="Особистий кабінет", menu=user_cab)

    user_page.mainloop()


def openProductsScreen(previous_window: Tk):
    previous_window.destroy()
    products_screen = Tk()
    products_screen.geometry('')

    products_reader = Reader()
    my_products = products_reader.products()

    for i in range(len(my_products)):
        product_name = Label(products_screen, text=my_products[i].product_name)
        product_name.grid(row=i, column=0)
        description = Label(products_screen, text=my_products[i].description)
        description.grid(row=i, column=1)
        price = Label(products_screen, text=my_products[i].price)
        price.grid(row=i, column=2)
        open_button = Button(products_screen, text="Відкрити",
                             command=lambda x=i: openProduct(products_screen, my_products[x]))
        open_button.grid(row=i, column=3)

    products_screen.mainloop()


num = 0


def openProduct(previous_window: Tk, my_products):
    global num
    def changeNum(to_add):
        global num
        if num < 2 and to_add == -1:
            return

        num = num + to_add
        product_num['text'] = num
        price['text'] = my_products.price * num

    def addToCart():
        Cart = "resources/Carts/cart" + Authentication.logged_user.name
        cart_file = open(Cart, "a", encoding="utf-8")
        cart_file.write(str(my_products.product_name) + "|" + str(num) + "|" + str(my_products.price * num) + "|" + str(
            my_products.price) + "\n")

    previous_window.destroy()
    product_page = Tk()
    product_page.geometry('')

    product_name = Label(product_page, text=my_products.product_name, font=("Comic Sans MS", 16))
    product_name.place(relx=0.27, rely=0.01)
    description = Label(product_page, text=my_products.description, font=("Comic Sans MS", 16))
    description.place(relx=0.4, rely=0.01)
    price = Label(product_page, text=my_products.price * 1, font=("Comic Sans MS", 16))
    price.place(relx=0.5, rely=0.07)
    cart_button = Button(product_page, text="Додати в корзину", command=lambda: addToCart(), width=8, height=2,
                         font=("Arial", 12))
    cart_button.place(relx=0.5, rely=0.11)
    separator = Frame(product_page, height=1, bd=2, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)
    plus_btn = Button(product_page, text="+", command=lambda: changeNum(1), font=("Comic Sans MS", 16))
    minus_btn = Button(product_page, text="-", command=lambda: changeNum(-1), font=("Comic Sans MS", 16))
    plus_btn.place(relx=0.45, rely=0.06)
    minus_btn.place(relx=0.45, rely=0.13)
    product_num = Label(product_page, font=("Comic Sans MS", 16), text=num)
    product_num.place(relx=0.43, rely=0.1)


def login(name: str, password: str, previous_window: tkinter.Tk):
    login_result = LoginManager.Login(User(name, password))
    if login_result == 1:
        inAdminAcc(previous_window)
    elif login_result == 2:
        InAcc(previous_window)
    elif login_result == 3:
        print("Error")
        login(name, password, previous_window)


def register(name: str, password: str):
    Authentication.registrate_user(name, password)


def openRegisterScreen(previous_window: Tk):
    previous_window.destroy()
    register_screen = Tk()
    register_screen.geometry('')

    register_name_entry = Entry(register_screen, width=25)
    register_name_entry.place(relx=0.47, rely=0.01)

    register_password_entry = Entry(register_screen, width=25)
    register_password_entry.place(relx=0.47, rely=0.05)

    register_button = Button(register_screen, text="Зареєструватися",
                             command=lambda: register(register_name_entry.get(),
                                                      register_password_entry.get()))
    register_button.place(relx=0.5, rely=0.1)


def openLoginScreen(previous_window: Tk):
    previous_window.destroy()
    login_screen = Tk()
    login_screen.geometry('')
    login_screen.winfo_width()

    login_name_entry = Entry(login_screen, width=25)
    login_name_entry.place(relx=0.1, rely=0.01)

    login_password_entry = Entry(login_screen, width=25)
    login_password_entry.place(relx=0.1, rely=0.09)

    login_button = Button(login_screen, text="Увійти")
    login_button.bind("<Button-1>",
                      lambda event, button=login_button: login(login_name_entry.get(), login_password_entry.get(),
                                                               login_screen))
    login_button.place(relx=0.4, rely=0.22)

    login_screen.mainloop()


class AuthenticationInterface:

    def __init__(self):
        start_screen = Tk()

        register_button = Button(start_screen, text="Реєстрація", command=lambda: openRegisterScreen(start_screen))
        login_button = Button(start_screen, text="Увійти", command=lambda: openLoginScreen(start_screen))

        register_button.place(relx=0.35, rely=0.01)
        login_button.place(relx=0.35, rely=0.13)
        start_screen.mainloop()


class LoginManager:
    def Login(user: User):
        if Check.check_admin(user):
            return 1
        else:
            if user.name.__contains__("@"):
                if Check.check_email_users(user):
                    Authentication.logged_user = user
                    return 2
            else:
                if Check.check_phone_users(user):
                    Authentication.logged_user = user
                    return 2
        return 3
