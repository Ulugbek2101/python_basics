def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
    """Avtomobil haqidagi ma'lumotlarni funksiya ko'rinishidagi qaytaruvchi funksiya"""
    avto ={'kompaniya':kompaniya,
           'model':model,
           'rang':rangi,
           'korobka':karobka,
           'yil':yili,
           'narx':narxi}
    return avto
def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar = []
    while True:
        print("\nQuydagi ma'lumotlarni kiriting", end="")
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi =input("Rangi: ")
        korobka =input("Karobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narx=input("narxi: ")
        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narxi))
        javob =input("Yana mashina qo'shasizmi? (yes/no)")
        if javob!='yes':
            break
    return avtolar
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")
