restaran = {
    'osh':15000,
    'non':4000,
    'manti':2000,
    "log'mon":1500,
    'cola':8000,
    'limon choy':5000,
    "sho'rva":10000,
    'bisteks':12000,
}
buyurtmalar = []
print("Uchta taom buyurtma qiling.")
for i in range(3):
    buyurtmalar.append(input(f"{i+1}-taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in restaran:
        print(f"{buyurtma.title()} {restaran[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma.title()} yo'q.")







# dav_poytaxt = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington',
#     'qozoqiston':'nursulton',
#     "qirg'iziston":'bishkek',
#     'tojikiston':'dushanbe',
#     'rossiya':'moskva',
#     'italiya':'rim'
# }
# davlat = input("Qaysi davlat haqida bilishni hohlaysiz: ").lower()
# poytaxt = dav_poytaxt.get(davlat)
# if poytaxt ==None:
#     print("Kechirasiz, bu yerda bunday ma'lumot yo'q.")
# else:
#     print(f"{davlat.upper()}ning poytaxti {poytaxt.title()}")


# dav_poytaxt = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington',
#     'qozoqiston':'nursulton',
#     "qirg'iziston":'bishkek',
#     'tojikiston':'dushanbe',
#     'rossiya':'moskva',
#     'italiya':'rim'

# }
# print("Dunyo davlatlari:")
# for davlat in sorted(dav_poytaxt):
#     print(davlat.upper())

# print("\nDavlat poytaxtlari:")
# for poytaxt in sorted(dav_poytaxt.values()):
#     print(poytaxt.title())



# dav_poytaxt = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington',
#     'qozoqiston':'nursulton',
#     "qirg'iziston":'bishkek',
#     'tojikiston':'dushanbe',
#     'rossiya':'moskva',
#     'italiya':'rim'

# }
# print("Dunyo davlatlari:")
# for davlat in sorted(dav_poytaxt):
#     print(davlat.upper())

# print("\nDavlat poytaxtlari:")
# for poytaxt in sorted(dav_poytaxt.values()):
#     print(poytaxt.title())
    




# izohli_lugat = {
#     'Boolean':'Mantiqiy qiymat',
#     'Float':"O'nlik qiymat",
#     'For':"Biror amalni qayta-qayta bajarish tsikli",
#     'If':'Shartlarni tekshirish operatori',
#     'Integer':'Butun son',
#     'Tuple':"O'zgarmas ro'yxat"
# }
# for key, value in izohli_lugat.items():
#     print(f"{key} - {value}.")



# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung A71 S',
#     'hasan':'samsung A20 S',
#     'husan':'redmi 5S',
#     'umar':'samsung 20 S',
#     'maruf':'iphone x'
# }
# for telefon in set(telefonlar.values()):
#     print(telefon.title()) 


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung A71 S',
#     'hasan':'samsung A20 S',
#     'husan':'redmi 5S',
#     'umar':'samsung 20 S'
# }
# for telefon in telefonlar.values():
#     print(telefon.title()) 


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung A71 S',
#     'hasan':'samsung A20 S',
#     'husan':'redmi 5S',
#     'umar':'samsung 20 S'
# }
# print(telefonlar.values())


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'behi':8000,
#     'gilos':12000,
#     'banan':22000
# }
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())



# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'behi':8000,
#     'gilos':12000,
#     'banan':22000
# }
# bozorlik =['olma', 'anor', 'banan', 'non']
# for buyum  in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, {buyum} olib keling.")


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'behi':8000,
#     'gilos':12000,
#     'banan':22000
# }
# bozorlik =['olma', 'anor', 'banan', 'non']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm.")



# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'behi':8000,
#     'gilos':12000,
#     'banan':22000
# }
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'behi':8000,
#     'gilos':12000,
#     'banan':22000
# }
# print(mahsulotlar.keys())


# telefonlar = {
#     'ali':'iphone 12 pro',
#     'vali':'samsung s20 ultira',
#     'hasan':'redmi note 9',
#     'husan':'samsung A51s'
# }
# for key, vaule in telefonlar.items():
#     print(f"{key}ning telefoni {vaule}.")


# talaba_0 = {
#     'ism':'Ulugbek',
#     'familiya':'Aminboyev',
#     'yosh':22,
#     'fakultet':'telekommunikatsiya'
# }
# for kalit, qiymat in talaba_0.items():
#     print(f'Kalit:',kalit)
#     print(f'Qiymat',qiymat)



# talaba_0 = {
#     'ism':'Ulugbek',
#     'familiya':'Aminboyev',
#     'yosh':22,
#     'fakultet':'telekommunikatsiya'
# }
# print(talaba_0.items())