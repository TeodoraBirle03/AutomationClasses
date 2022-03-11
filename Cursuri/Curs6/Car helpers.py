class Car:
    # fields (atribute)
    marca = 'Dacia'
    model = None
    culoare = None
    casatorit = None

    # constructor
    def __init__(self, model, culoare):
        self.model = model # self-ul este un placeholder pentru ce urmeaza
        self.culoare = culoare + 'uriu'
        # if varsta < 13:
        #     self.casatorit = False

    # metode
    def acclerate(self):
        print('Vruuuuummmm!')

    def paint(self, noua_culoare):
        self.culoare = noua_culoare

car1 = Car('Logan', 'alb')
car1.acclerate()
car1.paint('rosuuuuu')
car2 = Car('Duster', 'portocaliu')
print(car1.culoare)
print(car2.model)
# car1.culoare = 'alb'
# print(car1.culoare)
# car1.marca
# print(car1.marca)
#
# car2.culoare = 'rosu'
# print(car2.culoare)