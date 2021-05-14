class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username =username
        self.email = email

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.name}, email: {self.email} "
talaba1 = User("Husan Hasanov", "Husan2000", "Husan2000@gmail.com")
print(talaba1.get_info())