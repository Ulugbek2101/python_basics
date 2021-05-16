class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism 
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich  = 1
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    def set_bosqich(self, yangi_bosqich):
         self.bosqich = yangi_bosqich
    def update_bosqich(self):
        self.bosqich +=1
talaba1 = Talaba("Husan", "Hamidov", 2000)
#print(talaba1.get_info())
#talaba1.bosqich=2
#talaba1.set_bosqich(3)
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())

