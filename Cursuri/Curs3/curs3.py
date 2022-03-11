'''Recapitulare
sa scrii pe mai multe randuri

'''
nume = 'Andy'
len(nume)
print(len(nume))
nume_as_list = ['A', 'n', 'd', 'y']
# cum accesam un element
print(nume_as_list[0])
print(len(nume_as_list))
print(nume_as_list[0])
print(nume_as_list[0:4])
#cum scoatem un caracter
nume_as_list.remove('n') # in functie de valoare
print(nume_as_list)
# in functie de pozitie
print(nume_as_list.pop())
print(nume_as_list)
# cum supracriem?
nume_as_list[0] = 'a'
# cum adaugam la index?
nume_as_list.insert(0, 'A') # - pe index-ul 0, punem o valoare dorita
print(nume_as_list)
# cum adaugam la final?
nume_as_list.append('S')
print(nume_as_list)
# cum facem replace? Tema dupa ce invatam parcurgerea repetitiva a unei liste
# nume_as_list

#putem pune o lista in alta lista
lista_in_lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# cum afisez 7
print(lista_in_lista[2][0])

# sa luam random
lista2 = ['tel1', 'tel2', 'tel3']
import random
random_nr = random.randint(0, len(lista2)-1)

# set = avem valori unice
vocale = {'a', 'e', 'i', 'o', 'u'}
abc = {'a', 'b', 'c'}
print(abc.intersection())

# adaugam duplicat
vocale.add('a')
print(vocale)
