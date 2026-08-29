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
                return True
            else:
                return False
            


class Email(Validador):
    import string
    p = 0
    
    def validar(self,email):

        if email.count('@') == 1:
            self.p += 1

        if self.p == 1:
            print(True)
        else:
            print(False)


class Senha(Validador):
    import string
    p = 0
    
    def validar(self,senha:str):

        if len(senha) >= 8:
            self.p += 1
        if any(c.isupper() for c in senha):
            self.p += 1
        if any(c.islower() for c in senha):
            self.p += 1
        if any(c in self.string.punctuation for c in senha):
            self.p += 1

        if self.p == 4:
            return True
        else:
            return False
