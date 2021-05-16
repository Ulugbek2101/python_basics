class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism 
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich  = 1
   
    def set_bosqich(self, yangi_bosqich):
         self.bosqich = yangi_bosqich

    def update_bosqich(self):
        self.bosqich +=1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        return yil-self.tyil

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1

    def get_name(self):
        return self.nomi
         
    def get_students(self):
        return [x.get_info for x in self.talabalar]
    
    def get_students_nom(self):
        return self.talabalar_soni

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Husan", "Olimov", 1998)
talaba2 = Talaba("Asad", "Hamidov", 2000)
talaba3 = Talaba("Maruf", "Toshmadov", 2003)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

mat_talabalar = matematika.get_students()
print(mat_talabalar)

