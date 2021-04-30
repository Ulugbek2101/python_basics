savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if  qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")



# savol = "Yoshingiz nechada? "
# savol += "(dasturni to'xtatmoqi bo'lsangiz 'stop' yoki 'exit' buyrug'ini yozing)"
# while True:
#     qiymat = input(savol)
#     if qiymat =='exit' or qiymat =='stop':
#         break
#     yosh =int(qiymat)
#     if yosh < 7:
#         print("Muzeyga kirish 2000 so'm")
#     elif 7<= yosh <18:
#         print("Muzeyga kirish 3000 so'm")
#     elif 18<= yosh <65:
#         print("Muzeyga kirish 10000 so'm ")
#     elif 65 <= yosh:
#         print("Muzeyga kirish bepul")
#     elif  str(yosh) == 'exit' or str(yosh) =='stop':
#         break


# savol = "Yaxshi ko'rgan kitobingizni kiriting: "
# savol += "(dasturni to'xtatish uchun 'stop' deb yozing)"
# ishora =True
# while ishora:
#     qiymat = input(savol)
#     if qiymat=='stop':
#         ishora =False

# son=0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")




# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")



# print("Kiritilgan sonni kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)


# print("Kiritilgan sonni kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)



# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kirting"
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)


# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son+1



# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechada? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# heigt = float(height)


# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechada? "
# javob = input(savol)

# ism = input("Ismingiz nima? ")
# print(f"Salom, {ism.title()}")