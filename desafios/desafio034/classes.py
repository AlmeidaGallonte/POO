from abc import ABC,abstractmethod
from rich import print

class Funcionario(ABC):
    def __init__(self,nome:str = '',salario:int|float = 0):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
         return self._salario
    
    @salario.setter
    def salario(self, valor):
         if valor >= self._salario:
            self._salario = valor
         else:
             print(f'[red]ERRO:tentativa de mudar salario pra {valor}. Não pode reduzir salario de um Funcionario![/]')
    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
            return f'{self.nome} ganha R${self._salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}'

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


    
class Desingner(Funcionario):
    def calcular_bonus(self):
           return self.salario * 0.08
        


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10
        

    
def tentar_bonus(obj):
    try:
        obj.calcular_bonus()
    except:
         print(f'Erro ao tentar calcular o bonus')

