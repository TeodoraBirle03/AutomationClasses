
import random

class Caine:
    # atribute
    rasa = None
    nume = None
    culoare = None
    nume_stapan = None
    varsta = None

    def __init__(self, rasa, nume, culoare):
        self.rasa = rasa
        self.varsta = 1
        self.nume = nume
        self.culoare = culoare

    # metode
    def ani_cainesti(self):
        return self.varsta * 7

    def descrie(self):
        print(f'nume: {self.nume}')
        print(f'culoare: {self.culoare}')
        print(f'varsta: {self.ani_cainesti()}')

    def la_multi_ani(self):
        self.varsta += 1

    def latra(self):
        n = random.randint(1,3)
        print(self.nume + ':')
        print(f'Ham!' * n)


Grivei = Caine('golden', 'Grivei', 'alb')
Azorel = Caine('doberman', 'Azorel', 'negru')

Grivei.descrie()
Azorel.descrie()
Azorel.la_multi_ani()
Azorel.descrie()
Azorel.nume = 'Zdreanta'
Azorel.descrie()
Zdreanta = Azorel
Zdreanta.la_multi_ani()
Zdreanta.latra()
Zdreanta.descrie()