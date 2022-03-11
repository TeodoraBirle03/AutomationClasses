# # # while / else
i = 0
while i <= 3:
    print(i)
    i = i + 1
else: #optional, se executa o singura data la final indiferent daca conditia e true sau false
    print('done')

# # debug = depanare, punem pauza in cod ca sa vedem cum arata un anumit prezent

j = 1
j = j + 10
print(j)

# for/ for else
for i in range(101, 0, -2): #range functioneaza ca un sclicing, de unde incepem, daca nu default 0
    print(i)
else:
    print(f'la iesire din for i are valoarea {i} ')
#
# # sa folosim for pentru a parcurge lista
# culori = ['albastru', 'alb', 'verde', 'rosu', 'alb', 'galben']
# for i in range(len(culori)):
#     print(f'culoarea mea preferata este {culori[i]}')
#
# # for each, trecem prin toate elementele
# for culoare in culori: #pentru fiecare culoare din culori
#     if culoare == 'fuxia':
#         index = culori.index('fuxia')
#         culori[index] = 'magenta'
# print(f'lista de culori actualizate v2 {culori}')

# # acceleram pana ce mai avem benzina
# benzina_ramasa = 5
# consum = 0.5
# while benzina_ramasa > 0:
#     print(f'putem sa acceleram')
#     benzina_ramasa = benzina_ramasa - consum
#     if benzina_ramasa <= 2:
#         print(f'beculet rosu')
#     print(f'mai ai {benzina_ramasa}')
# else:
#     print('Stop, nu mai ai benzina')

# avand o lista de numere reale, afisati doar numele pozitive
numere = [-2, -4, 0, 2, 6, 67, 12]
lista_poz = []

for numar in numere:
    if numar > 0:
        print(f'Numarul pozitiv este: {numar}')
        lista_poz.append(numar)
print(lista_poz)

# for numar in numere:
#     if numar <= 0:
#         continue
#     print(f'Numar pozitiv {numar}')

