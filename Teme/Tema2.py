#b.1
# if (daca conditia este indeplinita) atunci se executa codul else (altfel) conditia nu e indeplinita
# else nu mai are nevoie de conditie pentru ca se executa ce a mai ramas,
# avand in vedere ca conditia nu a fost indeplinita
# if + conditia e urmata de :

#b.2
x =int(input('Introdu un numar: '))
if x >= 0:
    print(f'{x} este numar natural')
else:
    print(f'{x} este numar negativ')

#b.3
x =int(input('Introdu un numar: '))
if x == 0:
    print(f'{x} este numar neutru')
elif x > 0:
    print(f'{x} este numar pozitiv')
else:
    print(f'{x} este numar negativ')

#b.4
LIMITA_MIN = -2
LIMITA_MAX = 23
if x >= LIMITA_MIN and x<= LIMITA_MAX:
    print(f'{x} este cuprins intre {LIMITA_MIN} si {LIMITA_MAX}')
else:
    print (f'{x} este inafara limitelor stabilite')

#b.5
y = int(input('Introdu un al doilea numar: '))
CONS = 5
if x - y < CONS:
    print(f'diferenta este mai mica decat {CONS}')
else:
    print (f'diferenta este mai mare sau egala cu {CONS}')

#b.6
x =int(input('Introdu un numar: '))
if not(x >= 5 and x <= 27):
    print(f'{x} nu este cuprins intre 5 si 27')
else:
    print(f'{x} este cuprins intre 5 si 27')

# b.7
x =int(input('Introdu un numar: '))
y = int(input('Introdu un al doilea numar: '))
if x == y:
        print(f'{x} este egal cu {y}')
elif x > y:
        print(f'{x} este cel mai mare')
else:
        print(f'{y} este cel mai mare')

#b.8
a = int(input('Introdu prima latura: '))
b = int(input('Introdu a doua latura: '))
c = int(input('Introdu a treia latura: '))
if a == b == c:
    print('Triunghiul este echilateral')
elif a == b and a != c or a != b and b == c or a != b and a == c:
    print ('Triunghiul este isoscel')
else:
    print ('Triunghiul este oarecare')

#b.9
litera = input('Introdu o litera: ')# aici se poate folosi si casefold, care facem toate literele mici cand le introduci de la tastatura
vocale = 'a,e,i,o,u'
if litera.lower() == 'a' or litera.lower() == 'e' or litera.lower() == 'i' or litera.lower() == "o" or litera.lower() == 'u':
    print(f'{litera} este o vocala')
else:
    print(f'{litera} este o consoana')

#b.10
nota = int(input('Introdu nota: '))
if nota >= 9 and nota <= 10:
    nota_us = 'A'
    print(f'ai luat un: {nota_us}')# la 9 si 10, afiseaza A
elif nota >= 8 and nota < 9:
    nota_us = 'B'
    print(f'ai luat un: {nota_us}')# la 8, afiseaza B
elif nota >= 7 and nota < 8:
    nota_us = 'C'
    print(f'ai luat un: {nota_us}')# la 7, afiseaza C
elif nota >= 6 and nota < 7:
    nota_us = 'D'
    print(f'ai luat un: {nota_us}')# la 6, afiseaza D
elif nota >= 4 and nota < 6:
    nota_us = 'E'
    print(f'ai luat un: {nota_us}')# la 5 si 4, afiseaza D
elif nota < 4 and nota >= 1:
    nota_us = 'F'
    print(f'ai luat un: {nota_us}')# la 3,2,1, afiseaza F
else:
    print(f'{nota} nu este o valoare valida')

#c.11
x_c = int(input('Introdu un numar: '))
x_c_string = (f'{x_c}')
nr_cifre = len(x_c_string)
# print(type(x_c_string)) - am verificat ce tip de date are var x_c_string
if len(x_c_string) >= 4:
   print(f'{x_c} are {nr_cifre} cifre')
if x_c >= 1000:
    print(f'{x_c} are minim 4 cifre')


#c.12
#if len(x_c_string) == 6:
#    print(f'{x_c} are exact {nr_cifre} cifre')
if x_c >= 100000 and x_c < 1000000:
    print(f'{x_c} are exact 6 cifre')

#c.13
if x_c % 2 == 0:
    print (f'{x_c} este numar par')
else:
    print (f'{x_c} este numar impar')

#c.14
x_c = int(input('Introdu primul numar: '))
y_c = int(input('Introdu al doilea numar: '))
z_c = int(input('Introdu al treilea numar: '))
if x_c == y_c == z_c:
    print('numerele introduse sunt egale')
elif x_c >= y_c and x_c >= z_c:
    print(f'{x_c} este cel mai mare numar')
elif y_c >= x_c and y_c >= z_c:
    print(f'{y_c} este cel mai mare numar')
else:
    print(f'{z_c} este cel mai mare numar')

#c.15
x15 = int(input(f'Introdu unghiul x: ' ))
y15 = int(input(f'Introdu unghiul y: ' ))
z15 = int(input(f'Introdu unghiul z: ' ))
sum_unghiuri = x15 + y15 + z15
if sum_unghiuri == 180 and x15 > 0 and y15 > 0 and z15 > 0:
    print('acesta este un triunghi valid')
else:
    print('acesta este un triunghi invalid')

#c.16
pasaport = True
if pasaport == False:
    print('Pasagerul nu se poate imbarca, nu are pasaport')
else:
    varsta = int(input('Introduceti varsta pasagerului: '))
    if varsta >= 18:
        print('Pasagerul se poate imbarca')
    else:
        cu_mama = True
        cu_tata = False
        permisiune_mama = True
        permisune_tata = True
        if cu_mama ==True and cu_tata == True:
            print('Pasagerul se poate imbarca, e cu ambii parinti')
        elif cu_mama == True and cu_tata == False and permisune_tata == True:
            print('Pasagerul se poate imbarca, e cu mama si acord tata')
        elif cu_mama == False and cu_tata == True and permisiune_mama == True:
            print('Pasagerul se poate imbarca, e cu tata si acord mama')
        else:
            print('Pasagerul nu se poate imbarca, e minor si nu indeplineste toate conditiile')

# 17. Joc ghicit zarul - doar am inteles logica, rezolvat de Isa
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
import random # random = genereaza intamplator diferite variabile
dice_roll = random.randint(1,6)

# Luati un nr ghicit de la utilizator
x = int(input('Alegeti un numar dat cu zarul, de la 1 la 6: '))

# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
if x < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x}, dar a fost {dice_roll}.')
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
elif x > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x}, dar a fost {dice_roll}.')
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y
else:
    print(f'Ai ghicit. Felicitari? Ai ales {x} si zarul a fost {dice_roll}.')