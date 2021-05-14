class Talaba:
    """Talaba nomili class yaratamiz"""
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        return yil-self.tyil
    
    def tanishtir(self):
        print (f"Ismim {self.ism} {self.familiya}. {self.tyil} da tug'ilganman.")
talaba1 = Talaba("Asad", "Madiyev", 1998)
print(talaba1.get_age(2021))



# class Talaba:
#     """Talaba nomili class yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_name(self):
#         return self.ism

#     def get_lastname(self):
#         return self.familiya

#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"
    
#     def tanishtir(self):
#         print (f"Ismim {self.ism} {self.familiya}. {self.tyil} da tug'ilganman.")
# talaba1 = Talaba("Asad", "Madiyev", 1998)
# print(talaba1.get_fullname())




# class Talaba:
#     """Talaba nomili class yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def tanishtir(self):
#         print (f"Ismim {self.ism} {self.familiya}. {self.tyil} da tug'ilganman.")
# talaba1 = Talaba("Asad", "Madiyev", 1998)
# talaba2 = Talaba("Olim", "Qodirov", 2000)
# talaba3 = Talaba("Husan", "Shokirov", 2005)

# talaba1.tanishtir()