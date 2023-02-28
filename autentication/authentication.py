from autentication.model.data import User
from autentication.file_manager import RegistrationManager
from autentication.Checking import Check



gmail_users_file_path = "resources/email_users"
phone_users_file_path = "resources/phone_users"

logged_user: User = User("", "")

def check_password(password: str):
    number_cost = 0
    if len(password) < 7 or len(password) > 19:
        print("wrong password length(too short or too long)")
        return False
    if not password.istitle():
        print("password must begin with an uppercase letter")
        return False
    for i in range(len(password)):
        if password[i].isdigit():
            number_cost = number_cost + 1
        if number_cost > 3:
            break
    if number_cost < 4:
        print("need 4 numbers")
        return False
    return True


def check_email(email: str):
    short = email[email.find("@"):len(email)]
    if len(short[short.find("."):len(short)]) < 2 or len(email[email.find("@"):len(email)]) < 5:
        print("Wrong email doman!")
        return False
    if len(email[0:email.find("@")]) < 3:
        print("Wrong email name!")
        return False
    if email.find("@") != email.rfind("@"):
        print("Email cannot contain more than 1 '@'!")
        return False

    return True

def check_phone_number(phone_number: str):
        if len(phone_number) < 10:
            print("Wrong phone number (too short)!")
        if phone_number.__contains__("+"):
            if not phone_number[1:len(phone_number)].isdigit():
                print("Wrong phone number! (Should be only numbers and + in start!)")
                return False
            if len(phone_number) != 13:
                print("Phone number length is wrong!")
                return False
            return True
        else:
            if len(phone_number) != 10 and len(phone_number) != 12:
                print("Wrong number lenght!")
                return False
            if not phone_number.startswith("0") or phone_number.startswith("380"):
                print("Wrong phone number")
                return False
            else:
                if not phone_number.isdigit():
                    print("Wrong phone number! (Should be only numbers!)")
                    return False
        return True


class Authentication:
    logged_user = User("00", "00")
    @staticmethod
    def get_logged_user():
        return logged_user
    @staticmethod
    def registrate_user(name: str, password: str):

        if Authentication.register_user(User(name, password)):
            global logged_user
            logged_user = User(name, password)
    @staticmethod
    def register_user(user: User):
        if user.name.__contains__("@"):
            if not Check.check_email_users(user):
                if check_email(user.name) and check_password(user.password):
                    RegistrationManager.registrate_gmail_user(user)
                    return True
                return False
            print("this email is already in use")

        if not Check.check_phone_users(user):
            if check_phone_number(user.name) and check_password(user.password):
                RegistrationManager.registrate_phone_user(user)
                return True
            return False
        print("this phone number is already in use")

