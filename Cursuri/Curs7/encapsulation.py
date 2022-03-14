# encapsulation = cand ascundem atributele si folosim getter si setter sa ajungem la ele
# si metodele pot fi private, nu doar atributele
# ele se ascund daca punem __ inainte
import random


class Car:
    __color = 'gray'

    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita

    def delete_color(self):
        self.__color = None

    def __hidden(self):
        pass


volvo = Car()
print(volvo.get_color()) # getter
volvo.set_color('red') # setter
print(volvo.get_color()) # getter
volvo.delete_color() # deleter
print(volvo.get_color()) # getter



class CarPy:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            self.__color = 'gray'
        else:
            self.__color = color
        print(f'Setter: Noua culoare este {color}')


    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color = None


car2 = CarPy('gray')
car2.color = 'red' # set color
car2.color # get color
del car2.color # del color
car2.color # get color
print('--------------------------------')
car3 = CarPy('white')
print(car3.color) # get color
car3.color = 'black'
print(car3.color)
del car3.color
print(car3.color)