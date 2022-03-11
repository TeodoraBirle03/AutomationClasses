# b.1
'''variabila = o zona din memoria calculatorului care contine niste date/informatie sau o cutiuta cu un label
 care contine o valoare'''

#b.2 si b.3
# string
nume_copil = 'Alexandru'
print(type(nume_copil))
# integer
varsta = 2
print(type(varsta))
# float
greutate = 22.58
print(type(greutate))
# boolean
prezenta_gradi = True
print(type(prezenta_gradi))

#b.4
# rotunjim valorea var greutate
print(round(greutate))
# suprascriere
greutate = round(greutate)
print(type(greutate))

#b.5
print(f'Copilul din grupa Veveritelor se numeste {nume_copil}.')

print(f'Copilul {nume_copil} are varsta de {varsta} ani.')

print (f'{nume_copil} cantareste {greutate} kg.')

print (f'{nume_copil} a venit azi la gradinita? {prezenta_gradi}')

#b.6
nume = 'Pop'
prenume1 = 'Ion'
prenume2 =  'Vlad'
nume_complet = len(f'{nume}{prenume1}{prenume2}')

print(f'Numele complet are {nume_complet} caractere.')

#b.7
lungimea = 6
latimea = 3
aria = lungimea * latimea
print(f'Aria dreptunghiului este: {aria}')

#b.8
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('alege un numar: '))
print(string[0:-x])
# print(len(string)) - lungimea intregului string

#b.9
string1 = (string[0:5])
#lungime_string = len(string)
#string2 = string[-5:lungime_string] # de la char " ",(pe poz -5) la final
string2 = string[-5:]
string_nou = print(f'{string1}{string2}')

#b.10
print(string.count('the'))

#b.11
print(string.replace('the', 'THE'))

#b.12
index_of_rock = string.index('rock')
print(f'Index of rock: {index_of_rock}') # metoda index gaseste pozitia unei valori specificate
print(string[0:index_of_rock])

#b.13
new_string = input('Introdu string-ul: ')
first_char = new_string[0]
# print(first_char)
last_char = new_string[-1:]
# print(last_char)
assert first_char.casefold() == last_char.casefold() # metoda casefold obliga toate caracterele sa fie mici, iar assert valideaza;

#b.14
string_number = '0123456789'
numar_par = string_number[::2]
print(numar_par)
numar_impar = string_number[1::2]
print(numar_impar)

#b.15 - e variabila de la ex b.8
print(string) # ca sa-mi amintesc string-ul corect
assert string == string.isnumeric() # verifica daca toate caracterele din variabila sunt numerice

