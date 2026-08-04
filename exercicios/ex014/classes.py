class Mãe():
    def __init__(self,nome = 'Mamãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite condensado e calda')
    def fritar_coxinha(self):
        print(f'{self.nome} faz COXINHA no óleo de soja')

class Filha(Mãe):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite Ninho com Nutella')

class Filho(Mãe):
    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA na Air Fryer')