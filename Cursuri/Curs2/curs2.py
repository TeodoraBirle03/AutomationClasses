# operatori de atribuire
x = 3
x += 7 # la fel ca si x = x + 7
print(x)

# operatori aritmetici
print(4 + 6)
print (10 % 3)
print ( 5 ** 2)

# operatori de comparare
print (3 != 3) # => 3 este diferit de 3
print (3 == 3) # => 3 este egal cu 3?
print (3 <= 3) # 3 este mai mic sau egal cu 3

# operatori logici = and/or/not
print (3>0 and 5>0)
# true and true => true
print (-3>0 and 5>0)
# false and true => false
print (-3>0 or 5>0)
# false or true => true
print (-3>0 or -5>0)
# false or false => false
print(not(-3>0 or -5>0)) # concluzia e false dar o intorc => true

# putem complica cat vrem noi
print(-3>0 or 3 >0 and 5>0)
# false  or (true and true) => false or true => true
print(not(-3>0 or 3 >0 and 5>0))
# negarea rezultatului not(true) => false

# if
NOTA_DE_TRECERE_EXAMEN = 4.5 # asa este o constanta, semnalata cu litere mari,nu se suprascrie
NOTA_DE_TRECERE_PURTARE = 7
if 7 >= NOTA_DE_TRECERE_EXAMEN and 9 >= NOTA_DE_TRECERE_PURTARE:
    print('am trecut') # 4 spatii la inceput se numeste identare

# if else - controlam pe unde trece codul, un branch, codul trece printr-o anumita ramura
nota_examen = 10
nota_purtare = 10
if 7 >= NOTA_DE_TRECERE_EXAMEN and 9 >= NOTA_DE_TRECERE_PURTARE:
    print('Am trecut') # 4 spatii la inceput se numeste identare
    if nota_examen  and nota_purtare:
        print('ai luat premiul intai')
else: # nu are conditie, pentru ca e ceea ce a mai ramas
    print('Nu am trecut')

# if else if ... if elif else
