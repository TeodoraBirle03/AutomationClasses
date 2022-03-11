'''1.Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# cazul cu for simplu
for masina in range(len(masini)):
    print(f'Masina mea preferata este: {masini[masina]}')

# cazul cu for each
for masina in masini:
    print(f'Masina mea preferata este: {masina}')

# cazul cu while
i = 0 # acesta este indexul
while i < len(masini): # atata timp cat index-ul este mai mic decat numarul elementelor din lista
    print(f'Masina mea preferata este: {masini[i]}')
    i = i + 1
else:
    print(f'Esti pretentios')

'''2.Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
In else
   Printati lista
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
prima_masina = masini[0]
print(prima_masina)
ultima_masina = masini[len(masini)-1]
print(ultima_masina)
for masina in range(1,len(masini)-1): # ne deplasam de la a doua poz pana la penultima
    masini[masina] = masini[masina].upper() # facem pentru toate aceste elemente litere mari
else:
    print(masini)#printam lista modificata

'''3. Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin modalitatea aleasa de voi
Daca masina e mercedes 
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:# iteram lista
    if masina == 'Mercedes': # daca gasim ca masina are valoarea Mercedes
        print(f'am gasit masina dorita de dvs {masina}')
        break
    else:
        print(f'Nu am gasit masina Mercedes.Mai cautam')

'''4.Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
Iterati prin lista
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
(nu trebuie else)
Printati S-ar putea sa va placa masina x
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

'''5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = [] # initializam o lista noua, goala

for masina in masini: #iteram lista masini
    if masina == 'Lastun' or masina == 'Trabant':# cand intalnim valorile Lastun sau Trabant
        masini_vechi.append(masina)# le adaugam in lista nou creata
        index = masini.index(masina)# identificam pozitia valorilor Lastun si Trabant
        masini[index] = 'Tesla'# aici le suprascriem cu valoare tesla in lista masini
print(masini_vechi)
print(masini)

'''6. Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
'''
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items(): # iteram prin dict, cu masina si pret
    if pret <= buget:# punem conditia
        print(f'Pentru un buget de sub 15000 euro puteti alege masina: {masina}')
        # afisam doar masinile care indeplinesc conditia

'''7.Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

x = 0 # variabila care numara de cate ori apare 3
for numar in numere: # iteram lista
    if numar == 3: # cand gasim valoarea 3
      x = x + 1 # se numara in aceasta valoare
print(f'Numarul 3 apare de {x} ori in lista de numere')

'''8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0 #initializam o variabila care sa contina suma
for numar in numere: #iteram lista
    suma = suma + numar # adaugam la valoarea sumei, valoarea numar
print(f'Suma numerelor din lista este: {suma}')

'''9.Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este: {max}')

'''10.Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0 : # punem conditia ca pentru numerele pozitive
        numar = (-abs(numar)) # functie care transforma numarul sau
        #numar = numar * (-1)
        lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')
# dar acum lista contine doar valorile poz care au devenit neg, fara 0 si -4

'''11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este:, {numere_pare}')
print(f'Lista cu numere impare este:,{numere_impare}')
print(f'Lista cu numere pozitive este:,{numere_pozitive}')
print(f'Lista cu numere negative este:,{numere_negative}')

'''12.Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4'''
