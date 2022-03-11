# # functii
# def say_hi():
#     print('Hi!')
#
# say_hi()
# say_hi()
# # functii simple
# #functii cu parametrii
#
# # nume si prenume sunt parametrii
# def say_hi_user(name, prenume):
#     prenume = prenume.upper()
#     print(f'Hi {name} {prenume}!')
#
# # Ana, Ionel sunt argumente
# say_hi_user('Ana', 'ana')
# say_hi_user('Ionel', 'Ionel')
#
# #functii cu return
# #input: 5 numere
# #output: ne dorim un set
# def make_set(n1, n2, n3):
#     r = set()
#     r.add(n1)
#     r.add(n2)
#     r.add(n3)
#     return r
#
# set1 = make_set(1,2,2)
# set2 = make_set(1,2,3)
#
# print(set1.intersection(set2))
#
# #cand apelez functia eu deja trebuie sa vizualizez rezultatul, in mintea mea
# print(make_set(1,2,3).intersection(make_set(2, 3, 3)))
#
# # functie cu return dar fara parametrii
# def pi_value():
#     return 3.14
#
# x = pi_value() + 4
# print(x)
# # import doar ce am nevoie, functia de care am nevoie
# from Folder1.helpers import suma
# print(suma(3, 4))
#
# # import tot din helpers
# from Folder1.helpers import *
# print(suma(3, 4))
#
# # calculator de impozit in functie de cm3
#
# cc = int(input('Alege centrimetrii cubi: '))
# impozit = None
# def calcul_impozit(cc_input, hybrid_input ):
#     if hybrid_input == True:
#         return 10
#     else:
#         if cc_input < 1000:
#             return 70
#         elif cc_input < 2000:
#             return 160
#         else:
#             return 900
#
# # apelam functia
# impozit = calcul_impozit(cc, False)
# print(impozit) # cc = 49 rezulta 70
# impozit = calcul_impozit(2400, False)
# print(impozit) # 900
# impozit = calcul_impozit(2400, True)
# print(impozit) # 10

# avem o masina, calculam % procentul de benzina ramasa, la mai putin de 15% se aprinde beculetul rosu, pe return un procent

# REZERVOR = 50
# cantitate_benzina = float(input('Introdu cantitatea de benzina: '))
# def consum_benzina(cantitate_benzina):
#     if cantitate_benzina == 0:
#         return ('Caut-o sticla')
#     elif cantitate_benzina < 7.5:
#         return ('Atentie, cauta o benzinarie')
#     else:
#         return ('Vrummm, Vruummm')
#
# print(consum_benzina(cantitate_benzina))

benz = int(input('Benzina ramasa:'))
benz_ramasa = None
REZERVOR = 50
def benzina_ramasa(benzina_input):
    if benzina_input > REZERVOR:
        print('Nu poti avea mai multi l decat capacitatea max')
        return 'N/A'
    if benzina_input < 0:
        print('Nu poti avea valori negative')
        return 'N/A'
    procentaj_benz = benzina_input/REZERVOR * 100
    print(procentaj_benz)
    if procentaj_benz <= 15:
        print('Warning')
    return procentaj_benz


