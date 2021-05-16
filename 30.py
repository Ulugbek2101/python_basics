class Shaxs:
    def __init__(self, ism, familiya, passport, tyil ):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport} {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self, yil):
        return yil-self.tyil
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.mazil = manzil
    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.bosqich}-bosqich. ID raqami:{self.idraqam}"
        return info
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzi = f"{self.viloyat} viloayti, {self.tuman} tumani"
        manzil += f"{self.kocha} ko'chasi {self.uy}-uy"
        return manzil
talaba_manzil = Manzil(14,"Amir Temur","Urganch","Xorazm")
talaba=Talaba("Olim","Hamidov","AB1234567", 2000, "00000012",talaba_manzil)
print(talaba.manzil.get_manzil())
