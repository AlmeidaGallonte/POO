from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self,valor):
        print(f'não foi possivel analisar o valor {valor}')

    @analisar.register
    def _(self, valor:int):
        print(f'{valor} é um número Inteiro')

    @analisar.register
    def _(self, valor:str):
        print(f'{valor} é uma cadeia de caracteres')