from autentication.model.data import User
from autentication.Checking import Check

email_users_file_path = "resources/email_users"
phone_users_file_path = "resources/phone_users"
admin_users_file_path = "resources/Admins"


class RegistrationManager:
    @staticmethod
    def registrate_admin(user: User):
        file = open(admin_users_file_path,"a")
        file.write(user.name + "|" + user.password + "|\n")
        file.close()

    @staticmethod
    def registrate_gmail_user(user: User):
        file = open(email_users_file_path, "a")
        file.write(user.name + "|" + user.password + "|\n")
        file.close()

    @staticmethod
    def registrate_phone_user(user: User):
        print("Hello")
        file = open(phone_users_file_path, "a")
        file.write(user.name + "|" + user.password + "|\n")
        file.close()

    @staticmethod
    def users_wiev():
        file = open(email_users_file_path, "r")
        file1 = open(phone_users_file_path, "r")
        print("email users:", file.read())
        print("phone users:", file1.read())

    def check_users_created_email(user: User):
        email_file = open(email_users_file_path, "r")
        for temp_user in email_file.readlines():
            splited_user = temp_user.split("|")
            print("splited_uiser = ", splited_user)
        email_file.close()


class LoginManager:
    def Login(user: User):
        if Check.check_admin(user):
            return 1
        else:
            if user.name.__contains__("@"):
                if Check.check_email_users(user):
                    return 2
            else:
                if Check.check_phone_users(user):
                    return 2
        return 3
