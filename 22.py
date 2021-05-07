def summa(x,y, *sonlar):
    """Kiritilgan sonlar yig'indisini topuvchi funksiya """
    return x+y+sum(sonlar)
print(summa(1,2,4))


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