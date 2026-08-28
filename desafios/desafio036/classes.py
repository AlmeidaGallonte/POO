from abc import ABC

class Pagamento(ABC):
    def __int__(self):
        self._valor = 0
        self.fvalor = f'R$ {self.valor:,.2f}'

    @property
    def fvalor(self):
        return self.fvalor
    
    @fvalor.setter
    def fvalor(self, valor):
        self.fvalor = valor

    def pagar():
        pass


class Boleto(Pagamento):
    def __int__(self):
        super().__int__()

class PIX(Pagamento):
    def __int__(self):
        super().__int__()

class Crédito(Pagamento):
    def __init__(self):
        super().__init__()

def finalizar_compra(tipo_pag, valor:float):
    print(f'Pagamento COMFIRMADO de R$ {valor:,.2f} via {tipo_pag.__class__.__name__}')