
son = int(input("Istalgan butun sonni kiriting: "))
for i in range(2,11):
    if son%i == 0:
        print(f"{son} soni {i} ga qodiqsiz bo'linadi")




# foydalanuvchi = ["anvar", "bobur", "mamur", "olim", 'botir']
# login =input("Yangi login tanlang: ")
# if login in foydalanuvchi:
#     print("Xush kelibsiz")
# else:
#     print("Login band, yangi login tanlang.")



# mahsulotlar = ["olma", "anor", "olcha", "shaftoli", "behi", "hurmo", "anjir", "nok", "gilos", "banan"]
# savat = []
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# print("5 ta mahusot kiriting.")
# for i in  range(5):
#      savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))
# for mahsulot in savat:
#      if mahsulot in  mahsulotlar:
#           bor_mahsulotlar.append(mahsulot)
#      else:
#           yoq_mahsulotlar.append(mahsulot)



# if bor_mahsulotlar:
#      print("Do'konimizda quydagi mahsulotlar yo'q:")
# for mahsulot in yoq_mahsulotlar:
#      print(mahsulot)
# else:
#      print("Siz so'ragan barcha mahsulotlar bor.")




# mahsulotlar = ["olma", "anor", "olcha", "shaftoli", "behi", "hurmo", "anjir", "nok", "gilos", "banan"]
# savat = []
# print("5 ta mahusot kiriting.")
# for i in  range(5):
#      savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))
# for sav in savat:
#      if sav in mahsulotlar:
#           print(f"Do'konimizda {sav} bor. ")
#      else:
#           print(f"Do'konimizda {sav} yo'q")





# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi soni kiriting: "))
# if a > b:
#      print(a,">",b )
# elif a < b:
#      print(a,"<",b )
# elif a == b:
#      print(a,"=",b)






# yosh = int(input("Yoshingiz nechada: "))
# if yosh <= 4 or yosh >= 60:
#      narx = 0
# elif yosh <= 18:
#      narx = 10000
# elif yosh > 18:
#      narx = 20000
# print(f"Sizga chipta {narx} so'm.")




# son = int(input("Juft son kiriting>>>>> "))
# if son % 2 == 0:
#      print("Raxmat!")
# else:
#      print("Bu juft son emas.")



# menu = ["so'msa", "norin", "osh", "shashlik", "qazonkabob"]
# buyurtma = ["osh", "norin", "so'msa", "manti"]
# if buyurtma:
#      for taom in buyurtma:
#           if taom in menu:
#                print(f"Menuda {taom} bor.")
#           else:
#                print(f"Kechirasiz, menuda {taom} yo'q.")
# else:
#      print("Savatcha bo'b bosh")              





# menu = ["so'msa", "norin", "osh", "shashlik", "qazonkabob"]
# buyurtma = ["osh", "norin", "so'msa", "manti"]

# for taom in buyurtma:
#      if taom in menu:
#           print(f"Menuda {taom} bor.")
#      else:
#           print(f"Kechirasiz, menuda {taom} yo'q.")




# menu = ["palov", "manti", "so'msa", "chuchvara", "sho'rva"]
# ovqat = input("Nima ovqat yeysiz?>>>>>")
# if ovqat.lower() not in menu:
#      print("Afsusfi bizda bunday ovqat yo'q.")
# else:
#      print("buyurtma qabul qilindi.")





# menu = ['manti', 'olma', 'palov', 'somsa', 'qazon kabob', "chuchvara", "qovirilgan baliq"]
# ovqat = input("Nima buyurtma qilasiz>>>> ")
# if ovqat.lower() in menu:
#      print("Buyurtma qabul qilindi.")
# else:
#      print("Afsuski bizda bunday ovqat yo'q.")





# narx = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# asarti =False
# if choy:
#      print("Mijoz choy oldi.")
#      narx = narx +3000
# if salat:
#      print("Mijoz salat oldi.")
#      narx = narx + 5000
# if non:
#      print("Mijoz non oldi.")
#      narx = narx + 2000
# if kompot:
#      print("Mijoz kompot oldi.")
#      narx = narx + 5000
# if asarti:
#      print("Mijoz asarti oldi.")
#      narx = narx + 15000
# print(f"Jami {narx} so'm.")







# narx =15000
# choy = True
# salat = False

# if choy and salat:
#      narx = narx + 10000
# elif choy or salat:
#      narx = narx +5000

# print(f"Jami {narx} so'm.")







 
# kun =input("Bugungi kun nima? ")
# harorat =float(input("Harorat qanday? "))
# if ( kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat >= 30:
#      print("Ketdik cho'milishga!")
# elif (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat <30:
#      print("Uyda qolamiz.")




# kun = input("Bugungi kun nima? ")
# harorat = float(input("Havo haroarti qanday? "))
# if kun.lower() == "yakshanba" and harorat >= 30:
#      print("Cho'milishga ketdik!")
# elif kun.lower() == "yakshanba" and harorat <30:
#      print("Bugun uyda qolamiz.")





#kun = input("Bugun nima kun: ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#      print("Bugun dam olish kuni.")
# else:
#      print("Bugun ish kuni.")









# yosh = int(input("Yoshingiz nechada?>>>>> "))
# if yosh <=4:
#      price = 0
# elif yosh <= 12:
#      price = 5000
# elif yosh < 65:
#      price = 10000
# elif yosh >= 65:
#      price = 8000
# print(f"Sizga kirish {price} so'm.")








# yosh = int(input("Yoshingizni kiriting>>>> "))
# if yosh <=4:
#      narx = 0
# elif yosh <=12:
#      narx = 5000 
# elif yosh <= 65:  
#      narx = 10000   
# else:
#      narx = 8000
# print(f"Sizga kirish {narx} so'm")











# yosh = int(input("Yoshingizni kiriting>>>> "))
# if yosh <=4:
#      narx = 0
# elif yosh <=12:
#      narx = 5000 
# else:
#      narx = 10000
# print(f"Sizga kirish {narx} so'm")





# yosh = int(input("Yoshingizni kiriting>>>> "))
# if yosh <=4:
#     print("Sizga kirish bepul.")
# elif yosh <=12:
#     print("Sizga kirish 5000 so'm.")
# else:
#     print("Sizzga kirish 10000 so'm.")