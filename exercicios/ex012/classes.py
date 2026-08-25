from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ''):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo um som')

class Pato(Animal):
    def emitir_som(self):
        print(f'{self.nome} quak quak')

class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} Au Au Au')

class Pitbull(Cachorro):
     def emitir_som(self):
             print(f'{self.nome} Aaaaaaaaah vou te matar')

class Spitz(Cachorro):
     pass

class Gato(Animal):
    def emitir_som(self):
            print(f'{self.nome} MIauuuuuu MIAIIIIaaaaaaauuuu')

class Galinha(Animal):
    def emitir_som(self):
            print(f'{self.nome} co co  oco coc')
