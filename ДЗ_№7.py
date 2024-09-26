# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
#
# designations = []
# codes = []
#
# for item in data:
#     if item.isdigit():
#         codes.append(item)
#     else:
#         designations.append(item)
#
# operators = dict(zip(designations, codes))
#
# del operators['Katel']
# del operators['Fonex']
#
# operators["O!"] = {'0705', '0700', '0500'}
# operators["Megacom"] = {'0550', '0999', '0555'}
# operators["Beeline"] = {'0770', '0222', '0777'}
#
# for key, value in operators.items():
#     print(f"{key} - {value}")

# print(len("geeks"))
# print(100 if 300 // 2 == 150 else 200)


# print(float("python"))

# print("996" + "312" + 1991)

# g = ['Бишкек', 'Ош', 'Кара', 'Бишкек 9мкр']
# g.sort()
# g = [i.upper() for i in g]
#
# g = g[::-1]
# print(g)

counter = 5

while counter != 0:
    print('as')
    counter -= 1