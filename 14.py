davlatlar = {
       "o'zbekiston":{'poytaxt':'toshkent',
                      'hududi':448978,
                      'aholisi':33000000,
                      'pul birligi':"so'm"
                     },
       'rossiya':{'poytaxt':'moskva',
                  'hududi':17098246,
                  'aholisi':1440000000,
                  'pul birligi':'rubl'
                 },
       'aqsh':{'poytaxt':'vashington',
               'hududi':9631418,
               'aholisi':327000000,
               'pul birligi':'dollar'
              },          
      'malaziya':{'poytaxt':'kuala-lumpur',
                   'hududi':329750,
                   'aholisi':25000000,
                   'pul birligi':'rinngit'
                  }
}       
davlat = input("Davlat nomini kiriting: ").lower()        
if davlat in davlatlar:
       info = davlatlar[davlat]
       print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
             f"\nHududi: {info['hududi']} kv.km"
             f"\nAholisi: {info['aholisi']} "
             f"\nPul birligi: {info['pul birligi']}")
else:
       print("Bizda bu davlat haqida ma'lumot mavjud emas")



# davlatlar = {
#        "O'zbekiston":{'poytaxt':'toshkent',
#                       'hududi':448978,
#                       'aholisi':33000000,
#                       'pul birligi':"so'm"
#                      },
#        'rossiya':{'poytaxt':'moskva',
#                   'hududi':17098246,
#                   'aholisi':1440000000,
#                   'pul birligi':'rubl'
#                  },
#        'aqsh':{'poytaxt':'vashington',
#                'hududi':9631418,
#                'aholisi':327000000,
#                'pul birligi':'dollar'
#               },          
#       'malaziya':{'poytaxt':'kuala-lumpur',
#                    'hududi':329750,
#                    'aholisi':25000000,
#                    'pul birligi':'rinngit'
#                   }
# }               
# for davlat, info in davlatlar.items():
#        if davlat.lower =='aqsh':
#               davlat=davlat.upper()
#        else:
#               davlat=davlat.capitalize()
#        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#              f"\nHududi: {info['hududi']} kv.km"
#              f"\nAholisi: {info['aholisi']} "
#              f"\nPul birligi: {info['pul birligi']}")
       


# kino = {
#        'ali':['Terminator','Rambo','Titanic'],
#        'vali':['Tenet','Inception','Interstellar'],
#        'hasan':['Abdullajon','Bomba','Shaytanat'],
#        'husan':['Mahallada duv-duv gap', 'John Wick']
# }
# for ism, kinolar in kino.items():
#        print(f'{ism.title()}ning sevimli kinolari: ')
#        for kin in kinolar:
#               print(kin.capitalize())



# shaxs_1 ={
#        'ismi':'Abu Abdulloh Muhammad ibn Ismoil',
#        'asarlar':["Al-jome' as-sahih", 'Al-adab al-mufrad', 'Al-tarix al-kabir', "Al-tarix al-sag'ir"]
# }
# shaxs_2 ={
#        'ismi':'Abdulla Qodiriy',
#        'asarlar':["O'tkan kunlar", 'Mehrobdan Chayob', 'Obid ketmon']
# }
# shaxs_3 = {
#        'ismi':'Erkin Vohidov',
#        'asarlar':['Tong nafasi', "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]

# }
# shaxs_4 = {
#        'ismi':'Alisher Navoiy',
#        'asarlar':['Xamsa','Liso ut-Tayr', 'Mahbub Al-Qulub', 'Munojat']
# }
# shaxslar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4]
# for shaxs in shaxslar:
#        print(f"{shaxs['ismi']} ning mashxur asarlari: ")
#        for asar in shaxs['asarlar']:
#               print(asar)




# shaxs_1 ={
#        'ismi':'Abu Abdulloh Muhammad ibn Ismoil',
#        't_yil':810,
#        't_yeri':'Buxoro',
#        'umri':60,
# }
# shaxs_2 ={
#        'ismi':'Abdulla Qodiriy',
#        't_yil':1894,
#        't_yeri':"Toshkent",
#        'umri':44
# }
# shaxs_3 = {
#        'ismi':'Erkin Vohidov',
#        't_yil':1936,
#        't_yeri':"Fargo'ona",
#        'umri':80
# }
# shaxs_4 = {
#        'ismi':'Alisher Navoiy',
#        't_yil':1441,
#        't_yeri':'Hirot',
#        'umri':60
# }
# shaxslar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4]
# for shaxs in shaxslar:
#        print(f"{shaxs['ismi']} {shaxs['t_yil']}-yilda"
#        f"{shaxs['t_yeri']} tavallud topgan. "
#        f"{shaxs['umri']} yil umr ko'rgan."
#        )


