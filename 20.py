def fibanachini_tuz(n):
    """Fibanachi ketma-ketligini topuvchi funksiya """
    F = [0]*(n+1)
    F[0]=1
    F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F
n = int(input())
print(fibanachini_tuz(n))  


# def tub_sonlarni_top(a, b):
#     """Berilgan oraliqdagi tup sonlarni topuvchi funksiya """
#     sonlar = []
#     for i in range(a, b + 1):
#         isprime = True
#         for j in range(2, int(i ** 0.5 + 1)):
#             if i % j == 0:
#                 isprime = False
#                 break
#         if i < 2:
#             isprime = False
#         if isprime:
#             sonlar.append(i)
#     return sonlar

# a, b = map(int, input().split())

# print(tub_sonlarni_top(a, b))
    
# prime = [0]*1000001

# for i in range(2, n+1):
#     if ! prime[i]:
#         for j in range(i * i, n + 1, i):
#             prime[j] = 1





# def aylana_info(r):
#     """Aylanani radiusini qabul qilib uning parametrlarini lug'at ko'rinishida qaytaruvchi funksiya"""
#     aylana ={ 'radiusi':r,
#               'diametri':2*r,
#               'perimetri':2*3.14*r,
#               'yuzi':3.14*r**2,
#             }
#     return aylana
# r = float(input("Aylananing radiusini kiriting: "))
# aylana_1 =aylana_info(r)
# print(aylana_1)


# def kattasini_top(a, b, c):
#     """ 3ta son qabul qilib kattasini topuvchi funksiya"""
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# a, b, c = map(int, input().split()) 
# sonlar = kattasini_top(a, b, c)
# print(sonlar)



# def shaxs_info(ism, familiya, t_yil, t_joy, tel_raqam='', email_manzil=''):
#     shaxs ={'ism':ismi,
#             'familya':familiyasi,
#             't_yil':t_yili,
#             't_joy':t_joyi,
#             'tel_raqam':tel_raqami,
#             'email_manzil':email_manzili
#            }
#     return shaxs
# print("Shaxslar haqida m'lumot shakllantiramiz")
# shaxslar = []
# while True:
#     print("\n Quydagi ma'lumotlarni kiriting")
#     ismi = input("Ismi: ")
#     familiyasi = input("Familiyasi: ")
#     t_yili = input("Tug'ilgan yili: ")
#     t_joyi = input("Tugigan joy: ")
#     tel_raqami = input("Tel raqami: ")
#     email_manzili = input("Eamil manzili: ")
#     shaxslar.append(shaxs_info(ismi, familiyasi, t_yili, t_joyi, tel_raqami, email_manzili))
        
#     javob = input("Yana shaxs qo'shasizmi? (yes/no)")
#     if  javob =='no':
#         break  
# print("Shaxslar ro'yxati")
# for shaxs in shaxslar:
#     print(shaxs)

# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None ):
#     avto = {'kamponiya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'karobka':karobka,
#             'yil':yili,
#             'narx':narxi
#            }
#     return avto
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuydagi ma'lumotlarni kiriting")
#     kompaniya = input('Ishlab chiqaruvchi: ')
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narxi = input("Narxi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))

#     javob = input("Yana avtomashina qo'shasizmi? (yes/no)")
#     if javob == 'no':
#         break
# print("Salonimizdagi avtolar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} karobka. Narxi: {narx}")

# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam 
#     return sonlar
# print(oraliq(0,21,2))


# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,15))
# print(oraliq(10,100))

# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None ):
#     avto = {'kamponiya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'karobka':karobka,
#             'yil':yili,
#             'narx':narxi
#            }
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2019)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2018,14000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud mashinalar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']} Narxi: {narx}.")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('hasan','olimov') 
# talaba2 = toliq_ism_yasa('maruf','rustamovich','norimov')
# print(f"Darsga kelmagan o'quvchilar: {talaba1}, {talaba2}.")

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('hasan','olimov') 
# talaba2 = toliq_ism_yasa('maruf','norimov')
# print(f"Darsga kelmagan o'quvchilar {talaba1.title()}, {talaba2.title()}.")