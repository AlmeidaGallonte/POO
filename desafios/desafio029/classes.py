from rich import print
class Diario:
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()


       
    def escrever(self,msg):
        if isinstance(msg, str) and len(msg) > 0 :
            self.__segredos.append(msg.strip())
        
    def ler(self,senha = None):
        if senha != self.__senha:
            raise PermissionError('NAOOOOOOOOOOOOO')
        else:
            print(f'[green]SIMMMMMMMMMM[/]')


    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de cer a senha")
        
    @senha.setter
    def senha(self, novasenha):
        pass