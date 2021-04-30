buyurtmalar = ['olma', 'anor', 'uzum', 'olcha']
mahsulotlar = {
    'olma':10000,
    'banan':8000,
    'shaftoli':30000,
    'anor':20000,
    'uzum':40000
}
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh =mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narh} so'm ")
    else:
        print(f"Bizda {buyurtma} yo'q.")


# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulotning nomini kiriting: ")
#     baho = input(f"{mahsulot.title()} bahosini kiriting: ")
#     mahsulotlar[mahsulot] = int(baho)
    
#     javob = input("Yana mahsulot kiritasizmi (ha/yo'q): ")
#     if javob != 'ha':
#         break





# mahsulotlar = []
# print("Nima buyurtma qilmoqchisiz?")
# n=1
# while True:
#     mahsulot = input(f"{n}-buyurtmangizni kiriting: ")
#     mahsulotlar.append(mahsulot)
#     javob =input("Yana buyurtma berasizmi (ha/yo'q): ")
#     if javob == "ha":
#         n += 1
#         continue
#     else:
#         break
# print(mahsulotlar)

# talabalar = ['ali', 'vali', 'husan', 'olim']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba]=baho
# print(baholangan_talabalar)


# cars =['locetti', 'nexia', 'malibu', 'toyota', 'nexia', 'audi']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)


# print("Do'stlaringiz yoshini saqlaymiz ")
# dostlar = {}
# ishora = True
# while ishora:
#     ism  = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot kiritasizmi (ha/yo'q)")
#     if javob =="yo'q":
#         ishora=False
#     for ism, yosh in dostlar.items():
#         print(f"{ism.title()} {yosh} yoshda")




# ismlar = []
# print("Yaqin do'stlaringiz ma'lumotini tuzamiz")
# n=1
# while True:
#     savol =f"{n}-do'stingiz ismini kiriting: "
#     ism=input(savol)
#     ismlar.append(ism)
#     javob =input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())