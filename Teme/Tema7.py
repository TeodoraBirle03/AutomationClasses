# Abstraction
'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''

from abc import ABC, abstractmethod # importam aceasta metoda pt a putea folosi metoga abstracta din clasa parinte

class FormaGeometrica: # clasa parinte
    PI = 3.14 # atribut de tip constanta

    @abstractmethod # metoda abstracta in care nu definim nimic, dar obligam clasa copil sa scrie o logica in acesta metoda
    def aria(self):
        raise NotImplementedError

    def descrie(self): # metoda logica
        print(f'Cel mai probabil am colturi')

class Patrat(FormaGeometrica): # clasa copil care mosteneste clasa parinte
    __latura = 0 # variabila latura este privata, se ascunde

    # are un costructor
    def __init__(self, latura):
        self.__latura = latura

    @property # este un decorator, metoda intrinseca Python, care ne ajuta sa folosim getter/setter/deleter
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura are dimensiunea: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Noua dimesiune a laturii este: {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Am sters valoarea laturii')
        self.__latura = 0

    def aria(self):
        self.aria = self.__latura * self.__latura
        return self.aria

class Cerc(FormaGeometrica): # clasa copil Cerc
    __raza = 0
    # constructorul clasei copil Cerc
    def __init__(self, raza):
        self.__raza = raza

    @property # decoratorul pt getter/setter/deleter
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = 0

    def aria(self): # metoda abstracta din clasa parinte, care are logica specifica clasei copil
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului.__round__(2)

    def descrie(self): # metoda logica din parinte, care se suprascrie = polimorfism
        print(f'Eu nu am colturi')

patrat1 = Patrat(10)  # definim obiectul patrat1 de tip Patrat
patrat1.descrie()   # accesam metoda descrie din parinte
print(patrat1.aria()) # accesam metoda aria din parinte cu logica in clasa copil
patrat1.latura # getter
patrat1.latura = 15 # setter
del patrat1.latura # deleter
patrat1.latura # din nou getter, cu valoarea dupa deleter


cerc1 = Cerc(3)
cerc1.descrie()
print(cerc1.aria())
cerc1.raza
cerc1.raza = 9
print(cerc1.aria())
del cerc1.raza
cerc1.raza
print(cerc1.aria())





