# list1 = ["abc", 34, True, 40, "male", "male"]
# print(list1)
# print(list1[0])
# print(len(list1))
#
# thisdict = {
#   "brand": "Volvo",
#   "model": "XC 60",
#   "year": 2011
# }
# print(thisdict)
# print(thisdict['brand'])
# print(len(thisdict))
#
# culori = {'alb', 'rosu', 'galben'}
# print(culori)
# print(len(culori))
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(len(thistuple))
#
# #------------------------------------------------
#
# nume = 'Andy'
# nume_as_list = ['A', 'n', 'd', 'y']
# # cum accesam un element
# print(nume_as_list[0])
# # da, merge len
# print(len(nume_as_list))
# # merge slicing? da
# print(nume_as_list[0:2]) # 0, 1
# # cum scoatem un caracter?
# print(nume_as_list.remove('n')) # in f de valoare
# # in f de index (defaut este last pos)
# print(nume_as_list.pop())
# print(nume_as_list)
# # cum suprascriem?
# nume_as_list[0] = 'a'
# # cum adaugam la index?
# nume_as_list.insert(0, 'A')
# print(nume_as_list)
# # cum adaugam la final?
# nume_as_list.append('S')
# print(nume_as_list)
# # cum facem replace? TEMA dupa ce invatam parcurgerea repetitiva a unei liste
#
# # putem pune o lista in alta lista? (lista 2d)
# lista_in_lista = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# # cum afisez 7
# randul_3 = lista_in_lista[2]
# print(randul_3[0])
# # sau
# print(lista_in_lista[2][0])
#
# # sa luam la nimereala
# lista2 = ['tel1', 'tel2', 'tel3', 'tel4']
# import random
# random_nr = random.randint(0, len(lista2)-1)
# # dau click
# print(lista2[random_nr])
# lista3 = ['a', 'n', 'a'] # putem pune valori duplicat
# print(lista3)
#
# # set - avem valori unice, neordonate
# vocale = {'a', 'e', 'i', 'o', 'u'}
# abc = {'a', 'b', 'c'}
# # adaugam duplicat
# before = len(vocale)
# vocale.add('a')
# after = len(vocale)
# if before == after:
#   print('ai adaugat un duplicat')
# print(vocale)
# print(abc.union(vocale))
#
# litera = 'b'
# if litera in vocale:
#   print('litera e vocala')
# else:
#   print('litera e consoana')
# # tupla = nu permite schimbari, permite duplicate, este ordinata
# camere_hotel = (1, 2, 3, 4, 5, 6, 7)
# print(camere_hotel[0])
# print(camere_hotel)
# print(camere_hotel.index(7))
# print(len(camere_hotel))
#
# # dict - structura cheie : valoare
# # nu putem avea chei duplicate
# capitale = {
#   'Romania' : 'Bucuresti',
#   'Ungaria' : 'Budapesta',
#   'Italia' : 'Roma',
#   'Bulgaria' : 'Sofia'
# }
# # putem sa accesam date?
# print(capitale.get('Romania'))
# print(capitale['Romania'])
# # suprascriere/update
# capitale['Romania'] = 'Cluj'
# # adaugare
# capitale['Ucraina'] = 'Kiev'
# # sterge
# capitale.pop('Romania')
# # editare cu update
# print(capitale)
# capilate2 = {'Romania': 'Buc', 'Rusia' : 'Moscova', 'Italia' : 'Milan'}
# capitale.update(capilate2)
# print(capitale)

lista_fructe = ['mar', 'para', 'banana', 'mango', 'ananas']
print(lista_fructe)
print(type(lista_fructe))
print(len(lista_fructe))
ultima_poz = len(lista_fructe) - 1
print(lista_fructe[ultima_poz])
print(lista_fructe[4])
set_fructe = {'mar', 'para', 'banana', 'mango', 'ananas'}
print(set_fructe)
print(len(set_fructe))
set_fructe.add('cirese')
print(set_fructe)
print(len(set_fructe))
before = len(set_fructe)
set_fructe.add('zmeura')
after = len(set_fructe)
if before == after:
  print(set_fructe)


