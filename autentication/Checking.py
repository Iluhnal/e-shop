from autentication.model.data import User

email_users_file_path = "resources/email_users"
phone_users_file_path = "resources/phone_users"
admin_users_file_path = "resources/Admins"
class Check:
    @staticmethod
    def check_admin(user: User):
        admins_file = open(admin_users_file_path, "r")
        for temp_user in admins_file.readlines():
            splited_user = temp_user.split("|")
            if splited_user[0] == user.name:
                if splited_user[1] == user.password:
                    return True
        admins_file.close()
        return False

    @staticmethod
    def check_email_users(user: User):
        email_file = open(email_users_file_path, "r")
        for temp_user in email_file.readlines():
            splited_user = temp_user.split("|")
            if splited_user[0] == user.name:
                if splited_user[1] == user.password:
                    return True
        email_file.close()
        return False

    @staticmethod
    def check_phone_users(user: User):
        phone_file = open(phone_users_file_path, "r")
        for temp_user in phone_file.readlines():
            splited_user = temp_user.split("|")
            if splited_user[0] == user.name:
                if splited_user[1] == user.password:
                    phone_file.close()
                    return True
        phone_file.close()
        return False



