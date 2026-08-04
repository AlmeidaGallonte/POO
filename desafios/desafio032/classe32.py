from hashlib import sha256

class ContaBancaria:
    """
Cria uma conta báncaria e permite fazer saques e depósitos    
    """
    def __init__(self,id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id
        self._titular = nome 
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f'Conta {self._id} criada com sucesso. saldo atual de R${self.__saldo:,.2f}')

    def pede_senha(self):

        while True:
            senha = str(input('Senha: ')).strip()
            if len(senha) >= 6:
                break 

        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} AUTORIZADO!')


    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()


        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque de R${valor:,.2f} NEGADO! na conta {self._id}:SALDO INSUFICIENTE')
            else:
                self.__saldo -= valor 
                print(f'saque de R${valor:,.2f} AUTORIZADO! na conta {self._id}. saldo atual R${self.__saldo:,.2f}')
        else:
            print('Senha nao confere. Saque negado!')

        @property
        def nome(self):
            return self._titular
        
        @nome.setter
        def nome(self, novonome:str = None):
            chave = self.pede_senha()
            
            if self.validar_senha(chave):
                if len(novonome) >= 5:
                    self._titular = novonome
            else:
                print('Senha não confere. Não foi possivel alterar o nome!')