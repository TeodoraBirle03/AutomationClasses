'''Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

1.Clasa Cerc
  Atribute: raza, culoare
  Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()'''

class Cerc:
    # atribute
    raza = 0
    culoare = None

    # constructor
    def __init__(self, raza_input, culoare_input):
        self.raza = raza_input
        self.culoare = culoare_input

    # metode
    def descrie(self):
        print(f'raza cercului: {self.raza}')
        print(f'culoarea cercului: {self.culoare}')

    def arie_cerc(self):
        PI = 3.14
        arie_cerc = PI * self.raza * self.raza
        return (f'Aria cercului este: {arie_cerc.__round__(2)}')

    def diametru_cerc(self):
        diametru = 2 * self.raza
        return(f'Diametrul cercului este : {diametru.__round__(2)}')

    def circumferinta_cerc(self):
        PI = 3.14
        circumferinta = 2 * self.raza * PI
        return (f'Circumferinta cercului este: {circumferinta.__round__(2)}')

# de ce nu pot pune constanta PI ca variabila intre atributele clasei?
# obiectele clasei
Cerc_mare = Cerc( 20, 'roz')
Cerc_mic = Cerc( 4, 'verde')

Cerc_mare.descrie()
print(Cerc_mare.arie_cerc())
print(Cerc_mare.diametru_cerc())
print(Cerc_mare.circumferinta_cerc())
Cerc_mic.descrie()
print(Cerc_mic.arie_cerc())
print(Cerc_mic.diametru_cerc())
print(Cerc_mic.circumferinta_cerc())


'''2.Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''

class Dreptunghi:
    # atributele
    lungime = 0
    latime = 0
    culoare = None

    # constructorul clasei
    def __init__(self, lungime_input, latime_input, culoare_input):
        self.lungime = lungime_input
        self.latime = latime_input
        self.culoare = culoare_input

    # metodele clasei
    def descrie(self):
        print(f'Lungimea este: {self.lungime}')
        print(f'Latimea este: {self.latime}')
        print(f'Culoarea este: {self.culoare}')

    def aria(self):
        arie = self.lungime * self.latime
        print(f'Aria dreptunghiului este: {arie}')

    def perimetru(self):
        perimetru = (self.lungime * 2) + (self.latime * 2) # stie ordinea operatiilor?
        print(f'Perimetrul dreptunghiului este: {perimetru}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare # suprascriem valoarea variabilei culoare, cu noua culoare

# obiectele
dreptunghi1 = Dreptunghi(6, 4, 'gri')
dreptunghi2 = Dreptunghi(78, 52, 'rosu')

dreptunghi1.descrie()
dreptunghi1.aria()
dreptunghi1.perimetru()
dreptunghi1.schimba_culoarea('portocaliu')
dreptunghi1.descrie()
dreptunghi2.descrie()
dreptunghi2.aria()
dreptunghi2.perimetru()
dreptunghi2.schimba_culoarea('mov')
dreptunghi2.descrie()

'''3.Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)'''

class angajat:
    # atribute
    nume = None
    prenume = None
    salariu = 0

    # constructorul clasei
    def __init__(self, nume_input, prenume_input, salariu_input):
        self.nume = nume_input
        self.prenume = prenume_input
        self.salariu = salariu_input

    # metodele(functii in cadrul unei clase)
    def descrie(self):
        print(f'Numele angajatului este: {self.nume}')
        print(f'Prenumele angajatului este: {self.prenume}')
        print(f'Salariul angajatului este: {self.salariu}')

    def nume_complet(self):
        return  (f'{self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar a lui {self.nume_complet()} este {self.salariu}')

    def salariu_anual(self):
        sal_anual = self.salariu * 12
        return (f'Salariul anual este: {sal_anual}')

    def marire_salariu(self, procent_marire):
        self.salariu = self.salariu + (self.salariu * procent_marire/100) # suprascriem valoarea salariului cu salariu marit
        print(f'Dupa marirea cu {procent_marire}% salariul a devenit: {self.salariu}')

angajat1 = angajat('Popescu', 'Ionel', 480)
angajat2 = angajat('Vuscan', 'Doina', 650)

angajat1.descrie()
print(angajat1.nume_complet())
angajat1.salariu_lunar()
print(angajat1.salariu_anual())
angajat1.marire_salariu(10)
angajat2.descrie()
print(angajat2.nume_complet())
angajat2.salariu_lunar()
print(angajat2.salariu_anual())
angajat2.marire_salariu(5)

'''4.Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
numar, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)

