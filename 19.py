# def bolinish_alomatlari(n):
#     """Sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshirish """
#     for i in range(2,11):
#         if n%i == 0:
#             print(f"{n} {i} ga qoldiqsiz bo'linadi.")

# son = int(input("Istalgan sonni kiriting: ")) 
# bolinish_alomatlari(son)

# def daraja_kotar(x, y=2):
#     """x ninng y-darajasini topuvchi funksiya"""
#     print(f"x ning y darajasi {x**y} teng.")
# son1 = int(input("x sonini kiriting: "))
# daraja_kotar(son1)


# def daraja_kotar(x, y):
#     """x ninng y-darajasini topuvchi funksiya"""
#     print(f"x ning y darajasi {x**y} teng.")
# son1 = int(input("x sonini kiriting: "))
# son2 = int(input("y sonini kiriting: "))
# daraja_kotar(son1,son2)


# def taqqosla(son1, son2):
#     """2 ta sonni taqqoslovchi funksiya"""
#     if son1>son2:
#         print(f"Katta son {son1}")
#     elif son1<son2:
#         print(f"Katta son {son2}")
#     else:
#         print("Sonlar teng.")
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# taqqosla(x, y)




# def sonni_juft_toqlikka_tekshir(son):
#     """Sonni juft toqlikka tekshiruvchi funksiya"""
#     if son%2==0:
#         print(f"{son} juft son.")
#     else:
#         print(f"{son} toq son.")
# sonn = int(input("Istalgan sonni kiriting: "))
# sonni_juft_toqlikka_tekshir(sonn)


# def darajani_hisobla(son):
#     """Sonni kvadrati va kubini chiqaruvchi funksiya """
#     print(f"{son} ning kvadrati {son**2} teng.\n"
#           f"{son} ning kubi {son**3} teng.")
# sonn = int(input("Istalgan sonni kiriting: "))
# darajani_hisobla(sonn)


# def yosh_hisobla(ism, yosh):
#     """Foydalanuvchi ism yoshi orqali tug'ilgan yilini topish"""
#     print(f"{ism.title()} {2021-yosh}-yilda tug'ilan.")
# ismm =input("Ismingizni kiriting: ")
# yoshsh = int(input("Yoshingizni kiriting: "))
# yosh_hisobla(ismm, yoshsh)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
#     """Foydalanuvchi tug'ilgan yilidan yoshini topuvchi funksiya"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
# yosh_hisobla(1999)




# def yosh_hisobla(ism='ulugbek', tugilgan_yil=1999):
#     """Foydalanuvchning yoshini hisoblovchii funksiya"""
#     print(f"{ism.title()} {2021-tugilgan_yil} yoshda")
# yosh_hisobla()




# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchning yoshini hisoblovchii funksiya"""
#     print(f"{ism.title()} {2021-tugilgan_yil} yoshda")
# yosh_hisobla('ulugbek', 1999)




# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('olim', 'hamidov')



# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')
# salom_ber('olim')


# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#      unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')
# print(salom_ber.__doc__)



# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')


# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()