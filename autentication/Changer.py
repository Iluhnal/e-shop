from autentication.authentication import Authentication

email_users = "resources/email_users"
phone_users = "resources/phone_users"
products_loc = "resources/products"

class Change:

    def changePassword(self,new_pass):
        file = []
        if Authentication.logged_user.name.__contains__("@"):
            email = open(email_users, "r", encoding="utf-8")
            for temp in email.readlines():
                splited_user = temp.split("|")
                file.append(splited_user)
                email.close()
            chng = open(email_users, "w", encoding="utf-8")
            chng.write("")
            chng.close()
            track = open(email_users, "a", encoding="utf-8")
            for i in range(len(file)):
                if file[i] == Authentication.logged_user.password:
                    file[i] = new_pass
                track.write(file[i][0] + "|" + file[i][1] + "|" + file[i][2])
            track.close()
        else:
            phone = open(phone_users, "r", encoding="utf-8")
            for temp in phone.readlines():
                splited_user = temp.split("|")
                file.append(splited_user)
            phone.close()
            chng = open(phone_users, "w", encoding="utf-8")
            chng.write("")
            chng.close()
            track = open(phone_users, "a", encoding="utf-8")
            for i in range(len(file)):
                if file[i][1] == Authentication.logged_user.password:
                    file[i][1] = new_pass
                track.write(file[i][0] + "|" + file[i][1] + "|" + file[i][2])
            track.close()

    def changeNick(self,new_nick):
        file = []
        if Authentication.logged_user.name.__contains__("@"):
            chng = open(email_users, "w", encoding="utf-8")
            chng.write("")
            chng.close()
            track = open(email_users, "a", encoding="utf-8")
            email = open(email_users, "r", encoding="utf-8")
            for temp in email.readlines():
                splited_user = temp.split("|")
                file.append(splited_user)
                email.close()
                for i in range(len(file)):
                    if file[i][0] == Authentication.logged_user.name:
                        file[i][0] = new_nick
                    track.write(file[i][0] + "|" + file[i][1] + "|" + file[i][2])
                track.close()

        else:
            phone = open(phone_users, "r", encoding="utf-8")

            for temp in phone.readlines():
                splited_user = temp.split("|")
                file.append(splited_user)
                phone.close()
                chng = open(phone_users, "w", encoding="utf-8")
                chng.write("")
                chng.close()
                track = open(phone_users, "a", encoding="utf-8")
                for i in range(len(file)):
                    if file[i][0] == Authentication.logged_user.name:
                        file[i][0] = new_nick
                    track.write(file[i][0] + "|" + file[i][1] + "|" + file[i][2])
                track.close()

    def chngInfo(self):
        file = []
        products = open(products_loc, "r", encoding="utf-8")
        for temp in products.readlines():
            splited_file = temp.split("|")
            file.append(splited_file)
            products.close()