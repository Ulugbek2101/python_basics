izohli_lugat  = {
'integer':'butun son',
'float':"o'nlik son",
'string':'satr',
'if':'agar sharti',
'else':"aksholda sharti",
'upper':'katta bn yozish',
'lower':'kichik harfla bn yozish',
'title':'birichi sozi katta harfga otkazish'
}
javob =input("kalit so'z kiriting: ").lower()
tarjima =izohli_lugat.get(javob)
if tarjima == None:
    print("Bunday so'z mavjud emas.")
else:
    print(tarjima)









# izohli_lugat  = {
# 'integer':'butun son',
# 'float':"o'nlik son",
# 'string':'satr',
# 'if':'agar sharti',
# 'else':"aksholda sharti",
# 'upper':'katta bn yozish',
# 'lower':'kichik harfla bn yozish',
# 'title':'birichi sozi katta harfga otkazish'
# }
# javob =input("kalit so'z kiriting: ")
# print(izohli_lugat.get(javob,"bunday so'z mavjud emas"))
     







# taom = {
# "ali":'osh',
# 'vali':'norin',
# 'hasan':'manti',
# 'asad':'chuchvara',
# 'husan':"somsa" 
# }
# print(f"Alining sevimli taomi {taom['ali']}.")
# print(f"Hasanning sevimli taomi {taom['hasan']}.")
# print(f"Asadning sevimli taomi {taom['asad']}.")




# otam =  {
#     'ism':'saidov nurulla',
#     't_yil':1971,
#     'manzil':'shovot tumani',
#     'yosh':50
# }
# onam = {
#     'ism':'otajonova muqaddas',
#     't_yil':1974,
#     'manzil':'shovot tumani',
#     'yosh':47
# }
# ukam ={
#     'ism':'aminboyev diyorbek',
#     't_yil':2004,
#     'manzil':"shovot tumani",
#     'yosh':17
# }
# print(f"Otam {otam['ism'].title()} {otam['yosh']} yoshda {otam['t_yil']}-yilda {otam['manzil']}da tug'ilgan.")
# print(f"Onam {onam['ism'].title()} {onam['yosh']} yoshda {onam['t_yil']}-yilda {onam['manzil']}da tug'ilgan.")
# print(f"Ukam {ukam['ism'].title()} {ukam['yosh']} yoshda {ukam['t_yil']}-yilda {ukam['manzil']}da tug'ilgan.")




# telefonlar = {
#     'ali':'iphone X pro',
#     'vali':'samsung A51s',
#     'adham':'redmi note 9s',
#     'mamur':'samsung 20s'
# }
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
# print(phone)






# telefonlar = {
#     'ali':'iphone X pro',
#     'vali':'samsung A51s',
#     'adham':'redmi note 9s',
#     'mamur':'samsung 20s'
# }
# print(telefonlar)




# talaba_0 = {"ism":"aminboyev ulug'bek", "yosh":22, "t_yil":1999 }
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)  






# talaba_1 = {}
# talaba_1['ism'] = 'bekzod raximov'
# talaba_1['kurs'] = 3
# talaba_1['t_yil'] = 2000
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs.")





# talaba_1 = {}
# talaba_1['ism'] = 'bekzod raximov'
# talaba_1['kurs'] = 3
# talaba_1['t_yil'] = 2000
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs.")



# talaba_0 = {"ism":"aminboyev ulug'bek", "yosh":22, "t_yil":1999 }
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = "Telekommunikatsiya"
# print(talaba_0)



# talaba_0 = {"ism":"aminboyev ulug'bek", "yosh":22, "t_yil":1999 }
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-tug'ilgan,\
#  {talaba_0['yosh']} yoishda")




# car_0  ={"model":"ferari", "rang":"qizil"}
# print(car_0["model"])
# print(car_0["rang"])
