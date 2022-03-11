# Abstraction
'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''

from abc import ABC, abstractmethod

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

    @property
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
        self.__latura = None

    def aria(self):
        self.aria = self.__latura * self.__latura
        return self.aria

class Cerc(FormaGeometrica):
    __raza = 0
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului.__round__(2)

    def descrie(self):
        print(f'Eu nu am colturi')

patrat1 = Patrat(10)
patrat1.descrie()
print(patrat1.aria())


cerc1 = Cerc(3)
cerc1.descrie()
print(cerc1.aria())