# hamkasblar ={
#     'ali':{'familiya':'olimov',
#            't_yil':1995,
#            'malumot':'oliy',
#            'tillar':['pyhon','c++']                  
#            },
#     'vali':{'familiya':'murodov',
#              't_yil':2000,
#              'malumot':"o'rta maxsus",
#              'tillar':['html','css','js'] 
#              },
#     'hasan':{'familiya':'ozodov',
#              't_yil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']    
#              },       
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#     f"{info['t_yil']}-yilda tug'ilgan. "
#     f"Ma'lumoti: {info['malumot']}. \n"
#     "Quydagi dasturlash tillarini biladi: ")
#     for til in info['tillar']:
#            print(til.upper())

# dasturchilar = {
#     'ali':['python','C++'],
#     'vali':['html','css','js'],
#     'husan':['python','php'],
#     'hasan':['php','sql'],
#     'maryam':['c++','c#']
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi daturlash tillarni biladi: ", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')


# malibus = []
# for n in range(10):
#     new_car ={
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'karobka':'avtomat'
#          }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang'] ='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['karobka'] = 'mexanika'
# for malibu in malibus:
#     if malibu['karobka'] == 'avtomat':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx'] = 35000
# for malibu in malibus:
#     print(malibu )


# car_0 = {
#     'model':'locetti',
#     'rang':'oq',
#     'yil':'2018',
#     'narx':'13000',
#     'km':'5000',
#     'karobka':'avtomat'
# }

# car_1 = {
#     'model':'cobalt',
#     'rang':'kulrang',
#     'yil':'2020',
#     'narx':'11000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# car_2 = {
#     'model':'spark',
#     'rang':'qizil',
#     'yil':'2017',
#     'narx':'8000',
#     'km':'6000',
#     'karobka':'mexanik'
# }

# car_3 = {
#     'model':'malibu',
#     'rang':'qora',
#     'yil':'2020',
#     'narx':'30000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# cars = [car_0, car_1, car_2, car_3]
# print(cars[0])
# print(cars[0]['model'])

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}"  )

# car_0 = {
#     'model':'locetti',
#     'rang':'oq',
#     'yil':'2018',
#     'narx':'13000',
#     'km':'5000',
#     'karobka':'avtomat'
# }

# car_1 = {
#     'model':'cobalt',
#     'rang':'kulrang',
#     'yil':'2020',
#     'narx':'11000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# car_2 = {
#     'model':'spark',
#     'rang':'qizil',
#     'yil':'2017',
#     'narx':'8000',
#     'km':'6000',
#     'karobka':'mexanik'
# }

# car_3 = {
#     'model':'malibu',
#     'rang':'qora',
#     'yil':'2020',
#     'narx':'30000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# cars = [car_0, car_1, car_2, car_3]
# for car in cars:
#     print(f"{car['model'].title()} "
#         f"{car['rang']} rang, "
#         f"{car['yil']}-yil {car['narx']}$")



# car_0 = {
#     'model':'locetti',
#     'rang':'oq',
#     'yil':'2018',
#     'narx':'13000',
#     'km':'5000',
#     'karobka':'avtomat'
# }

# car_1 = {
#     'model':'cobalt',
#     'rang':'kulrang',
#     'yil':'2020',
#     'narx':'11000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# car_2 = {
#     'model':'spark',
#     'rang':'qizil',
#     'yil':'2017',
#     'narx':'8000',
#     'km':'6000',
#     'karobka':'mexanik'
# }

# car_3 = {
#     'model':'malibu',
#     'rang':'qora',
#     'yil':'2020',
#     'narx':'30000',
#     'km':'2000',
#     'karobka':'avtomat'
# }

# car = car_0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil {car['narx']}$")

# car = car_1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil {car['narx']}$")

# car = car_2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil {car['narx']}$")

# car = car_3
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil {car['narx']}$")