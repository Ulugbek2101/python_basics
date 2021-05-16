class Avto:
    def __init__(self, model, rang, karobka, narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.kilometr = 0

        def get_info(self):
            return f"{self.rang} rangli {self.model}. Karobka: {self.karobka} narx:{self.narx} "

        def get_model(self):
            return self.model
        
        def get_rang(self):
            return self.rang
        
        def get_karobka(self):
            return self.karobka

        def get_narx(self):
            return self.narx

        def update_km(self):
             self.kilometr += 100

class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.salondagi_avtomobillar_soni = 0
        self.sotuvdagi_avtomobillar = []

    def add_avtomobil(self, avto):
        self.sotuvdagi_avtomobillar.append(avto)
        self.salondagi_avtomobillar_soni += 1
    
    def get_nomi(self):
        return self.nomi

    def get_manzili(self):
        return self.manzili 

    def get_avtomobillar(self):
        return [x.get_info() for x in self.sotuvdagi_avtomobillar]
avtosalon = Avtosalon("Uzavto", "Shavot")
avto1 = Avto("Malibu", "qora", "avtomat", 35000)
avto2 = Avto("Gentra", "oq", "avtomat", 14000)
avto3 = Avto("Cobalt", "oq", "mexanik", 10000)

avtosalon.add_avtomobil(avto1)
avtosalon.add_avtomobil(avto2)
avtosalon.add_avtomobil(avto2)

print(avtosalon.salondagi_avtomobillar_soni())
