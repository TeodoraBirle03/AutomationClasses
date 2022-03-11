'''Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul
1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
# cazul in care putem introduce numerele de la tastatura, e mai dinamic
x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))
def suma_numere(x,y):
    suma = x + y
    return (f'Suma celor doau numere este: {suma}')

print(suma_numere(x,y))

# cazul in care punem argumentele cand apelam functia
def suma_numere(a,b):
    suma = a + b
    return (f'Suma celor doau numere este: {suma}')

print(suma_numere(8,10))
print(suma_numere(78,10))

'''2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar'''
def par_impar(numar): # definim functia si-i punem parametrul numar
    if numar % 2 == 0: # verificam prin modulo daca este par
        return(f'{numar} este un numar par') # returnam un raspuns
    else:
        return(f'{numar} este un numar impar')

print(par_impar(84))
print(par_impar(75))
'''3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''
def total_caractere(nume, prenume1, prenume2):
    total_string = (nume + prenume1 + prenume2)# punem parametrii intr-un string pt a-l putea parcurge
    total_string = total_string.replace(' ', '')# in cazul in care apar spatii, le eliminam
#   print(f'{total_string}')
    return len(total_string)# dimensiunea stringului ne va returna numarul de caractere

print(total_caractere('Birle', 'Dan ', 'Vasile'))
print(total_caractere('Pop', 'Victor', 'Stefan'))
print(total_caractere('Popescu    ', 'Alex', ' '))

'''4. Functie care returneaza aria dreptunghiului'''

# lungime_input = int(input('Introdu lungimea: '))
# latime_input = int(input('Introdu latimea: '))
def aria_dreptunghi(Lungime, latime):
    arie =  Lungime * latime
    return (f'Aria dreptunghiului este: {arie}')

print(aria_dreptunghi(8, 5))
print(aria_dreptunghi(10, 45))

'''5. Functie care returneaza aria cercului'''

PI = 3.14
def aria_cercului(raza):
    arie_cerc = raza * raza * PI
    return (f'Aria cercului este: {arie_cerc}')

print(aria_cercului(6))
print(aria_cercului(10))
'''6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu'''

string_input = 'abc12311 :&   ABCD1! '
x = input('Introduceti caracterul cautat: ')
def cautare_caracter(string, x):
    contine = False
    nr = 0
    for char in string:
        if char == x:
            contine = True
            nr = nr + 1
    print(f'{x} apare in string de {nr} ori')
    return contine

print(cautare_caracter(string_input, x))

'''7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y '''

string_input = 'abc1ABCD!'
def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
        # else:
        #     print('nu ati introdus litere')
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')

lower_upper(string_input)

'''8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive'''

lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]
lista_numere_pozitive = []

def numere_pozitive(numere):
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return(lista_numere_pozitive)

print(numere_pozitive(lista_numere))


'''9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''

def doua_numere(x, y):
    if x == y:
        print(f'Numerele sunt egale' )
    elif x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    else:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')

doua_numere(89, -5)
doua_numere(7, 46)

'''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''

set_numere_input = {2, 5, 8 ,78, -8, 45}
def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'am adaugat numarul {numar_nou} in set')
        print(set_numere)
        return True

print(adaugare_numar(set_numere_input, 78))
print(adaugare_numar(set_numere_input, 75))


'''c. Optionale (may need google)
11. Functie care primeste o luna din an si returneaza cate zile are acea luna'''

lunile_anului = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
def calendar(luna):
    if luna in lunile_anului:
        return (lunile_anului.get(luna))

print(calendar('June'))
print(calendar('January'))
print(calendar('February'))

'''12. Functie calculator care sa returneze 4 valori
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)'''

'''14. Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele'''

def maxim(x, y, z):
    if x == y == z:
        return ('numerele sunt egale')
    elif x >= y and x >= z:
        return (f'{x} este cel mai mare numar')
    elif y >= x and y >= z:
        return (f'{y} este cel mai mare numar')
    else:
        return (f'{z} este cel mai mare numar')

print(maxim(20, 20, 2))
print(maxim(5, 100, 100))
print(maxim(7, 7, 7))
print(maxim(17, 2, 17))

'''BONUS:16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
'Numele este de baiat' sau 'Numele este de fata'
'''
exceptii_fete = ['Carmen', 'Iris', 'Damaris']
exceptii_baieti = ['Horea', 'Mihnea', 'Horea', 'Toma']

def verificare_nume(nume):
    if nume in exceptii_fete:
        return (f'Numele introdus este de fata')
    elif nume in exceptii_baieti:
        return(f'Numele introdus este de baiat')
    elif nume[len(nume)-1] == 'a':
        return (f'Numele introdus este de fata')
    else:
        return('Numele introdus este de baiat')

print(verificare_nume('Victor'))
print(verificare_nume('Horea'))
print(verificare_nume('Rodica'))
print(verificare_nume('Iris'))