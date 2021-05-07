def talaba_info(ism, familiya, **malumotlar):
    """ Talaba haqida ma'lumot qaytaruchi funksiya """
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar 
talaba1 = talaba_info('Ulugbek', 'Aminboyev', manzil = 'Shovot', t_yil =1999)
print(talaba1)
# def kopaytma(*sonlar):
#     """Istalgan sonni ko'paytmasini topuvchi funksiya"""
#     kopaytma =1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# print(kopaytma(10,20,30))

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 =avto_info("GM", 'malibu', rang = 'qora', yil = 2019)
# avto2 = avto_info('Kia', 'K5', rang = 'qizil', narx = 35000)
# print(avto2)

# def summa(x,y, *sonlar):
#     """Kiritilgan sonlar yig'indisini topuvchi funksiya """
#     return x+y+sum(sonlar)
# print(summa(1,2,4))


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indi topuchi funksiya"""
#     return sum(sonlar)
# print(summa(22,34,12))


# def summa(*sonlar):
#     """Sonlarning yig'indisi topuvchi funksiya """
#     yigindi = 0
#     for son in sonlar:
#         yigindi +=son
#     return yigindi
# print(summa(1,2))