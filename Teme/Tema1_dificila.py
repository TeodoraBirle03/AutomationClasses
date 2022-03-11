#c.18
string18 = input('Introdu un string: ')
x = string18.split()
print(len(x))
print(x)


#c.16
import math
string_impar = input('Introdu un string de dimensiune impara: ')
char_mijloc = math.floor(len(string_impar)/2)
# print(f'mijloc={char_mijloc} din total={len(string_impar)}') afisez index-ul caracterului din mijloc
print(string_impar[char_mijloc:char_mijloc+1])

#c.19
string4 = input('Introdu string-ul dorit: ')
primul_char = string4[0]
# print(primul_char)
string_all_big = string4.replace(primul_char, primul_char.upper())
first_string_lower= string_all_big[0].lower()+string_all_big[1:]
string_without_last_character = first_string_lower[:-1]
last_letter_lower = string4[-1].lower()
all_ok = string_without_last_character + last_letter_lower
print(all_ok)

#c.17
string17 = input('Scrie un string: ')
string17_invers = string17[::-1]
assert string17 == string17_invers # sa verificam daca cuvantul este palindrom

# print(x[len(x)-1]) = asa se afiseaza caracterul de la un index specificat