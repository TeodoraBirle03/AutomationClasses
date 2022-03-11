class Nerfgun:
    # atribute/ fields
    model = None
    culoare = None
    culori_posibile = {'alb', 'negru', 'rosu'}
    nr_gloante = 0
    piedica = True

    # constructor
    def __init__(self, model, culoare):
        self.model = model
        if culoare in self.culori_posibile:
            self.culoare = culoare
        else:
            print(f'la initializarea obiectului {model} culoarea este invalida!')

    # metode
    def descrie(self):
        print(f'modelul este: {self.model}')
        print(f'culoarea este: {self.culoare}')
        print(f'gloantele sunt: {self.nr_gloante}')
        print(f'piedica este: {self.piedica}')

    def scoate_piedica(self):
        self.piedica = False
        print(f'ai scos piedica cu succes')

    def pune_piedica(self):
        self.piedica = True
        print(f'ai pus piedica cu succes')

    def trage(self):
        if self.piedica == False and self.nr_gloante > 0:
            self.nr_gloante = self.nr_gloante - 1
            print('pac, pac')
        else:
            print(f'nu poti trage! verifica piedica scoasa si nr de gloante')

    def incarca(self, gloante_input):
        if gloante_input >= 10:
            self.nr_gloante = 10
        elif gloante_input <= 0:
            print(f'{gloante_input} invalide')
        else:
            self.nr_gloante = gloante_input


# initializam obiecte
nerf1 = Nerfgun('glock', 'alb')
nerf2 = Nerfgun('beretta', 'roz')
nerf1.descrie()
nerf2.descrie()
nerf2.culoare = 'mov'
nerf2.descrie()
nerf1.scoate_piedica()
nerf1.trage()
nerf1.incarca(11)
nerf1.trage()
nerf1.trage()
nerf1.descrie()
nerf1.pune_piedica()
nerf1.trage()
nerf1.descrie()
nerf2.incarca(1)
nerf2.scoate_piedica()
nerf2.trage()
nerf2.trage()