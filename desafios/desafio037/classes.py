from rich import print
from rich.panel import Panel



class Mensagem:
    def __init__(self, mensagem):
        self.msg = mensagem

    def mostrar(self):
        print(Panel(f'{self.msg}', style='white on black', border_style='white',expand=False, title = ' () AVISO ()'))

class Erro(Mensagem):

    def mostrar(self):
            print(Panel(f'{self.msg}', style='yellow on red', border_style='yellow',expand=False, title = '(X) ERRO (X)'))

class Alerta(Mensagem):

    def mostrar(self):
            print(Panel(f'{self.msg}', style='black on yellow', border_style='black',expand=False, title = '(!) ALERTA (!)'))