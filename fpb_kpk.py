angka_1 = int(input('Masukkan angka pertama: '))
angka_2 = int(input('Masukkan angka kedua: '))

# FPB
list_1 = []
list_2 = []

for elemen_1 in range(2,angka_1 + 1):
    if angka_1 % elemen_1 == 0:
        list_1.append(elemen_1)
print(list_1)

for elemen_2 in range(2,angka_2 + 1):
    if angka_2 % elemen_2 == 0:
        list_2.append(elemen_2)
print(list_2)

list_fpb = []
for elemen_fpb1 in list_1:
    for elemen_fpb2 in list_2:
        if elemen_fpb1 == elemen_fpb2:
            list_fpb.append(elemen_fpb1)
# print(list_fpb[-1])

kpk = (angka_1 * angka_2 // list_fpb[-1])

print('FPB = {} | KPK = {}'.format(list_fpb[-1], kpk))