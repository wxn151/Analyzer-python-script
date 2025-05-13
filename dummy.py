class UserService:
    def __init__(self):
        self.db = DB()
        self.mailer = Mailer()

    def register_user(self):
        print("Registering")

    def login_user(self):
        print("Logging in")

    def send_email(self):
        print("Sending email")

    def reset_password(self):
        print("Resetting")

    def deactivate_user(self):
        print("Deactivating")

class DB:
    pass

class Mailer:
    pass
