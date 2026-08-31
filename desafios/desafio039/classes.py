from abc import ABC, abstractmethod
from rich import print

class Validador(ABC):
    @abstractmethod
    def validar(self):
        pass
class Usuário(Validador):
    def validar(self,usuario:str):
        if 5<= len(usuario) <= 20:
            if usuario == usuario.lower():
                print(True)
            else:
                print(False)

class Email(Validador):
    import string
    p = 0
    
    def validar(self,email):

        if ' ' in email:
            self.p -= 1 
        if email.count('@') == 1 and email.index('@') != 0:
            self.p += 1
        if email.count(self.string.punctuation) <= 2:
            self.p += 1
        if email[-4] == '.':
            self.p += 1

        if self.p == 3:
            print(True)
        else:
            print(False)

class Senha(Validador):
    import string
    p = 0

    def validar(self,senha:str):
        if any(c.isdigit() for c in senha):
            self.p += 1
        if len(senha) >= 8:
            self.p += 1
        if any(c.isupper() for c in senha):
            self.p += 1
        if any(c.islower() for c in senha):
            self.p += 1
        if any(c in self.string.punctuation for c in senha):
            self.p += 1

        if self.p == 5:
            print(True)
        else:
            print(False)

def validar_dado(validador:Validador, valor:str):
    validador.validar(valor)