genereaza_factura() - va printa tabelar daca reusiti
Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/'''

class Factura:
    # atribute
    SERIA = 'FX'
    numar_factura = 0
    nume_produs = None
    cantitatea = 0
    pret_buc = 0.00

    # constructor
    def __init__(self, numarf_input, numeprod_input, cantitate_input, pret_input):
        self.numar_factura = numarf_input
        self.nume_produs = numeprod_input
        self.cantitatea = cantitate_input
        self.pret_buc = pret_input

    # metode
    def schimba_cantitatea(self, noua_cantitate):
        self.cantitatea = noua_cantitate
        print(f'Noua cantitate este: {self.cantitatea}')

    def schimba_pretul(self, noul_pret):
        self.pret_buc = noul_pret
        print(f'Noul pret/buc este: {self.pret_buc}')

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        print(f'Noul nume este: {self.nume_produs}')

    def generare_factura(self):
        print(f'Factura seria {self.SERIA} numar {self.numar_factura}')
        from datetime import date # se importa o clasa dintr-un alt file pt a genera data
        today = date.today()
        print(f'Data este: {today}')
        total = self.cantitatea * self.pret_buc
        print(f'Produs    | cantitatea | pret bucata | totalul ')
        print(f'{self.nume_produs} |     {self.cantitatea}     |   {self.pret_buc}      | {total} ')

factura1 = Factura(26, 'Telefon', 1, 500)
factura2 = Factura(897, 'Husa', 25, 45)
factura1.schimba_cantitatea(7)
factura1.schimba_pretul(520)
factura1.schimba_nume_produs('Smartphone')
factura1.generare_factura()
factura2.schimba_cantitatea(40)
factura2.schimba_pretul(30)
factura2.schimba_nume_produs('Husa protectie')
factura2.generare_factura()

'''5.Clasa Cont
Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''
class Cont:
    #atribute
    iban = None
    titular_cont = None
    sold = 0.00

    # constructor
    def  __init__(self, iban_input, titular_input, sold_input):
        self.iban = iban_input
        self.titular_cont = titular_input
        self.sold = sold_input

    # metode
    def afisare_sold(self):
        print(f'Titularul contului {self.titular_cont} are in contul {self.iban}, suma de {self.sold} Ron')

    def debitare_cont(self, suma_debitata):
        if self.sold > 0 and self.sold > suma_debitata:
            self.sold = self.sold - suma_debitata
            print(f'Mai aveti {self.sold} Ron disponibili')
        else:
            print (f'Fonduri insuficiente')

    def creditare_cont(self, suma_creditata):
        self.sold = self.sold + suma_creditata
        print(f'Contul dvs a fost creditat cu suma de {suma_creditata} Ron')
        print(f'Aveti in cont: {self.sold} Ron')

cont1 = Cont('ING44RO452', 'Pop Vlad', 5000)
cont2 = Cont ('ING48RO458', 'Trif Adela', 79000)
cont1.afisare_sold()
cont1.debitare_cont(850)
cont1.creditare_cont(150)
cont2.afisare_sold()
cont2.debitare_cont(80000)
cont2.creditare_cont(10000)

'''6.Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0'''

class Masina:
    # atributele clasei
    marca = 'Honda'
    model = None
    viteza_max = 0
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'neagra', 'alba', 'verde', 'rosie', 'albastra', 'roz'}
    inmatriculata = False

    # constructor
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_max = viteza_maxima

    # metodele
    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_max}km/h')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}km/h')
        print(f'Culoarea actuala a masinii este: {self.culoare}')
        print(f'Masina este inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        print(f'Masina dvs este acum inmatriculata: {self.inmatriculata}')

    def vopseste(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii dvs este: {self.culoare}')
        else:
            print(f'Culoarea aleasa nu face parte din oferta noastra')

    def accelereaza(self, viteza):
        if viteza < self.viteza_actuala:
            print(f'Atentie, valoarea introdusa este invalida!')
        elif viteza <= self.viteza_max:
            self.viteza_actuala = viteza
            print(f'Ati accelerat pana la viteza de: {self.viteza_actuala}km/h')
        else:
            self.viteza_actuala = self.viteza_max
            print(f'Ati atins viteza maxima de: {self.viteza_actuala}km/h')

    def franeaza(self):
        # if viteza > 0 and viteza < self.viteza_max:# masina sa fie in mers, dar e nevoie de un parametru pt viteza
        # if self.viteza_actuala == self.accelereaza(120):
            self.viteza_actuala = 0
            print(f'Masina s-a oprit, viteza dvs este: {self.viteza_actuala}')


masina1 = Masina('Acord', 240)
masina2 = Masina('Civic', 180)

masina1.descrie()
masina1.inmatriculare()
masina1.vopseste('mov')
masina1.vopseste('neagra')
masina1.accelereaza(120)
masina1.accelereaza(-56)
masina1.accelereaza(280)
masina1.franeaza()
masina2.descrie()
masina2.inmatriculare()
masina2.vopseste('rosie')
masina2.accelereaza(130)
masina2.franeaza()

'''7. Clasa TodoList
 Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task() - se va adauga in dict
finalizeaza_task() - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''

class TodoList:
    # atribute
    todo = {}

    # metode
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(f'Lista de task-uri a devenit: {self.todo}')

    def finalizeaza_task(self, nume):
        self.todo[nume] = self.todo.pop(nume)
        print(f'Task-ul {self.todo[nume]} a fost finalizat')
        print(f'Lista de task-uri a devenit: {self.todo}')

    def afiseaza_todo_list(self):
            print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo.keys():
            print(f'Detaliile acestui task sunt: {self.todo.get(nume_task)}')
        else:
            print(f'Doriti sa adaugati {nume_task} in lista?')
            raspuns = True
            if raspuns == False:
                print(f'Copilul nu este pregatit pentru scoala')
            else:
                self.todo['Coloreaza'] = 'ramane in contur'
                print(f'Lista a devenit: {self.todo}')


list1 = TodoList()
list2 = TodoList()

list1.adauga_task('Scrie', 'stie sa scrie cifre si litere')
list1.adauga_task('Citeste', 'citeste cuvinte scurte')
list1.adauga_task('Numara', 'numara pana la 100')
list1.finalizeaza_task('Scrie')
list1.afiseaza_todo_list()
list1.afiseaza_detalii_suplimentare('Citeste')
list1.afiseaza_detalii_suplimentare('Coloreaza')
list2.adauga_task('Calculeaza', 'face calcule simple')
list2.finalizeaza_task('Calculeaza')
list2.afiseaza_todo_list()
list2.afiseaza_detalii_suplimentare('Scrie')
