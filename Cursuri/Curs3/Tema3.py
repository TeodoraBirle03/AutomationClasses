''' b.1
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
'''
note_muzicale = ['do','re', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

note_muzicale[::-1]# desi i-am facut slicing si am pus-o de la coada la cap, lista se afiseaza ca cea initiala
note_muzicale = note_muzicale[::-1] # aici suprascriem lista initiala cu cea inversata si apoi o printam inversata
print(note_muzicale)

note_muzicale.reverse()# functia reverse face slicing si suprascriere in acelasi timp, nu se salveaza intr-o variabila
print(note_muzicale)

'''b.2. De cate ori apare ‘do’?'''
print(note_muzicale.count('do'))

'''b.3
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista.
Afisati lista ordonata astfel [0,1,2,3,4,5,6]
'''
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# lista1.extend(lista2)
# print(lista1)
lista_ordonata = lista1 + lista2
print(lista_ordonata)

lista_ordonata.sort() # sort ordoneaza elementele listei crescator
print(lista_ordonata)

#lista1.append(lista2) # append-ul adauga pe ultimul index lista2, nu valorile din lista2
#print(lista1)

'''b.4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
'''
lista_ordonata.sort()
print(lista_ordonata)
lista_ordonata.remove(0)
print(lista_ordonata)
# lista_ordonata.reverse()# aceasta functie pune elementele listei in ordine descrescatoare
# print(lista_ordonata)

'''b.5.
Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala'''

if len(lista_ordonata) >= 1:
    print('Lista are elemente')
else:
    print('Lista este goala')

'''b.6
Folositi o functie care sa stearga lista de la ex3
   b.7.
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala
'''
lista_ordonata.clear()
print(lista_ordonata)
if len(lista_ordonata) == 0:
    print('Lista este goala')
else:
    print('Lista are elemente')

'''b.8.
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)'''
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5}
print(dict1.keys())

'''b.9
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
'''
print(f'Ana a luat nota: ', (dict1['Ana']))
print(dict1.get('Ana')) #functia get ia valoarea din dic in funtie de cheie
print(f'Gigel a luat nota: ', (dict1['Gigel']))
print(dict1.get('Gigel'))
print(f'Dorel a luat nota: ', (dict1['Dorel']))
print(dict1.get('Dorel'))

'''b.10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
'''
dict1['Dorel'] = 6 # este o suprascriere
print(dict1)

'''b.11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi
'''
dict1.pop('Gigel')# il scoate din dic
print(dict1)
dict1['Ionica'] = '9' # il adauga pe Ionica in dic
print(dict1)

'''b.12.Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

# nu poti duplica o valoare existenta, deci nu o sa se afiseze luni*2ori
zile_sapt.add('aici')

before = len(zile_sapt)
zile_sapt.add('luni')
after = len(zile_sapt)
if before == after:
    print('ai adaugat un duplicat')

print(zile_sapt)
print(len(zile_sapt))
'''b.13
Folositi un if si verificati daca
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt
'''
if weekend.issubset(zile_sapt):
    print('weekend este un subset al zilelor sapt')
else:
    print('weekend NU este un subset al zilelor sapt')

'''b.14.
Afisati diferentele dintre aceste 2 seturi
'''
diferenta = zile_sapt.difference(weekend)
print(diferenta)

'''b.15.
Afisati intersectia elementelor din aceste 2 seturi
'''
intersectia = zile_sapt.intersection(weekend)
print(intersectia)

'''16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”'''

lista_jucatori = {'jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5'}
print(lista_jucatori)
jucator_in = 'jucator2'
jucator_out = 'jucator8'
schimbari_efectuate = 1
SCHIMBARI_MAX = 3
schimbari_ramase = SCHIMBARI_MAX - schimbari_efectuate
#print(schimbari_ramase)
if jucator_out in lista_jucatori and schimbari_ramase > 0:
    if jucator_in in lista_jucatori: # eliminam cazul cand jucatorul este deja in teren;
        print(f'Nu putem face schimbarea deoarece jucatorul introdus este deja in teren')
    else: # cazul valid, happy flow
        lista_jucatori.remove(jucator_out)# scoatem din teren acest jucator
        lista_jucatori.add(jucator_in)# introducem in teren acest jucator
        print(lista_jucatori)
        print(f'Schimbare efectuata cu succes!')
        schimbari_ramase = schimbari_ramase - 1 #contorizam schimbarea
        print(f'A intrat {jucator_in} a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('nu mai aveti dreptul la alte schimbari')
    else:
        print(f'{jucator_out} nu este in teren, nu se poate face schimbarea')
print(f'echipa este: {lista_jucatori}')

