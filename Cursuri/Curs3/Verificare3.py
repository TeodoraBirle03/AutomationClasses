
# lista2 = ['tel1', 'tel2', 'tel3', 'tel4']
# import random
# random_nr = random.randint(0, len(lista2)-1)
# print(lista2[random_nr])

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

lista_jucatori = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5']
print(lista_jucatori)
jucator_schimbat = 'jucator1'
schimbari = [0, 1, 2, 3]
print(schimbari)
schimbari_efectuate = 3
schimbari_maxime = 3
schimbari_ramase = schimbari_maxime - schimbari_efectuate
#print(schimbari_ramase)
if jucator_schimbat in lista_jucatori and schimbari_efectuate in schimbari:
    print('jucatorul poate fi schimbat')
    lista_jucatori.remove(jucator_schimbat)
    print(lista_jucatori)
    jucator_nou = 'jucator6'
    lista_jucatori.append(jucator_nou)
    print(lista_jucatori)
    print(f'A intrat {jucator_nou} a iesit {jucator_schimbat}, mai aveti', schimbari_ramase, 'schimbari')
else:
    print('jucatorul nu e pe teren')
    if schimbari_ramase <= 0 or schimbari_ramase > 3:
        print('nu mai aveti dreptul la alte schimbari')



